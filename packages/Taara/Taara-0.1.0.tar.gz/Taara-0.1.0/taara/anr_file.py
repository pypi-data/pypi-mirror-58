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
from taara.anr_stack import is_java_layer_stack_line, is_kernal_stack_line, is_aosp_code_stack_line, parse_native_stack, \
    BinderStackHelper
from taara.anr_state import get_readable_state, get_readable_state_for_detail, is_sleep, is_native
from taara.taara_teminal_color import print_exit, print_tips, print_key, print_header

ANR_HEAD_INFO = re.compile(r' *----- *pid (\d*) at (\d*)-(\d*)-(\d*) (\d*):(\d*):(\d*)')
KNOWN_PACKAGE = 'com.kongming'


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
    pid = 0
    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0
    second = 0

    def __init__(self):
        pass

    def to_string(self):
        return 'pid[%s] [%s-%s-%s] %s:%s:%s' % (
            self.pid, self.year, self.month, self.day, self.hour, self.minute, self.second)

    def get_time_string(self):
        return '%s-%s-%s %s:%s:%s' % (
            self.year, self.month, self.day, self.hour, self.minute, self.second)


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
        pass

    cmd_line = ''

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
    is_main = False
    tid = 0
    priority = 0
    thread_name = ''
    state = ''
    info = ''
    stack = ''
    stack_tree = None

    def __init__(self):
        pass

    def to_string(self):
        return "线程名[%s] TID[%s]\n%s%s" % (self.thread_name, self.tid, self.info, self.stack)


class ProcessAllData:
    head = HeadInfo()
    cmd_line = CMDLine()
    thread_info_stacks = []

    def __init__(self):
        pass

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


class GuessReason:
    core_reason = 'unknown'
    top_head_info = None
    ref_process_data = {}
    binder_stack_helper = BinderStackHelper()

    def __init__(self):
        self.tmp_head = HeadInfo()
        self.tmp_cmd = CMDLine()
        self.is_first_thread = True
        pass

    def process(self, info):

        if isinstance(info, HeadInfo):
            self.tmp_head = info
        elif isinstance(info, ThreadInfoStack):
            ref_cause = False
            # 顶部主线程
            is_top_main_process = False
            if self.is_first_thread:
                # this is main cause for anr
                ref_cause = True
                is_top_main_process = info.is_main
                self.is_first_thread = False

            ref_cause = self.binder_stack_helper.process(info.stack_tree, is_top_main_process) or ref_cause

            if ref_cause:
                # 得到顶部HeadInfo
                if self.top_head_info is None:
                    self.top_head_info = self.tmp_head

                # 收集所有数据到process_all_data
                if self.tmp_head in self.ref_process_data:
                    process_all_data = self.ref_process_data[self.tmp_head]
                else:
                    process_all_data = ProcessAllData()
                    self.ref_process_data[self.tmp_head] = process_all_data
                process_all_data.head = self.tmp_head
                process_all_data.cmd_line = self.tmp_cmd
                process_all_data.thread_info_stacks.append(info)

                # 收集binder调用对端所有信息
                self.binder_stack_helper.process_process_all_data(process_all_data)

        elif isinstance(info, CMDLine):
            self.tmp_cmd = info

    def guess(self):
        basic_cause = ""
        detail_cause = ""
        ref_thread_stacks = []

        for head_info in self.ref_process_data:
            process_data = self.ref_process_data[head_info]
            if head_info == self.top_head_info:
                basic_cause, detail_cause = self.guess_top_process(process_data, basic_cause, detail_cause,
                                                                   ref_thread_stacks)
            else:
                cmd_line = process_data.cmd_line
                for thread_info_stack in process_data.thread_info_stacks:
                    ref_thread_stacks.append(self.assemble_ref_thread_stacks(cmd_line, thread_info_stack))

        print_header("------> 基本原因: ")
        print basic_cause

        print_header("------> 基本描述: ")
        print detail_cause

        if len(ref_thread_stacks) > 0:
            print_header("------> 相关堆栈: ")
            for stack in ref_thread_stacks:
                print stack

    def guess_top_process(self, top_process_data, basic_cause, detail_cause, ref_thread_stacks):
        top_main_thread = None
        for thread_info_stack in top_process_data.thread_info_stacks:
            if thread_info_stack.is_main:
                top_main_thread = thread_info_stack
                break

        cmd_line = top_process_data.cmd_line

        print "                  Taara ANR原因猜想"

        if self.binder_stack_helper.is_binder_invoke:
            basic_cause += "栈顶Binder调用: %s#%s\n" % \
                           (self.binder_stack_helper.interface_name, self.binder_stack_helper.method_name)
            basic_cause = self.binder_stack_helper.guess_service_invoke_detail(basic_cause)
            basic_cause += "\n"

        if top_main_thread is None:
            basic_cause = "未知"
            detail_cause = "主线程堆栈未找到"
        else:
            basic_cause, detail_cause = self.guess_top_main_thread(top_main_thread, cmd_line, basic_cause, detail_cause,
                                                                   ref_thread_stacks)
        if self.top_head_info is None:
            detail_cause += "发生时间: 未知\n"
        else:
            detail_cause += "发生时间: %s\n" % self.top_head_info.get_time_string()

        detail_cause += "包/指令: %s\n" % cmd_line.to_string()
        return basic_cause, detail_cause

    def guess_top_main_thread(self, top_main_thread, top_cmd_line, basic_cause, detail_cause, ref_thread_stacks):
        # state
        state = top_main_thread.state.upper()
        ref_thread_stacks.append(self.assemble_ref_thread_stacks(top_cmd_line, top_main_thread))

        detail_cause += ("主线状态(%s): %s\n" % (state, get_readable_state(state)))

        stack_tree = top_main_thread.stack_tree
        top_stack = stack_tree[0]
        if top_stack.__contains__(KNOWN_PACKAGE):
            basic_cause += ("栈顶在应用(%s) %s\n" % (top_stack.strip(), get_readable_state_for_detail(state)))
        elif is_sleep(top_stack, state):
            basic_cause += ("%s 调用了sleep没有唤醒导致\n", top_stack)
        elif is_native(state):
            basic_cause = parse_native_stack(basic_cause, stack_tree)

        return basic_cause, detail_cause

    def assemble_ref_thread_stacks(self, cmd_line, thread_info_stack):
        ref_thread_stack = "所在进程[%s]: %s\n" % (self.top_head_info.pid, cmd_line.to_string())
        ref_thread_stack += thread_info_stack.to_string()
        return ref_thread_stack
