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


STATE_RUNNABLE = "RUNNABLE"
STATE_NATIVE = "NATIVE"


def get_readable_state(state=''):
    if state.upper().__eq__("TERMINATED"):
        return "线程死亡"
    elif state.upper().__eq__(STATE_RUNNABLE):
        return "线程可运行/正在运行"
    elif state.upper().__eq__("TIMED_WAITING"):
        return "阻塞等待(执行了带有超时参数的wait、sleep或join函数)"
    elif state.upper().__eq__("BLOCKED"):
        return "阻塞，等待获取对象锁"
    elif state.upper().__eq__("WAITING"):
        return "执行了无超时参数的wait函数"
    elif state.upper().__eq__("NEW"):
        return "线程正在初始化"
    elif state.upper().__eq__("NATIVE"):
        return "Native调用"
    elif state.upper().__eq__("SLEEPING"):
        return "正在阻塞Sleep"
    else:
        return "未知"


def is_sleep(top_stack_string='', state=''):
    return top_stack_string.__contains__("sleep") and state.upper().__eq__(STATE_RUNNABLE)


def is_native(state=''):
    return state.upper().__eq__(STATE_NATIVE)


def get_readable_state_for_detail(state=''):
    if not state:
        return ''
    elif state.upper().__eq__("TERMINATED"):
        return "线程死亡"
    elif state.upper().__eq__(STATE_RUNNABLE):
        return "正在运行"
    elif state.upper().__eq__("TIMED_WAITING"):
        return "阻塞等待(执行了带有超时参数的wait、sleep或join函数)"
    elif state.upper().__eq__("BLOCKED"):
        return "阻塞，等待获取对象锁"
    elif state.upper().__eq__("WAITING"):
        return "执行了无超时参数的wait函数"
    elif state.upper().__eq__("NEW"):
        return "线程正在初始化"
    else:
        return "未知"
