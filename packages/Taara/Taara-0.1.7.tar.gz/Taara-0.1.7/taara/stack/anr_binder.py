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

# at android.app.IActivityManager$Stub$Proxy.activityPaused(IActivityManager.java:4596)
from taara.stack.anr_stack import is_java_layer_stack_line, is_binder_transact, is_binder_invoke_stack, get_some_stack

BINDER_INVOKE_METHOD = re.compile(r'([^.]*)\(')
BINDER_INTERFACE_NAME = re.compile(r'\.([^.$]*)\$')


def get_binder_invoke_method(stack_tree):
    for stack_line in stack_tree:
        if is_java_layer_stack_line(stack_line) and not is_binder_transact(stack_line):
            finders = BINDER_INVOKE_METHOD.findall(stack_line)
            method_name = finders[0]
            finders = BINDER_INTERFACE_NAME.findall(stack_line)
            interface_name = finders[0]
            return interface_name, method_name


class BinderStackHandler:
    def __init__(self):
        pass

    interface_name = None
    method_name = None
    is_binder_invoke = False
    guess_ref_class_name = None
    server_invoke_stack_tree = None
    server_invoke_process_all_data = None

    def process(self, stack_tree, is_top_main_thread, process_data):
        if is_top_main_thread and is_binder_invoke_stack(stack_tree):
            self.interface_name, self.method_name = get_binder_invoke_method(stack_tree)
            self.is_binder_invoke = True

            if self.interface_name.strip().startswith("I"):
                self.guess_ref_class_name = self.interface_name[1:]
            ref_stack = True
        else:
            ref_stack = self.is_binder_invoke and self.is_ref_stack_tree(stack_tree)

        if not is_top_main_thread and ref_stack:
            self.server_invoke_stack_tree = stack_tree
            self.server_invoke_process_all_data = process_data

        return ref_stack

    def is_ref_stack_tree(self, stack_tree):
        if not self.is_binder_invoke:
            return False

        for stack_line in stack_tree:
            if self.interface_name in stack_line:
                return True
            if self.method_name in stack_line:
                # 如果包含相同方法说明是对端
                self.server_invoke_stack_tree = stack_tree
                return True
            if self.guess_ref_class_name is not None and self.guess_ref_class_name in stack_line:
                return True

        return False

    def guess_service_invoke_detail(self, basic_cause):
        if self.server_invoke_stack_tree is None:
            basic_cause += "但是未找到有效对端调用堆栈，下面相关堆栈中将打出所有相关可以参考\n"
        else:
            head_info = self.server_invoke_process_all_data.head_info
            cmd_line = self.server_invoke_process_all_data.cmd_line
            thread_info_stacks = self.server_invoke_process_all_data.thread_info_stacks
            basic_cause += "Binder对端[%s, %s]线程[%s, %s]调用:\n" % \
                           (cmd_line.to_string(), head_info.pid, thread_info_stacks.thread_name, thread_info_stacks.tid)
            # 给三行堆栈
            stack_tree = thread_info_stacks.stack_tree
            some_stack = get_some_stack(stack_tree, is_java_layer_stack_line)
            basic_cause += some_stack

        return basic_cause
