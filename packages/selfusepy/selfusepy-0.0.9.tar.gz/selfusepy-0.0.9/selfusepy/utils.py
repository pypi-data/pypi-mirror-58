#   Copyright 2018-2019 LuomingXu
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Author : Luoming Xu
#  File Name : utils.py
#  Repo: https://github.com/LuomingXu/selfusepy

import logging
import os
import sys
from logging import handlers
from typing import MutableMapping, List

from log_timedelta import LogTimeUTCOffset


def eprint(*args, sep = ' ', end = '\n', file = sys.stderr):
  """
  collect from: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
  """
  print(*args, sep = sep, end = end, file = file)


def override_str(clazz):
  """
  override default func __str__(), print Object like Java toString() style
  """

  def __str__(self):
    values: MutableMapping = {}
    for k, v in vars(self).items():
      if isinstance(v, list):
        values[k] = '[%s]' % ', '.join('%s' % item.__str__() for item in v)
      else:
        values[k] = v.__str__()

    return '%s(%s)' % (
      type(self).__name__,  # class name
      ', '.join('%s: %s' % item for item in values.items())
    )

  clazz.__str__ = __str__
  return clazz


class ShowProcess(object):
  """
  显示处理进度的类
  调用该类相关函数即可实现处理进度的显示
  # 效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
  """

  i = 0  # 当前的处理进度
  max_steps = 0  # 总共需要处理的次数
  max_arrow = 50  # 进度条的长度
  infoDone = 'done'

  def __init__(self, max_steps, infoDone = 'Done'):
    """
    初始化函数，需要知道总共的处理次数
    :param max_steps: 总共需要处理的次数
    :param infoDone: 结束时打印的字符
    """
    self.max_steps = max_steps
    self.i = 0
    self.infoDone = infoDone

  def show_process(self, i = None):
    """
    显示函数，根据当前的处理进度i显示进度
    :param i: 当前进度
    """
    if i is not None:
      self.i = i
    else:
      self.i += 1
    num_arrow = int(self.i * self.max_arrow / self.max_steps)  # 计算显示多少个'>'
    num_line = self.max_arrow - num_arrow  # 计算显示多少个'-'
    percent = self.i * 100.0 / self.max_steps  # 计算完成进度，格式为xx.xx%
    process_bar = '[' + '>' * num_arrow + '-' * num_line + ']' \
                  + '%.2f' % percent + '%' + '\r'  # 带输出的字符串，'\r'表示不换行回到最左边
    sys.stdout.write(process_bar)  # 这两句打印字符到终端
    sys.stdout.flush()
    if self.i >= self.max_steps:
      self.close()

  def close(self):
    print('')
    print(self.infoDone)
    self.i = 0


class Logger(object):
  """
  日志类
  usage: log = Logger('error.log').logger OR log = Logger().logger
         log.info('info')
  """

  def __init__(self, filename = None, time_offset: LogTimeUTCOffset = LogTimeUTCOffset.UTC8, when = 'D', backCount = 3,
               fmt = '%(asctime)s-[%(levelname)8s]-[%(threadName)15s] %(customPathname)50s(%(lineno)d): %(message)s'):
    """
    init
    :param filename: 储存日志的文件, 为None的话就是不储存日志到文件
    :param when: 间隔的时间单位. S秒, M分, H小时, D天, W每星期(interval==0时代表星期一) midnight 每天凌晨
    :param backCount: 备份文件的个数, 如果超过这个个数, 就会自动删除
    :param time_offset: log的时间, 默认为UTC+8
    :param fmt: 日志格式
    """
    logging.Formatter.converter = time_offset
    self.logger = logging.Logger(filename)
    format_str = logging.Formatter(fmt)
    self.logger.setLevel(logging.DEBUG)  # 设置日志级别为debug, 所有的log都可以打印出来
    sh = logging.StreamHandler()  # 控制台输出
    sh.setFormatter(format_str)
    self.logger.addHandler(sh)
    self.logger.addFilter(LoggerFilter())

    if filename is not None:
      """实例化TimedRotatingFileHandler"""
      th = handlers.TimedRotatingFileHandler(filename = filename, when = when, backupCount = backCount,
                                             encoding = 'utf-8')
      th.setFormatter(format_str)  # 设置文件里写入的格式
      self.logger.addHandler(th)


def upper_first_letter(s: str) -> str:
  """
  make first letter upper case
  :param s:
  :return:
  """
  return s[0].capitalize() + s[1:]


class LoggerFilter(logging.Filter):

  def _s_len(self, l: List[str]):
    len: int = 0
    for item in l:
      len += item.__len__() + 1
    return len

  def _replace_underline(self, l: List[str]):
    for i, item in enumerate(l):
      l[i] = item.replace('_', '')

  def filter(self, record: logging.LogRecord):
    s = str(record.pathname).replace('\\', '/').replace(RootPath().root_path, '').replace('/', '.')[1:]
    l: List[str] = s.split('.')
    l.pop(l.__len__() - 1)  # 丢弃最后的文件扩展名'py'
    file_name = l.pop(l.__len__() - 1)
    self._replace_underline(l)  # 有些py文件以'_'开头, 需要删去, 才能取首字母
    i: int = 0
    while self._s_len(l) + file_name.__len__() + record.funcName.__len__() > 50:  # 如果超出了长度再进行缩减操作
      if i >= l.__len__():  # 实在太长了缩减不了, 就算了, 需要保证最后的文件名与函数名的完整
        break
      l[i] = l[i][0]
      i += 1

    l.append(file_name)
    l.append(record.funcName)

    record.customPathname = '.'.join('%s' % item for item in l)
    """
    不能在这边直接就修改
    >>>record.pathname = '.'.join('%s' % item for item in l)
    有可能后面的log依赖这个pathname, 那么这个pathname就被修改了, 
    而没有被系统重新赋予正确的pathname
    例如test.log包中的多层级__init__, 就会出现这种问题
    """
    return True


class RootPath(object):
  """获取根目录"""
  root_path = None

  def __init__(self):
    if RootPath.root_path == None:
      # 判断调试模式
      debug_vars = dict((a, b) for a, b in os.environ.items()
                        if a.find('IPYTHONENABLE') >= 0)

      # 根据不同场景获取根目录
      if len(debug_vars) > 0:
        """当前为debug运行时"""
        RootPath.root_path = sys.path[2]
      elif getattr(sys, 'frozen', False):
        """当前为exe运行时"""
        RootPath.root_path = os.getcwd()
      else:
        """正常执行"""
        RootPath.root_path = sys.path[1]

      # 替换斜杠
      RootPath.root_path = RootPath.root_path.replace('\\', '/')


def lookahead(iterable):
  """
  Pass through all values from the given iterable, augmented by the
  information if there are more values to come after the current one
  (True), or if it is the last value (False).
  collect from: https://stackoverflow.com/a/1630350
  >>>from selfusepy.utils import lookahead
  >>>from typing import List
  >>>c: List[int] = list()
  >>>for item, has_next in lookahead(c):
  >>>  if not has_next:
  >>>    # do something for last item
  >>>  # other item
  """
  # Get an iterator and pull the first value.
  it = iter(iterable)
  last = next(it)
  # Run the iterator to exhaustion (starting from the second value).
  for val in it:
    # Report the *previous* value (more to come).
    yield last, True
    last = val
  # Report the last value.
  yield last, False
