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
#  File Name : log_timedelta.py
#  Repo: https://github.com/LuomingXu/selfusepy

from datetime import datetime, timedelta, timezone

from enum import Enum

__all__ = ['LogTimeUTCOffset']


def _UTC_12(sec, what):
  return _delta_base(-12)


def _UTC_11(sec, what):
  return _delta_base(-11)


def _UTC_10(sec, what):
  return _delta_base(-10)


def _UTC_9(sec, what):
  return _delta_base(-9)


def _UTC_8(sec, what):
  return _delta_base(-8)


def _UTC_7(sec, what):
  return _delta_base(-7)


def _UTC_6(sec, what):
  return _delta_base(-6)


def _UTC_5(sec, what):
  return _delta_base(-5)


def _UTC_4(sec, what):
  return _delta_base(-4)


def _UTC_3(sec, what):
  return _delta_base(-3)


def _UTC_2(sec, what):
  return _delta_base(-2)


def _UTC_1(sec, what):
  return _delta_base(-1)


def _UTC(sec, what):
  return _delta_base(0)


def _UTC1(sec, what):
  return _delta_base(1)


def _UTC2(sec, what):
  return _delta_base(2)


def _UTC3(sec, what):
  return _delta_base(3)


def _UTC4(sec, what):
  return _delta_base(4)


def _UTC5(sec, what):
  return _delta_base(5)


def _UTC6(sec, what):
  return _delta_base(6)


def _UTC7(sec, what):
  return _delta_base(7)


def _UTC8(sec, what):
  return _delta_base(8)


def _UTC9(sec, what):
  return _delta_base(9)


def _UTC10(sec, what):
  return _delta_base(10)


def _UTC11(sec, what):
  return _delta_base(11)


def _UTC12(sec, what):
  return _delta_base(12)


def _delta_base(delta: int):
  return datetime.now(timezone(timedelta(hours = delta))).timetuple()


class LogTimeUTCOffset(Enum):
  UTC_12 = _UTC_12
  UTC_11 = _UTC_11
  UTC_10 = _UTC_10
  UTC_9 = _UTC_9
  UTC_8 = _UTC_8
  UTC_7 = _UTC_7
  UTC_6 = _UTC_6
  UTC_5 = _UTC_5
  UTC_4 = _UTC_4
  UTC_3 = _UTC_3
  UTC_2 = _UTC_2
  UTC_1 = _UTC_1
  UTC = _UTC
  UTC1 = _UTC1
  UTC2 = _UTC2
  UTC3 = _UTC3
  UTC4 = _UTC4
  UTC5 = _UTC5
  UTC6 = _UTC6
  UTC7 = _UTC7
  UTC8 = _UTC8
  UTC9 = _UTC9
  UTC10 = _UTC10
  UTC11 = _UTC11
  UTC12 = _UTC12
