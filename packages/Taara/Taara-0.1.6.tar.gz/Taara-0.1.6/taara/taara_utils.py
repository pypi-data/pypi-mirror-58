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
from os import environ, mkdir
from os.path import exists

__author__ = 'JacksGong'

NO_HOME_PATH = re.compile(r'~/(.*)')
HOME_PATH = environ['HOME']
ANDROID_HOME_ENV_NAME = 'ANDROID_HOME'
TEMP_HOME_PATH = HOME_PATH + "/" + ".taara"
RETRACE_SH_FROM_ANDROID_HOME = "/tools/proguard/bin/retrace.sh"


def is_android_home_env_valid():
    return environ.get(ANDROID_HOME_ENV_NAME) is not None


def get_retrace_sh_path():
    return environ[ANDROID_HOME_ENV_NAME] + RETRACE_SH_FROM_ANDROID_HOME


# get the home case path
def handle_home_case(path):
    path = path.strip()
    if path.startswith('~/'):
        path = HOME_PATH + '/' + NO_HOME_PATH.match(path).groups()[0]
    return path


def get_temp_file_path(base_file_name):
    if not exists(TEMP_HOME_PATH):
        mkdir(TEMP_HOME_PATH)
    return TEMP_HOME_PATH + "/" + base_file_name + ".tmp"


def is_path(path):
    if not path:
        return False

    if path.startswith('/') or path.startswith('~/') or path.startswith('./'):
        return True

    if exists(path):
        return True
    return False
