# coding=utf-8
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

# ----- pid 9507 at 2019-11-25 22:14:03 -----

ANR_HEAD_INFO = re.compile(r' *----- *pid (\d*) at (\d*)-(\d*)-(\d*) (\d*):(\d*):(\d*)')


def parse_header_info(line):
    head_info_matcher = ANR_HEAD_INFO.match(line)
    if head_info_matcher is not None:
        head_info_group = head_info_matcher.groups()

        head_info = HeadInfo()
        head_info.pid = head_info_group[0]
        head_info.year = head_info_group[1]
        head_info.month = head_info_group[2]
        head_info.day = head_info_group[3]
        head_info.hour = head_info_group[4]
        head_info.minute = head_info_group[5]
        head_info.second = head_info_group[6]
        return head_info
    return None


class HeadInfo:
    def __init__(self):
        self.pid = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        pass

    def to_string(self):
        return 'pid[%s] [%s-%s-%s] %s:%s:%s' % (
            self.pid, self.year, self.month, self.day, self.hour, self.minute, self.second)

    def get_time_string(self):
        return '%s-%s-%s %s:%s:%s' % (
            self.year, self.month, self.day, self.hour, self.minute, self.second)

    def is_empty(self):
        return self.pid == 0 and self.year == 0


# Cmd line: com.bytedance.h.a
CMD_LINE = re.compile(r'Cmd line: (.*)')


def parse_cmd_line(line):
    cmd_line_matcher = CMD_LINE.match(line)
    if cmd_line_matcher is not None:
        cmd_line = CMDLine()
        cmd_line.cmd_line = cmd_line_matcher.groups()[0]
        return cmd_line
    return None


class CMDLine:
    def __init__(self):
        self.cmd_line = '<当前>'

    def to_string(self):
        return self.cmd_line


# "main" prio=5 tid=1 Native
THREAD_HEAD = re.compile(r'"([^"]*)" prio=(\d*) tid=(\d*) (\S*)')


def parse_thread_info_stack(line, anr_reader):
    thread_header_matcher = THREAD_HEAD.match(line)

    if thread_header_matcher is not None:
        thread_info_stack = ThreadInfoStack()
        thread_header_group = thread_header_matcher.groups()

        thread_info_stack.thread_name = thread_header_group[0]
        thread_info_stack.priority = thread_header_group[1]
        thread_info_stack.tid = thread_header_group[2]
        thread_info_stack.state = thread_header_group[3]
        thread_info_stack.is_main = thread_info_stack.thread_name.__eq__('main')

        line = anr_reader.readline()
        while line != '\n':
            if line.__contains__(' | '):
                # info
                thread_info_stack.info += line
            else:
                thread_info_stack.stack += line
            line = anr_reader.readline()
        thread_info_stack.stack_tree = thread_info_stack.stack.splitlines()
        return thread_info_stack

    return None


class ThreadInfoStack:
    # native/runnable/wait

    def __init__(self):
        self.is_main = False
        self.tid = 0
        self.priority = 0
        self.thread_name = ''
        self.state = ''
        self.info = ''
        self.stack = ''
        self.stack_tree = None

    def to_string(self):
        return "线程名[%s] TID[%s]\n%s%s" % (self.thread_name, self.tid, self.info, self.stack)


class ProcessAllData:

    def __init__(self):
        self.head = HeadInfo()
        self.cmd_line = CMDLine()
        self.thread_info_stacks = []

    def to_string(self):
        thread_info_string = ''
        for info in self.thread_info_stacks:
            thread_info_string += info.to_string() + "\n"
        return self.head.to_string() + self.cmd_line.to_string() + thread_info_string

    def is_stack_belong(self, stack_tree):
        for info_stacks in self.thread_info_stacks:
            if stack_tree == info_stacks.stack_tree:
                return True
        return False
