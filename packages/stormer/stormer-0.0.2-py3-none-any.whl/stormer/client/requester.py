# -*- coding: utf-8 -*-
"""
Created By Murray(m18527) on 2019/12/13 13:57
"""
import json
from urllib.parse import urljoin

import redis
import requests

from .respresult import RespResult
from ..utils.config import config
from ..utils.logger import logging

logger = logging.getLogger(__name__)


class Requester(object):
    """Requester is request Class which base on questions, it be used for send request."""

    def __init__(self, server_url, headers=None, config_module=None, redis_url=None, timeout=0):
        """
        Init Requester
        :param config_module: config module
        """
        self.headers = headers
        self.server_url = server_url
        self.redis_url = redis_url
        self.timeout = timeout
        self.redis_conn = None
        self.apis = []

        if self.redis_url:
            try:
                self.redis_conn = redis.Redis(connection_pool=redis.ConnectionPool.from_url(self.redis_url))
            except ConnectionError:
                logger.warning("Redis connection pool is max number of clients reached, now disconnect.")
                self.redis_conn.connection_pool.disconnect()

        if config_module:
            try:
                config.from_obj(config_module)
            except Exception as e:
                logger.error("Error: set config fail, Detail: {}".format(e))

    @staticmethod
    def gen_md5(text, salt='_stormer_requester_'):
        import hashlib
        md = hashlib.md5()
        md.update("{}{}".format(text, salt).encode("utf-8"))
        res = md.hexdigest()
        return res

    @staticmethod
    def set_config_module(module):
        try:
            config.from_obj(module)
        except Exception as e:
            logger.error("Error: set config fail, Detail: {}".format(e))

    @classmethod
    def build_params_hash(cls, url, params, **kwargs):
        new_params = {k: v for k, v in (params or {}).items()}
        new_params.update({"url": url})
        new_params.update(kwargs)
        new_params = json.dumps(new_params, sort_keys=True)
        return str(cls.gen_md5(new_params)).upper()

    @staticmethod
    def _path_url(url, path_params):
        if path_params and isinstance(path_params, dict):
            url = url.format(**path_params)
        return url

    def _bind_func(self, pre_url, action, timeout=0):
        def req(path_params=None, params=None, data=None, json=None, files=None, headers=None, **kwargs):
            url = self._path_url(pre_url, path_params)
            params_hash, resp_result = None, None
            if self.redis_conn and timeout:
                params_hash = self.build_params_hash(url, params, **kwargs)
                resp_result = RespResult.from_cache(params_hash, action, self.redis_conn)
            if not resp_result:
                resp = self._do_request(action, url, params, data, json, files, headers, **kwargs)
                resp_result = RespResult(resp, url, action, redis_conn=self.redis_conn, params_hash=params_hash)
                resp_result.set_cache(timeout)
            return resp_result

        return req

    def _add_path(self, action, uri, func_name, timeout=0):
        action = action.upper()
        func_name = func_name.lower()
        assert func_name not in self.apis, u"Duplicate function {}.".format(func_name)
        url = urljoin(self.server_url, uri)
        setattr(self, func_name, self._bind_func(url, action, timeout=timeout))
        self.apis.append(func_name)
        return getattr(self, func_name)

    @staticmethod
    def _func_name(func):
        try:
            func_name = func.__name__
        except (Exception,):
            func_name = str(func)
        return func_name

    def register(self, action, func, uri, timeout=0):
        func_name = self._func_name(func)
        return self._add_path(action, uri, func_name, timeout=timeout or self.timeout)

    def _headers(self, headers):
        """combine headers"""
        if headers and isinstance(headers, dict):
            if self.headers:
                for key, value in self.headers.items():
                    if key in headers:
                        continue
                    headers[key] = value
        else:
            headers = self.headers
        return headers

    def _do_request(self, action, url, params=None, data=None, json=None, files=None, headers=None, **kwargs):
        headers = self._headers(headers)
        if action.upper() == "GET":
            return self.get(url, params=params, headers=headers, **kwargs)
        if action.upper() == "POST":
            return self.post(url, data=data, json=json, files=files, headers=headers, **kwargs)
        if action.upper() == "PUT":
            return self.put(url, data=data, json=json, files=files, headers=headers, **kwargs)
        if action.upper() == "DELETE":
            return self.delete(url, headers=headers, **kwargs)
        if action.upper() == "OPTIONS":
            return self.options(url, headers=headers, **kwargs)

    @staticmethod
    def get(url, params=None, headers=None, **kwargs):
        assert url, u"url不能为空."
        assert (not params or isinstance(params, dict)), u"params参数类型错误."
        return requests.get(url, params=params, headers=headers, **kwargs)

    @staticmethod
    def post(url, data=None, json=None, files=None, headers=None, **kwargs):
        assert url, u"url不能为空."
        assert (not data or isinstance(data, dict)), u"data参数类型错误."
        assert (not json or isinstance(json, dict)), u"json参数类型错误."
        assert (not files or isinstance(files, (list, tuple, dict))), u"files参数类型错误."
        return requests.post(url, data=data, json=json, files=files, headers=headers, **kwargs)

    @staticmethod
    def put(url, data=None, json=None, files=None, headers=None, **kwargs):
        assert url, u"url不能为空."
        assert (not data or isinstance(data, dict)), u"data参数类型错误."
        assert (not json or isinstance(json, dict)), u"json参数类型错误."
        assert (not files or isinstance(files, (list, tuple, dict))), u"files参数类型错误."
        return requests.put(url, data=data, json=json, files=files, headers=headers, **kwargs)

    @staticmethod
    def delete(url, headers=None, **kwargs):
        assert url, u"url不能为空."
        return requests.delete(url, headers=headers, **kwargs)

    @staticmethod
    def options(url, headers=None, **kwargs):
        assert url, u"url不能为空."
        return requests.options(url, headers=headers, **kwargs)
