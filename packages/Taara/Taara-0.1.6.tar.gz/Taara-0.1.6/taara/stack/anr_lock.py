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

# - waiting to lock <0x090eb953> (a a.b.c.d) held by thread 16
from taara.stack.anr_stack import is_wait_lock_line, is_lock_stack_line, get_some_stack, is_java_layer_stack_line
from taara.taara_teminal_color import colorize, YELLOW, BLUE, CYAN, RED


def find_wait_obj_thread(stack_tree):
    for stack_line in stack_tree:
        if is_wait_lock_line(stack_line):
            finders = WAIT_LOCK_INFO.findall(stack_line)[0]
            obj = finders[0]
            obj_path = finders[1]
            hold_tid = finders[2]
            return obj, obj_path, hold_tid

    return None, None, None


def find_stack_tree_by_wait_obj_thread(wait_obj, thread_info_stacks):
    for thread_info_stack in thread_info_stacks:
        for stack_line in thread_info_stack.stack_tree:
            if is_wait_lock_line(stack_line, wait_obj):
                return thread_info_stack.stack_tree
    return None


def find_lock_obj_thread(lock_obj, thread_info_stacks):
    for thread_info_stack in thread_info_stacks:
        for stack_line in thread_info_stack.stack_tree:
            if is_lock_stack_line(stack_line, lock_obj):
                return thread_info_stack
    return None


WAIT_LOCK_INFO = re.compile(r'- waiting to lock (\S*) \(a ([^)]*)\) held by thread (\d*)')
# - locked <0x090eb953> (a a.b.c.d)
LOCK_OBJ_INFO = re.compile(r'- locked (\S*) \(a ([^)]*)\)')


class LockThreadAtom:
    def __init__(self, wait_obj, wait_thread_info_stack, lock_thread_info_stack):
        self.wait_obj = wait_obj
        self.wait_thread_info_stack = wait_thread_info_stack
        self.lock_thread_info_stack = lock_thread_info_stack

    def to_string(self):
        wait_thread_name = self.wait_thread_info_stack.thread_name
        wait_thread_tid = self.wait_thread_info_stack.tid
        if self.lock_thread_info_stack is None:
            return "%s线程(TID[%s]) 正在等待释放 %s，但是找不到阻塞处" % (wait_thread_name, wait_thread_tid, self.wait_obj)
        else:
            lock_thread_name = self.lock_thread_info_stack.thread_name
            lock_thread_tid = self.lock_thread_info_stack.tid
            return "%s线程(TID[%s]) 等待 %s(TID[%s]) 释放 %s" % \
                   (wait_thread_name, wait_thread_tid, lock_thread_name, lock_thread_tid, self.wait_obj)

    def to_string_with_sample_stack(self):
        title = self.to_string()
        wait_thread_name = self.wait_thread_info_stack.thread_name
        wait_thread_stack_tree = self.wait_thread_info_stack.stack_tree
        wait_detail = colorize(wait_thread_name, BLUE) + ":\n"

        wait_sample_thread_stack = get_some_stack(wait_thread_stack_tree, is_java_layer_stack_line)
        wait_detail += wait_sample_thread_stack

        lock_thread_name = self.lock_thread_info_stack.thread_name
        lock_thread_stack_tree = self.lock_thread_info_stack.stack_tree
        lock_detail = colorize(lock_thread_name, BLUE) + ":\n"

        lock_sample_thread_stack = get_some_stack(lock_thread_stack_tree, is_lock_stack_line)
        lock_detail += lock_sample_thread_stack

        return colorize(title, YELLOW) + "\n" + wait_detail + lock_detail


class LockChain:

    def __init__(self):
        self.lock_obj_chain = []
        self.lock_thread_chain = []
        # 最后一个不是被阻塞的stack
        self.dirty_thread = None
        self.dead_lock = False

    def get_lock_atom_list(self):
        lock_atom_list = []
        cursor_index = 0
        for lock_obj in self.lock_obj_chain:
            wait_thread = self.lock_thread_chain[cursor_index]
            lock_thread = find_lock_obj_thread(lock_obj, self.lock_thread_chain)
            lock_atom_list.append(LockThreadAtom(lock_obj, wait_thread, lock_thread))
            cursor_index += 1

        return lock_atom_list

    def get_lock_stack(self):
        lock_stack = ""
        index = len(self.lock_obj_chain) - 1
        print self.lock_obj_chain
        while index >= 0:
            lock_obj = self.lock_obj_chain[index]
            lock_stack += "被锁对象 %s, 堆栈:\n" % lock_obj
            lock_stack += self.lock_thread_chain[index].to_string() + "\n"
            index -= 1
        return lock_stack


class LockObjHandler:
    def __init__(self):
        # head_info: lock_chain
        self.lock_chain_map = {}

    def process_for_main_wait(self, head_info, thread_info_stacks):
        # 调查主线程被阻塞的原因，如果主线程被阻塞
        main_thread_stack_tree = None
        main_thread = None
        for thread_info_stack in thread_info_stacks:
            if thread_info_stack.is_main:
                main_thread = thread_info_stack
                main_thread_stack_tree = thread_info_stack.stack_tree
                break

        if main_thread_stack_tree is None:
            # 找不到主线程，目前我们直接忽略
            return None

        main_wait_obj, main_wait_obj_path, hold_main_obj_tid = find_wait_obj_thread(main_thread_stack_tree)
        if main_wait_obj is None:
            # 主线程并没有被阻塞
            return None

        lock_obj_chain = []
        lock_thread_chain = []

        wait_obj = main_wait_obj
        wait_thread = main_thread

        dirty_thread = None
        dead_lock = False
        while wait_obj is not None:
            lock_obj_chain.append(wait_obj)
            lock_thread_chain.append(wait_thread)

            # 找阻塞的地方
            block_thread = find_lock_obj_thread(wait_obj, thread_info_stacks)
            if block_thread is None:
                # 找不到阻塞的地方
                break

            if block_thread in lock_thread_chain:
                # 存在死锁
                dead_lock = True
                break

            # 看该线程是否被阻塞
            wait_obj, wait_obj_path, main_obj_tid = find_wait_obj_thread(block_thread.stack_tree)
            if wait_obj is None:
                # 该线程不是被阻塞
                dirty_thread = block_thread
                # print "最后不是阻塞 %s" % block_thread.to_string()
                break
            else:
                wait_thread = block_thread

        lock_chain = LockChain()
        lock_chain.lock_thread_chain = lock_thread_chain
        lock_chain.lock_obj_chain = lock_obj_chain
        lock_chain.dirty_thread = dirty_thread
        lock_chain.dead_lock = dead_lock

        self.lock_chain_map[head_info] = lock_chain

        return lock_thread_chain

    def is_top_main_block(self):
        pass

    def guess_lock_cause(self, top_head_info, basic_cause):
        for head_info in self.lock_chain_map:
            if head_info == top_head_info:
                lock_chain = self.lock_chain_map[head_info]
                if lock_chain.dead_lock:
                    lock_cause_title = "锁检测结果: 存在死锁"
                elif lock_chain.dirty_thread:
                    lock_cause_title = "锁检测结果: 最后的堆栈非锁行为"
                else:
                    lock_cause_title = "锁检测结果: 最后的堆栈未知行为"

                basic_cause += "\n" + lock_cause_title + "\n"
                lock_atom_list = lock_chain.get_lock_atom_list()
                for lock_atom in lock_atom_list:
                    basic_cause += lock_atom.to_string_with_sample_stack() + "\n"

        return basic_cause
