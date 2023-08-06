import sys
import time
import traceback

import gevent
import gevent.monkey
from gevent.pool import Pool
from gevent.queue import Queue
from gevent.server import StreamServer

# patch_all() patch_thread() may cause thread exception at the end of app
gevent.monkey.patch_all(thread=False)

import logger
import proxy
import params
from cubi.proxy import Query, Answer, Messager
from cubi.params import Params


class Adapter(object):

    def __init__(self, name, endpoint, servant_num=512, accept_pool_size=512):
        self._name = name

        self._endpoint = endpoint
        self._query_queue = Queue()
        self._servants = {}
        self._servers = []

        self._servant_worker_num = servant_num
        self._accept_pool_num = accept_pool_size
        self._running = True
        self._wildcard_servant = None
        self._pool = None

    def __repr__(self):
        p = {}
        p['servant_num'] = self._servant_worker_num
        p['accept_pool_size'] = self._accept_pool_num
        p['endpoint'] = self._endpoint
        p['servants'] = self._servants
        p['pool_free_count'] = self._pool.free_count()
        return str(p)

    def get_name(self):
        return self._name

    # servant is a function with param (service, method, params)
    # special servant handle all service query
    # for somthing like proxy
    def add_wildcard_servant(self, servant):
        if len(self.servant) > 0:
            raise params.EngineError("normal servant is not empty when add wildcard servant")
        self._wildcard_servant = servant

    def add_servant(self, service, servant):
        if service == '*':
            self.add_wildcard_servant(servant)
            return
        if self._wildcard_servant:
            raise params.EngineError("wildcard servant is set when add normal servant")
        self._servants[service] = servant

    def _make_exception_params(self, query):
        exdict = {}
        exctype, exmsg, tb = sys.exc_info()
        exdict['exception'] = repr(exctype)
        exdict['code'] = 1
        exdict['message'] = repr(exmsg)
        exdict['raiser'] = query.method + "*" + query.service + self._endpoint
        exdict['detail'] = {}
        exdict['detail']['what'] = repr(traceback.extract_tb(tb))
        return exdict

    def _handle_wildcard_servant(self, query):
        logger.get_logger().debug('handle_wildcard_servant: %s', query)
        try:
            result = self._wildcard_servant(query.service, query.method, query.params)
            if query.qid:
                query.inbox.put(Answer(query.qid, 0, result))
        except proxy.ProxyError as ex:
            if query.qid:
                query.inbox.put(Answer(ex.qid, ex.status, ex.params))
        except:
            if query.qid:
                query.inbox.put(Answer(query.qid, 1, self._make_exception_params(query)))

    def _handle_normal_servant(self, query):
        called_method = query.method
        logger.get_logger().debug('handle_normal_servant: %s', query)
        servant = self._servants.get(query.service)
        if not servant:
            # build exception at params
            exdict = {}
            exdict['exception'] = 'ServantNotFound'
            exdict['code'] = 1
            exdict['message'] = "servant %s not found in adapter %s" % (query.service, self._endpoint)
            exdict['raiser'] = self._endpoint
            if query.qid:
                query.inbox.put(Answer(query.qid, 1, exdict))
            else:
                logger.get_logger().warning("%s.%s %s", query.service, called_method, exdict)
            return

        if called_method[0] == '\0':
            callback = servant._special_callback(query)
        else:
            callback = servant.find_method(called_method)

        if not callback:
            self._method_not_found(called_method, query)
            return

        try:
            time_start = time.time()
            servant.before_method_call(called_method, time_start)
            result = callback(Params(query.params))
            servant.after_method_call(called_method, time_start, (time.time() - time_start) * 1000)
            if query.qid:
                result = dict(result)
                query.inbox.put(Answer(query.qid, 0, result))
        except proxy.ProxyError as ex:
            if query.qid:
                query.inbox.put(Answer(query.qid, ex.status, ex.params))
            else:
                logger.get_logger().warning("%s.%s %d %s", query.service, called_method, ex.status, ex.params)
        except:
            logger.get_logger().error("query %d handle fail", query.qid, exc_info=1)
            if query.qid:
                query.inbox.put(Answer(query.qid, 1, self._make_exception_params(query)))

    def _method_not_found(self, called_method, query):
        logger.get_logger().error("method %s not found", called_method)
        """
        query method not found in servant
        """
        exdict = {}
        exdict['exception'] = 'MethodNotFound'
        exdict['code'] = 1
        exdict['message'] = "servant %s do no have method %s in adapter %s" % (
        query.service, called_method, self._endpoint)
        exdict['raiser'] = self._endpoint
        if query.qid:
            query.inbox.put(Answer(query.qid, 100, exdict))
        else:
            logger.get_logger().warning("%s.%s %s", query.service, called_method, exdict)
        return

    def servant_worker(self):
        while self._running:
            query = self._query_queue.get()
            if not isinstance(query, Query):
                logger.get_logger().error('invalid query %s', query)
                continue
            if not self._wildcard_servant:
                self._handle_normal_servant(query)
            else:
                self._handle_wildcard_servant(query)

    def activate(self):
        for i in range(self._servant_worker_num):
            gevent.spawn(self.servant_worker)

        self._pool = Pool(self._accept_pool_num)
        endpoint = self._endpoint
        try:
            service, host, port = proxy.parse_endpoint(endpoint)
            server = StreamServer((host, int(port)), self.sokect_handler, spawn=self._pool)
            logger.get_logger().debug('adapter start %s', endpoint)
            self._servers.append(server)
            server.start()
        except:
            logger.get_logger().error('start adapter fail %s', endpoint, exc_info=1)

    def deactivate(self):
        for server in self._servers:
            server.stop()
        self._servers = []
        self._running = False

    def answer_fiber(self, socket, address, inbox):
        for answer in inbox:
            if not isinstance(answer, Answer):
                logger.get_logger().error('invalid answer %s', answer)
                continue

            logger.get_logger().debug('%s: reply answer: %s', address, answer)
            socket.sendall(answer.get_data())
            logger.get_logger().debug('%s: answer fiber stop', address)

    def sokect_handler(self, socket, address):
        logger.get_logger().debug('%s: accept connection', address)

        # send welcome
        socket.sendall(Messager.data_for_welcome())
        conn_inbox = Queue()
        answer_thread = gevent.spawn(self.answer_fiber, socket, address, conn_inbox)
        while self._running:
            try:
                message = Messager.receive_msg(socket)
                if not message:
                    logger.get_logger().debug('%s: connection has been closed by client.', address)
                    break;
                if isinstance(message, Answer):
                    logger.get_logger().error('%s: unexpected message received: %s', address, message)
                    continue
                elif isinstance(message, Query):
                    logger.get_logger().debug('%s: message received: %s', address, message)
                    message.inbox = conn_inbox
                    self._query_queue.put(message)
            except gevent.socket.error as ex:
                logger.get_logger().error('%s: socket error: %s', address, repr(ex))
                break
            except:
                logger.get_logger().error('%s: exception: %s', address, traceback.format_exc())
                break

        logger.get_logger().debug('%s: close connection', address)
        socket.close()
        # stop answer thread
        conn_inbox.put(StopIteration)


class Servant(object):

    def __init__(self, engine):
        self.engine = engine
        self.__reflection_service_methods()

    def __reflection_service_methods(self):
        method_map = {}
        for name in dir(self):
            attr = getattr(self, name)
            if name[0] == '_':
                continue
            if callable(attr):
                method_map[name] = attr
        self.method_map = method_map

    def _special_callback(self, query):
        if query.method == '\0':
            return self._probe
        else:
            raise AttributeError('special method %s not support' % (query.method,))

    def _probe(self, params):
        """
        special probe method for servants internal status
        """
        sta = {}
        sta['methods'] = self.method_map.keys()
        return sta

    def find_method(self, method):
        if method in self.method_map:
            return self.method_map[method]
        return None

    def before_method_call(self, method, time_start):
        pass

    def after_method_call(self, method, time_start, time_spent):
        pass

    def __repr__(self):
        p = {}
        return str(p)


class Engine(object):

    def __init__(self, setting={}):
        self.setting = setting
        self._running = True
        self._adapters = {}
        self._proxies = {}
        logger.get_logger().debug("application setting %s", setting)

    def create_proxy(self, endpoint, timeout=6000):
        prx = proxy.Proxy(endpoint, timeout=timeout)
        self._proxies[endpoint] = prx
        return prx

    def add_adpater(self, adapter):
        name = adapter.get_name()
        self._adapters[name] = adapter

    def stop(self):
        for adp in self._adapters:
            self._adapters[adp].deactivate()
        self._running = False

    def serve_forever(self):
        for (name, adapter) in self._adapters.items():
            adapter.activate()

        self.start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        while self._running:
            # periodic log info that engine is running
            p = {}
            p['start_time'] = self.start_time
            p['adapters'] = self._adapters
            logger.get_logger().critical("THROB %s", str(p))
            gevent.sleep(60)
