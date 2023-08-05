#  The Apache License Version 2.0
#  Copyright (c) 2019
#  Author : Luoming Xu
#  Project Name : selfusepy
#  File Name : url.py
#  CreateTime: 2019/11/26 20:45

import json
from urllib.parse import urlencode

import urllib3
from urllib3.response import HTTPResponse


class HttpError(Exception):
  def __init__(self, msg):
    super().__init__(self)
    self.msg = msg

  def __str__(self) -> str:
    return self.msg


class Request(object):
  """
  进一步封装urllib3的接口, 直接提供GET, POST, PUT, DELETE接口, body全部使用json格式
  """

  def __init__(self):
    self.http = urllib3.PoolManager()
    self.UTF8 = 'utf-8'

  def get(self, url: str, head: dict = None, **params: dict) -> HTTPResponse:
    """
    http GET method
    :param head: request header
    :param url: URL
    :param params: http request params. should be class's dict. e.g., url.Request.get('https://example.com', **object.__dict__)
                   if your define a dict variable, you just use it like, url.Request.get('https://example.com', **dict)
    :return:
    """
    if params is not None:
      return self.http.request('GET', url, headers = head,
                               fields = params)
    else:
      return self.http.request('GET', url, headers = head)

  def put(self, url: str, body: object = None, head: dict = None, **params: dict) -> HTTPResponse:
    """
    http PUT method
    :param head: request header
    :param url: URL
    :param body: put body. one object
    :param params: http request params
    :return:
    """
    head['Content-Type'] = 'application/json'
    if params is not None:
      url += '?' + urlencode(params)
    if body is not None:
      return self.http.request('PUT', url, body = json.dumps(body.__dict__),
                               headers = head)
    else:
      return self.http.request('PUT', url, headers = head)

  def post(self, url: str, body: object, head: dict = None, **params: dict) -> HTTPResponse:
    """
    http POST method
    :param head: request header
    :param url: URL
    :param body: post body. one object
    :param params: http request params
    :return:
    """
    head['Content-Type'] = 'application/json'
    if body is None:
      raise HttpError('POST request\'s body can not be None')
    if params is not None:
      url += '?' + urlencode(params)

    return self.http.request('POST', url, body = json.dumps(body.__dict__),
                             headers = head)

  def delete(self, url: str, head: dict, **params: dict) -> HTTPResponse:
    """
    http DELETE method
    :param head: request header
    :param url: URL
    :param params: http request params
    :return:
    """
    if params is not None:
      return self.http.request('DELETE', url, fields = params, headers = head)
    else:
      return self.http.request('DELETE', url, headers = head)
