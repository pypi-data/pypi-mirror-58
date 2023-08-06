#!/usr/bin/python -u

"""
Copyright (c) 2019 ByteDance Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import argparse

__author__ = 'JacksGong'
__version__ = '0.1.8'
__description__ = 'This tool is for analysis Android anr automatically'

import ntpath
from os import remove
from os.path import exists

from taara.anr_re import parse
from taara.retrace import retrace_to_temp
from taara.taara_teminal_color import print_exit, print_key
from taara.taara_utils import is_path, get_temp_file_path


def main():
    print("-------------------------------------------------------")
    print("                  Taara v" + __version__)
    print("")
    print("Thanks for using Taara! Now, the doc is available on: ")
    print_key("        https://code.byted.org/hproject/taara")
    print("")
    print("                   Have Fun!")
    print("-------------------------------------------------------")

    parser = argparse.ArgumentParser(description='Analysis Android ANR automatically')
    parser.add_argument('anr_file_path', nargs='*',
                        help='the file of /data/anr/traces.txt')
    parser.add_argument('-m', '--mapping_path', dest='mapping_path', help='the path of mapping to retrace')
    # parser.add_argument('-y', '--yml_file_name', dest='yml', help='Using yml file you config on ~/.taara folder')
    # parser.add_argument('-adb_logcat', '--adb_logcat_file_path', dest='yml', help='the path of adb logcat file')

    # support only print all lock chain
    # support only print all binder chain

    args = parser.parse_args()

    candidate_paths = args.anr_file_path
    if not candidate_paths:
        anr_file_path = None
    else:
        anr_file_path = candidate_paths[0]

    if not is_path(anr_file_path):
        print("")
        print_exit("Please provide anr file on the /data/anr/traces.txt")
        print("")
        print("-------------------------------------------------------")
        exit()

    mapping_path = args.mapping_path
    temp_file_path = None
    if mapping_path:
        if not is_path(mapping_path):
            print_exit("Provide mapping[%s] not valid!" % mapping_path)
            exit(-100)

        anr_file_name = ntpath.basename(anr_file_path)
        temp_file_path = get_temp_file_path(anr_file_name)
        result = retrace_to_temp(mapping_path, anr_file_path, temp_file_path)
        if result:
            anr_file_path = temp_file_path
        print "-------------------------------------------------------"

    parse(anr_file_path)

    if temp_file_path is not None and exists(temp_file_path):
        remove(temp_file_path)
