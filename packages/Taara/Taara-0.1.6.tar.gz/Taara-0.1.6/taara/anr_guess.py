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
from taara.stack.anr_stack import is_java_layer_stack_line, is_aosp_code_stack_line, guess_normal_stack, \
    get_main_thread_stack, assemble_ref_thread_stacks, get_some_stack
from taara.taara_teminal_color import print_header, colorize, RED


def guess_top_main_thread(top_process_data, basic_cause, detail_cause,
                          ref_thread_stacks):
    top_main_thread = get_main_thread_stack(top_process_data.thread_info_stacks)
    state = top_main_thread.state.upper()

    assemble_ref_thread_stacks(top_process_data, ref_thread_stacks)

    detail_cause += ("主线状态(%s): %s\n" % (state, get_readable_state(state)))

    stack_tree = top_main_thread.stack_tree
    top_stack = stack_tree[0]
    if is_sleep(top_stack, state):
        basic_cause += ("%s 调用了sleep没有唤醒导致\n", top_stack)
    else:
        basic_cause += guess_normal_stack(stack_tree)
    return basic_cause, detail_cause


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

        for head_info in ref_process_data:
            process_data = ref_process_data[head_info]
            if head_info == top_head_info:
                # 发生问题的进程
                basic_cause, detail_cause = self.guess_top_process(process_data, basic_cause, detail_cause,
                                                                   ref_thread_stacks)
            else:
                assemble_ref_thread_stacks(process_data, ref_thread_stacks)

        lock_obj_handler = self.anrChain.lock_obj_handler
        basic_cause = lock_obj_handler.guess_lock_cause(top_head_info, basic_cause)

        print_header("------> 基本原因: ")
        print basic_cause

        print_header("------> 基本描述: ")
        print detail_cause

        # 没有任何关联的时候，将顶部堆栈前3个输出
        if len(ref_thread_stacks) <= 0:
            top_process_data = self.anrChain.all_process_data_map[top_head_info]
            assemble_ref_thread_stacks(top_process_data, ref_thread_stacks, 3)

        if len(ref_thread_stacks) > 0:
            print_header("------> 相关堆栈: ")
            for stack in ref_thread_stacks:
                print stack

    def guess_top_process(self, top_process_data, basic_cause, detail_cause, ref_thread_stacks):
        binder_stack_handler = self.anrChain.binder_stack_handler
        top_head_info = self.anrChain.top_head_info

        top_main_thread = get_main_thread_stack(top_process_data.thread_info_stacks)

        cmd_line = top_process_data.cmd_line

        print "                  Taara ANR原因猜想"

        if top_process_data.cmd_line.is_system_server():
            basic_cause += "需特别留意: " + colorize("系统服务ANR", RED) + "\n"

        if binder_stack_handler.is_binder_invoke:
            basic_cause += "栈顶Binder调用: %s#%s\n" % \
                           (binder_stack_handler.interface_name, binder_stack_handler.method_name)
            basic_cause = binder_stack_handler.guess_service_invoke_detail(basic_cause)
            basic_cause += "\n"

        if top_main_thread is None:
            basic_cause += "未知"
            detail_cause += "需特别留意: 主线程堆栈未找到\n"
        else:
            basic_cause, detail_cause = guess_top_main_thread(top_process_data, basic_cause, detail_cause,
                                                              ref_thread_stacks)
        if top_head_info is None:
            detail_cause += "发生时间: 未知\n"
        else:
            detail_cause += "发生时间: %s\n" % top_head_info.get_time_string()

        detail_cause += "包/指令: %s\n" % cmd_line.to_string()
        return basic_cause, detail_cause
