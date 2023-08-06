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
from taara.anr_state import get_readable_state, get_readable_state_for_detail, is_sleep, is_native
from taara.stack.anr_stack import is_java_layer_stack_line, is_aosp_code_stack_line, parse_native_stack
from taara.taara_teminal_color import print_header, colorize, YELLOW


class GuessReason:
    def __init__(self, anrChain):
        self.anrChain = anrChain
        pass

    def guess(self):
        ref_process_data = self.anrChain.ref_cause_process_data_map
        top_head_info = self.anrChain.top_head_info

        basic_cause = ""
        detail_cause = ""
        ref_thread_stacks = []

        pre_pid = None
        for head_info in ref_process_data:
            process_data = ref_process_data[head_info]
            cur_pid = head_info.pid
            if head_info == top_head_info:
                # 发生问题的进程
                basic_cause, detail_cause = self.guess_top_process(process_data, basic_cause, detail_cause,
                                                                   ref_thread_stacks)
            else:
                cmd_line = process_data.cmd_line
                for thread_info_stack in process_data.thread_info_stacks:
                    ref_thread_stacks.append(
                        self.assemble_ref_thread_stacks(pre_pid, cur_pid, cmd_line, thread_info_stack))
            pre_pid = cur_pid

        lock_obj_handler = self.anrChain.lock_obj_handler
        basic_cause = lock_obj_handler.guess_lock_cause(top_head_info, basic_cause)

        print_header("------> 基本原因: ")
        print basic_cause

        print_header("------> 基本描述: ")
        print detail_cause

        if len(ref_thread_stacks) > 0:
            print_header("------> 相关堆栈: ")
            for stack in ref_thread_stacks:
                print stack

    def guess_top_process(self, top_process_data, basic_cause, detail_cause, ref_thread_stacks):
        binder_stack_handler = self.anrChain.binder_stack_handler
        top_head_info = self.anrChain.top_head_info

        top_main_thread = None
        for thread_info_stack in top_process_data.thread_info_stacks:
            if thread_info_stack.is_main:
                top_main_thread = thread_info_stack
                break

        cmd_line = top_process_data.cmd_line

        print "                  Taara ANR原因猜想"

        if binder_stack_handler.is_binder_invoke:
            basic_cause += "栈顶Binder调用: %s#%s\n" % \
                           (binder_stack_handler.interface_name, binder_stack_handler.method_name)
            basic_cause = binder_stack_handler.guess_service_invoke_detail(basic_cause)
            basic_cause += "\n"

        if top_main_thread is None:
            basic_cause = "未知"
            detail_cause = "主线程堆栈未找到"
        else:
            basic_cause, detail_cause = self.guess_top_main_thread(top_head_info.pid, top_main_thread,
                                                                   top_process_data.thread_info_stacks, cmd_line,
                                                                   basic_cause, detail_cause,
                                                                   ref_thread_stacks)
        if top_head_info is None:
            detail_cause += "发生时间: 未知\n"
        else:
            detail_cause += "发生时间: %s\n" % top_head_info.get_time_string()

        detail_cause += "包/指令: %s\n" % cmd_line.to_string()
        return basic_cause, detail_cause

    def guess_top_main_thread(self, pid, top_main_thread, thread_stacks, top_cmd_line, basic_cause, detail_cause,
                              ref_thread_stacks):
        # state
        state = top_main_thread.state.upper()
        pre_pid = -1
        for thread_info_stack in thread_stacks:
            ref_thread_stacks.append(self.assemble_ref_thread_stacks(pre_pid, pid, top_cmd_line, thread_info_stack))
            pre_pid = pid

        detail_cause += ("主线状态(%s): %s\n" % (state, get_readable_state(state)))

        stack_tree = top_main_thread.stack_tree
        top_stack = stack_tree[0]
        if is_java_layer_stack_line(top_stack) and not is_aosp_code_stack_line(top_stack):
            basic_cause += ("栈顶在应用(%s) %s\n" % (top_stack.strip(), get_readable_state_for_detail(state)))
        elif is_sleep(top_stack, state):
            basic_cause += ("%s 调用了sleep没有唤醒导致\n", top_stack)
        elif is_native(state):
            basic_cause = parse_native_stack(basic_cause, stack_tree)

        return basic_cause, detail_cause

    def assemble_ref_thread_stacks(self, pre_pid, cur_pid, cmd_line, thread_info_stack):
        top_head_info = self.anrChain.top_head_info

        if pre_pid != cur_pid:
            ref_thread_stack = colorize("所在进程[%s]: %s\n" % (top_head_info.pid, cmd_line.to_string()), fg=YELLOW)
        else:
            ref_thread_stack = ''

        ref_thread_stack += thread_info_stack.to_string()
        return ref_thread_stack
