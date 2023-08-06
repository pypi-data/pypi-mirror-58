# -*- coding: utf-8 -*-
"""
Created By Murray(m18527) on 2019/12/13 13:57
"""
from __future__ import absolute_import, unicode_literals

import json
from collections import namedtuple

import requests

from stormer.utils.constants import UNKNOWN_ERROR, MSG, GONE_AWAY

Resp = namedtuple("Resp", ["status_code", "code", "data", "msg"])

META_CACHE_KEY = "STORMER:REQUESTER:META:{PARAMS_HASH}"
CONTENT_CACHE_KEY = "STORMER:REQUESTER:CONTENT:{PARAMS_HASH}"


class RespResult(object):
    """
    Used for packing request response
    """

    def __init__(self, resp=None, url=None, action=None, params_hash=None, redis_conn=None):
        if resp and not isinstance(resp, requests.Response):
            raise Exception("Param<resp> should be object of requests.Response, but {} found.".format(type(resp)))
        self.resp = resp
        self.status = None
        self.reason = None
        self.content = None
        self.headers = None
        self.encoding = None
        self.status_code = None
        self.req_url = url
        self.req_action = action
        self.params_hash = params_hash
        self.redis_conn = redis_conn
        self._init()

    def _init(self):
        if not self.resp:
            return
        self.status = self.resp.ok
        self.reason = self.resp.reason
        self.content = self.resp.content
        self.headers = self.resp.headers.__repr__()
        self.encoding = self.resp.encoding
        self.status_code = self.resp.status_code

    @property
    def bytes(self):
        return self.content

    @property
    def text(self):
        return self.resp.text

    @property
    def json(self):
        return self.resp.json

    @property
    def json_resp(self):
        """parse resp to api resp"""
        if not self.resp:
            return Resp(status_code=400, code=UNKNOWN_ERROR, data=None, msg=MSG[UNKNOWN_ERROR])
        if 200 <= self.status_code < 300:
            code = (self.json or {}).get("code", GONE_AWAY)
            if code:
                return Resp(status_code=self.status_code, code=code, data=None, msg=(self.json or {}).get("message"))
            return Resp(status_code=self.status_code, code=code, data=self.json, msg=MSG.get(code))
        if isinstance(self.reason, bytes):
            try:
                reason = self.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = self.reason.decode('iso-8859-1')
        else:
            reason = self.reason
        return Resp(status_code=self.status_code, code=UNKNOWN_ERROR, data=None, msg=reason)

    def set_cache(self, timeout):
        if not (self.redis_conn and timeout and self.params_hash) \
                or not (self.req_action and self.req_action.upper() == "GET"):
            return None
        meta_data = {
            "status": self.status,
            "reason": self.reason,
            "headers": self.headers,
            "encoding": self.encoding,
            "status_code": self.status_code,
            "req_url": self.req_url,
            "req_action": self.req_action,
        }
        meta_key = META_CACHE_KEY.format(PARAMS_HASH=self.params_hash)
        content_key = CONTENT_CACHE_KEY.format(PARAMS_HASH=self.params_hash)
        self.redis_conn.set(meta_key, json.dumps(meta_data), ex=timeout)
        self.redis_conn.set(content_key, self.content, ex=timeout)

    @classmethod
    def from_cache(cls, params_hash, action, redis_conn):
        if not (redis_conn and action and action.upper() == "GET"):
            return None
        meta_key = META_CACHE_KEY.format(PARAMS_HASH=params_hash)
        content_key = CONTENT_CACHE_KEY.format(PARAMS_HASH=params_hash)
        meta_data = redis_conn.get(meta_key)
        content = redis_conn.get(content_key)
        if not (meta_data and content):
            return None
        result = cls()
        for key, value in json.loads(meta_data).items():
            setattr(result, key, value)
        setattr(result, "content", content)
        return result
