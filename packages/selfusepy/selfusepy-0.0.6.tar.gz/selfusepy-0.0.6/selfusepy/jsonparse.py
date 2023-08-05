#  The Apache License Version 2.0
#  Copyright (c) 2019
#  Author : Luoming Xu
#  Project Name : selfusepy
#  File Name : jsonparse.py
#  CreateTime: 2019/11/26 20:45

"""
用来Json to Object的工具库,
可直接在__init__直接调用此工具库的实现
来直接使用
"""
import json
from typing import List

from selfusepy.utils import upper_first_letter

class_dict = {}

__classname__: str = '__classname__'


class BaseJsonObject(object):
  """
  用于在用户自定义Json的转化目标类的基类
  以是否为此基类的子类来判断这个类是否需要转化
  """
  pass


def deserialize_object(d: dict) -> object:
  """
  用于json.loads()函数中的object_hook参数
  :param d: json转化过程中的字典
  :return: object
  """
  cls = d.pop(__classname__, None)
  if cls:
    cls = class_dict[cls]
    obj = cls.__new__(cls)  # Make instance without calling __init__
    for key, value in d.items():
      setattr(obj, key, value)
    return obj
  else:
    return d


def add_classname(d: dict, classname: str) -> str:
  """
  给json字符串添加一个"__classname__"的key来作为转化的标志
  :param d: json的字典
  :param classname: 转化的目标类
  :return: 修改完后的json字符串
  """
  d[__classname__] = classname
  for k, v in d.items():
    if isinstance(v, dict):
      add_classname(v, upper_first_letter(k))
    elif isinstance(v, List):
      for item in v:
        add_classname(item, upper_first_letter(k))

  return json.dumps(d)  # 需要替换默认dict导出的str为单引号的问题


def generate_class_dict(obj: BaseJsonObject):
  """
  构造需要转化的目标类的所包含的所有类
  将key: 类名, value: class存入class_dict中
  :param obj: 目标类
  """
  cls = type(obj)
  class_dict[cls.__name__] = cls
  for item in vars(obj).values():
    cls = type(item)
    if issubclass(cls, BaseJsonObject):
      generate_class_dict(cls())
    elif issubclass(cls, List):
      cls = type(item.pop(0))
      if issubclass(cls, BaseJsonObject):
        generate_class_dict(cls())
