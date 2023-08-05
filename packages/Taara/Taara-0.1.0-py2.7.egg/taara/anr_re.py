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

from taara.taara_teminal_color import print_exit, print_tips, print_key, print_header
from taara.anr_file import parse_header_info, parse_cmd_line, parse_thread_info_stack, GuessReason


def parse(anr_file_path):
    guess_reason = GuessReason()

    with open(anr_file_path, 'r') as anr_reader:
        is_first_line = True
        line = anr_reader.readline()

        while line != '':
            # get line
            if not is_first_line:
                line = anr_reader.readline()
            else:
                is_first_line = False

            # for header info
            head_info = parse_header_info(line)
            if head_info is not None:
                # print_header(head_info.to_string())
                guess_reason.process(head_info)
                continue

            # for cmd line
            cmd_line = parse_cmd_line(line)
            if cmd_line is not None:
                # print_tips(cmd_line.to_string())
                guess_reason.process(cmd_line)
                continue

            # for this cmd line thread info
            thread_info_stack = parse_thread_info_stack(line, anr_reader)
            if thread_info_stack is not None:
                guess_reason.process(thread_info_stack)
                # if thread_info_stack.is_main:
                #     print(thread_info_stack.to_string())
                continue

    guess_reason.guess()


def cause_hint(thread_info_stack):
    if not thread_info_stack.is_main:
        return
