# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Time access and conversions."""

from __go__.time import Now, Second, Seconds, Sleep  # pylint: disable=g-multiple-import


accept2dyear = 0 if not os.environ.get('PYTHONY2K') else 1
altzone = None
daylight = None
timezone = None
tzname = None


class struct_time(object):

    def __init__(self, seq):
        if len(seq) != 9:
            raise TypeError('{}.{}() takes a 9-sequence ({}-sequence given)'
                            ''.format(self.__class__.__module__,
                                      self.__class__.__name__, len(seq)))
        if isinstance(seq, Mapping):
            self.__dict__.update(seq)
        elif isinstance(seq, Iterable):
            (tm_year, tm_mon, tm_day, tm_hour, tm_min,
             tm_sec, tm_wday, tm_yday, tm_isdst) = map(int, seq)
            self.tm_year = tm_year
            self.tm_mon = tm_mon
            self.tm_day = tm_day
            self.tm_hour = tm_hour
            self.tm_min = tm_min
            self.tm_sec = tm_sec
            self.tm_wday = tm_wday
            self.tm_yday = tm_yday
            self.tm_isdst = tm_isdst
        else:
             raise TypeError('constructor requires a sequence')
        
    def __str__(self):
        s = ('{}(tm_year={tm_year}, tm_mon={tm_mon}, tm_mday={tm_day}, '
             'tm_hour={tm_hour}, tm_min={tm_min}, tm_sec={tm_sec}, '
             'tm_wday={tm_wday}, tm_yday={tm_yday}, tm_isdst={tm_isdst})'
             ''.format(self.__class__.__name__, **self.__dict__))
        return s


def asctime(t=None):
    return strftime(format="%a %b %d %H:%M:%S %Y", t)


def clock():
    return Seconds()


def ctime(secs=None):
    seconds = secs or Seconds()
    raise NotImplementedError


def gmtime(secs=None):
    raise NotImplementedError()


def localtime(secs=None):
    raise NotImplementedError()


def mktime(t):
    raise NotImplementedError()


def sleep(secs):
    Sleep(secs * Second)


def strftime(format, t=None):
    raise NotImplementedError()


def strptime(string, format="%a %b %d %H:%M:%S %Y"):
    raise NotImplementedError()


def time():
    return float(Now().UnixNano()) / Second


def tzset():
    raise NotImplementedError()
