#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
import json
import logging
import time

import asyncio
from tortoise import models

from common.logger import http_logger, mysql_logger, root_logger


def async_timeout_deco_commonon_for_instance_method(
        time_interval=500, middleware_type_name='', logger: logging.Logger = mysql_logger,
        other_msg='', max_record_nums=0
):  # noqa
    """
    通用的超时装饰器，需要装饰在async实例方法上,类需要重写__str__。以便获得对象的有用的一些如连接得有用信息，如host  db。千万别把这加到非async的方法或函数上面。
    :param time_interval: 超时的时间
    :param middleware_type_name: 中间件的种类，例如是es mysql kafka什么的。
    :param logger : 日志，用什么命名空间的日志来记录日志，不同功能的中间件写入不同日志.记住这个参数千万要传具体的logger，不要传根命名空间的日志，也不要用默认参数。
    :param other_msg:
    :param max_record_nums 结果得最大条数，防止查询出十几万条来计算消耗大量cpu不知情。
    :return:
    """

    def _inner(func):
        @wraps(func)
        async def __inner(self, *args, **kwargs):
            args_str = str(args)[:500] + '.....'
            kwargs_str = str(kwargs)[:500] + '.....'
            start_time = time.time() * 1000
            ret = func(self, *args, **kwargs)
            if asyncio.iscoroutine(ret):  # 异步结果是协程，不是最终结果。
                ret = await ret
            end_time = time.time() * 1000
            cost_time = int(end_time - start_time)
            msg = {
                'middware_type': middleware_type_name,
                'function_args': ' '.join(args_str.replace(r'\n', '').split()),
                'function_kwargs': kwargs_str,
                'cost_time': cost_time,
                'specify_time_interval': time_interval,
                'specify_max_record_nums': max_record_nums,
                'other_msg': other_msg,
                'result_length': len(ret) if hasattr(ret, '__len__') and not isinstance(ret, str) else 0
            }
            if cost_time > time_interval:
                logger.warning('{}.{} timeout: {}'.format(str(self), func.__name__, json.dumps(msg)))

            return ret

        return __inner

    return _inner


def api_log_wrapper(timeout=5000, callback=None):
    """外部接口调用记录"""
    def __inner(func):
        @wraps(func)
        async def wrap(*args, **kwargs):
            start = time.time()
            url, params, header, resp = await func(*args, **kwargs)
            if callback and await callback(args[0],url, params, header, resp):
                url, params, header, resp = await func(*args, **kwargs)
            cost_time = (time.time() - start) * 1000
            if isinstance(resp, dict):
                status = resp.get('code') or resp.get('status')
                error = resp.get('error')
                if (status is not None and int(status) != 200) or error:
                    extra_info = {"url": url, "req_params": params, "header": header, 'resp': resp}
                    extra_info = json.dumps(extra_info, ensure_ascii=False)
                    # http_logger.error("{}.{} failed: {}".format(func.__module__, func.__name__, extra_info))
                if cost_time > timeout:
                    extra_info = {"url": url, "req_params": params, "header": header, 'cost_time': cost_time}
                    extra_info = json.dumps(extra_info, ensure_ascii=False)
                    # http_logger.warn("{}.{} timeout: {}".format(func.__module__, func.__name__, extra_info))
            extra_info = {"url": url, "req_params": params, "header": header, 'cost_time': cost_time}
            # http_logger.info(f"{extra_info}")
            # http_logger.info(f"{resp}")
            return resp

        return wrap

    return __inner


def method_timeout_wrapper(timeout=5000):
    """函数/方法超时记录"""

    def __inner(func):
        @wraps(func)
        async def wrap(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            if asyncio.iscoroutine(ret):
                ret = await ret
            cost_time = (time.time() - start) * 1000
            if cost_time >= timeout:
                extra_info = {"cost_time": cost_time}
                root_logger.warn("{}.{} timeout: {}".format(func.__module__, func.__name__, json.dumps(extra_info)))
            return ret

        return wrap

    return __inner


def orm_timeout_wrapper(timeout=1000):
    """tortoise-orm超时记录"""

    def _inner(func):
        @wraps(func)
        async def wrap(cls, *args, **kwargs):
            start = time.time()
            payload = await func(cls, *args, **kwargs)
            cost_time = (time.time() - start) * 1000
            if cost_time > timeout:
                extra_args = [i.filters if isinstance(i, models.Q) else i for i in args]
                extra_info = {'cost_time': cost_time, 'args': str(extra_args), 'kwargs': kwargs}
                extra_info = json.dumps(extra_info, ensure_ascii=False)
                mysql_logger.warn('orm {}.{} timeout: {}'.format(cls.__name__, func.__name__, extra_info))
            return payload

        return wrap

    return _inner
