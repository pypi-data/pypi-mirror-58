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
import time
from os import system

from taara.taara_utils import get_retrace_sh_path


def get_milli_time(): return int(round(time.time() * 1000))


def retrace_to_temp(mapping_file, stack_file, target_file):
    cmd = "/bin/bash " + get_retrace_sh_path() + " '%s' '%s' > '%s'" % (mapping_file, stack_file, target_file)
    print "start retrace with %s" % mapping_file
    start_millis = get_milli_time()
    stderr = system(cmd)
    if stderr:
        print "finish retrace failed with command %s" % cmd
        return False
    else:
        end_millis = get_milli_time()
        delta_millis = end_millis - start_millis
        print "success retrace cost: %dms" % delta_millis
        return True
