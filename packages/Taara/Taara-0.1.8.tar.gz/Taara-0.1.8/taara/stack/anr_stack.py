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
from taara.taara_teminal_color import colorize, YELLOW, colorize_title


def _assemble_ref_thread_stacks(pre_pid, cur_pid, cmd_line, thread_info_stack):
    if pre_pid != cur_pid:
        ref_thread_stack = colorize("所在进程[%s]: %s\n" % (cur_pid, cmd_line.to_string()), fg=YELLOW)
    else:
        ref_thread_stack = ''

    ref_thread_stack += thread_info_stack.to_string()
    return ref_thread_stack


def assemble_ref_thread_stacks(process_data, ref_thread_stacks, max_count=-1):
    pre_pid = -1
    cur_pid = process_data.head.pid
    count = 0
    for thread_info_stack in process_data.thread_info_stacks:
        ref_thread_stacks.append(
            _assemble_ref_thread_stacks(pre_pid, cur_pid, process_data.cmd_line, thread_info_stack))
        cur_pid = pre_pid
        count += 1
        if 0 < max_count <= count:
            break


def get_main_thread_stack(thread_info_stacks):
    for thread_info_stack in thread_info_stacks:
        if thread_info_stack.is_main:
            return thread_info_stack

    return None


def is_kernal_stack_line(stack_line=''):
    return stack_line.strip().startswith('kernal')


def is_java_layer_stack_line(stack_line=''):
    return stack_line.strip().startswith('at ')


def is_wait_lock_line(stack_line='', wait_obj=None):
    if wait_obj is None:
        return stack_line.lstrip().startswith('- waiting to lock <')
    else:
        return stack_line.lstrip().startswith('- waiting to lock %s' % wait_obj)


def is_lock_stack_line(stack_line='', locked_obj=None):
    if locked_obj is None:
        return stack_line.lstrip().startswith('- locked <')
    else:
        return stack_line.lstrip().startswith('- locked %s' % locked_obj)


def is_aosp_code_stack_line(stack_line=''):
    strip_line = stack_line.strip()
    return (strip_line.startswith('at android.') or
            strip_line.startswith('at dalvik.') or
            strip_line.startswith('at com.android.internal') or
            strip_line.startswith('at com.android.app') or
            strip_line.startswith('at com.android.server') or
            strip_line.startswith('at com.android.content') or
            strip_line.startswith('at java.lang') or
            strip_line.startswith('at java.io') or
            strip_line.startswith('at java.util'))


def is_binder_transact(stack_line=''):
    return stack_line.strip().startswith('at android.os.BinderProxy.')


def is_binder_transact_native(stack_line=''):
    return stack_line.__contains__('/system/lib/libbinder.so')


def is_binder_invoke_stack(stack_tree):
    for stack_line in stack_tree:
        if is_binder_transact_native(stack_line) or is_binder_transact(stack_line):
            return True
    return False


def guess_normal_stack(stack_tree):
    basic_cause = ''
    top_stack = stack_tree[0]
    is_native = not is_java_layer_stack_line(top_stack)

    first_three_stack = get_some_stack(stack_tree)

    if is_native:
        # 将前3行native堆栈输出
        basic_cause += colorize_title("栈顶在Native代码:") + "\n%s" % first_three_stack
        basic_cause += guess_native_stack(stack_tree)
    elif is_aosp_code_stack_line(top_stack):
        basic_cause += colorize_title("栈顶在AOSP代码:") + "\n%s" % first_three_stack
    else:
        basic_cause += colorize_title("栈顶在应用代码:") + "\n%s" % first_three_stack

    return basic_cause


def guess_native_stack(stack_tree):
    # 将调用native的关键java层打出
    basic_cause = ''
    java_layer_stack_line = get_some_stack(stack_tree, is_java_layer_stack_line)
    if java_layer_stack_line:
        basic_cause += colorize_title("Java层触发关键:") + "\n%s\n" % java_layer_stack_line

    # 将上层应用的可以第一个堆栈输出
    not_aosp_stack_line = get_some_stack(stack_tree, is_java_no_aosp_code_line, 3)
    if not_aosp_stack_line:
        basic_cause += colorize_title("上层调用关键:") + "\n%s" % not_aosp_stack_line
    else:
        basic_cause += "关键堆栈都是AOSP的调用栈\n"
    return basic_cause


def is_java_no_aosp_code_line(stack_line):
    return is_java_layer_stack_line(stack_line) and not is_aosp_code_stack_line(stack_line)


def get_some_stack(stack_tree, condition_func=None, line_count=3):
    stacks = None
    stack_line_count = 0
    for stack_line in stack_tree:
        if stacks is None and callable(condition_func):
            pre_condition = condition_func(stack_line)
        else:
            pre_condition = True

        if pre_condition and stacks is None:
            stacks = ''

        if pre_condition:
            stacks += stack_line + "\n"

        if stacks is not None:
            stack_line_count += 1

        if stack_line_count >= line_count:
            break

    return stacks
