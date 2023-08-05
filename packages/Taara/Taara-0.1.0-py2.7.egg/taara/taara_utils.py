#  Copyright (c) 2019 ByteDance Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import re
from os import environ
from os.path import exists

__author__ = 'JacksGong'

NO_HOME_PATH = re.compile(r'~/(.*)')
HOME_PATH = environ['HOME']


# get the home case path
def handle_home_case(path):
    path = path.strip()
    if path.startswith('~/'):
        path = HOME_PATH + '/' + NO_HOME_PATH.match(path).groups()[0]
    return path


def is_path(path):
    if not path:
        return False

    if path.startswith('/') or path.startswith('~/') or path.startswith('./'):
        return True

    if exists(path):
        return True
    return False
