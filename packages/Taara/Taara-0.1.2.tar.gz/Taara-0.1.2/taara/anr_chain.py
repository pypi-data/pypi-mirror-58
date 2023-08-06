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
from taara.stack.anr_binder import BinderStackHandler
from taara.anr_file import HeadInfo, ThreadInfoStack, ProcessAllData, CMDLine
from taara.stack.anr_lock import LockObjHandler


def create_process_all_data(head_info, cmd_line):
    process_all_data = ProcessAllData()
    process_all_data.head = head_info
    process_all_data.cmd_line = cmd_line
    return process_all_data


class ANRChain:
    def __init__(self):
        self.chain_head_info_list = []
        self.ref_cause_process_data_map = {}
        self.top_head_info = None

        self.binder_stack_handler = BinderStackHandler()
        self.lock_obj_handler = LockObjHandler()

        self.cur_head_info = HeadInfo()
        self.cur_cmd = CMDLine()
        self.is_first_thread = True

        self.pre_head_info = None

        # 所有进程都保存
        self.all_process_data_map = {}

    def process(self, info):
        if isinstance(info, HeadInfo):
            self.cur_head_info = info
        elif isinstance(info, ThreadInfoStack):
            ref_cause = False
            # 顶部主线程
            is_top_main_thread = False
            if self.is_first_thread:
                # this is main cause for anr
                ref_cause = True
                is_top_main_thread = info.is_main
                self.is_first_thread = False

            # 准备接下来可能要用到的进程的所有数据
            if self.cur_head_info in self.ref_cause_process_data_map:
                ref_process_all_data = self.ref_cause_process_data_map[self.cur_head_info]
            else:
                ref_process_all_data = create_process_all_data(self.cur_head_info, self.cur_cmd)

            ref_cause = (self.binder_stack_handler.process(info.stack_tree, is_top_main_thread, ref_process_all_data) or
                         ref_cause)

            if ref_cause:
                # 得到顶部HeadInfo
                if self.top_head_info is None:
                    self.top_head_info = self.cur_head_info

                # 收集所有数据到process_all_data
                if self.cur_head_info not in self.ref_cause_process_data_map:
                    self.ref_cause_process_data_map[self.cur_head_info] = ref_process_all_data

                ref_process_all_data.thread_info_stacks.append(info)

            # 无论如何都存储，这个是备用队列，会存储所有的进程中每个线程的数据
            self.update_all_process_all_data(self.cur_head_info, self.cur_cmd, info)

            if self.pre_head_info != self.cur_head_info:
                # 这里是新的process，也就是说上一个process已经全部收集完
                # 此处我们做锁处理，因为锁处理是针对当前进程的所有线程来说的
                if self.pre_head_info and not self.pre_head_info.is_empty():
                    # 说明已经完成前一个并且是有效的
                    is_top_process = self.pre_head_info == self.top_head_info
                    self.parse_lock_and_add_ref_cause(self.pre_head_info, is_top_process)

            self.pre_head_info = self.cur_head_info

        elif isinstance(info, CMDLine):
            self.cur_cmd = info

    def update_all_process_all_data(self, head_info, cmd_line, thread_info):
        if head_info in self.all_process_data_map:
            process_all_data = self.all_process_data_map[head_info]
        else:
            process_all_data = create_process_all_data(head_info, cmd_line)
            self.all_process_data_map[head_info] = process_all_data
        process_all_data.thread_info_stacks.append(thread_info)

    def on_final_process(self):
        # 补充最后的解析
        if self.pre_head_info != self.cur_head_info:
            is_top_process = self.cur_head_info == self.top_head_info
            self.parse_lock_and_add_ref_cause(self.cur_head_info, is_top_process)

    def parse_lock_and_add_ref_cause(self, head_info, is_top_process):
        if head_info not in self.all_process_data_map:
            # print "unknown %s" % head_info.pid
            return

        if not is_top_process:
            # 暂时只处理顶部进程
            return

        process_all_data = self.all_process_data_map[head_info]
        thread_info_stacks = process_all_data.thread_info_stacks
        lock_thread_chain = self.lock_obj_handler.process_for_main_wait(head_info, thread_info_stacks)

        if lock_thread_chain is not None:
            if head_info in self.ref_cause_process_data_map:
                ref_process_all_data = self.ref_cause_process_data_map[head_info]
            else:
                cmd_line = self.all_process_data_map[head_info].cmd_line
                ref_process_all_data = create_process_all_data(head_info, cmd_line)
                self.ref_cause_process_data_map[head_info] = ref_process_all_data

            # 将没有添加到原因相干堆栈，添加
            for thread_info_stack in lock_thread_chain:
                if thread_info_stack not in ref_process_all_data.thread_info_stacks:
                    ref_process_all_data.thread_info_stacks.append(thread_info_stack)
