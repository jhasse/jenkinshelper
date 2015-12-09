"""
Useful tools for continuous integration
"""

import os
import subprocess
from jenkinshelper import log

root_working_dir = os.getcwd()

class PushDir(object):
    def __init__(self, new_dir):
        self.old_dir = os.getcwd()
        self.new_dir = new_dir
    def __enter__(self):
        os.chdir(self.new_dir)
    def __exit__(self, type, value, tb):
        os.chdir(self.old_dir)

def run(cmd, may_fail=False):
    path = os.path.relpath(os.getcwd(), root_working_dir)
    if path == ".":
        path = ""
    else:
        path += " "
    print("\x1b[1;34m{}$ {}\x1b[0m".format(path, cmd))
    if may_fail:
        subprocess.call(cmd, shell=True)
    else:
        subprocess.check_call(cmd, shell=True)

def loadEnv(cmd):
    """
    Runs a cmd and loads the environment variables it sets
    """
    log.info("Loading environment variables from " + cmd)
    variables = subprocess.check_output(cmd + ' && set')
    for var in variables.splitlines():
        var = var.decode('cp1252') # FIXME: This works on (German?) Windows only
        k, _, v = [x.strip() for x in var.strip().partition('=')]
        if k.startswith('?') or k == '':
            continue
        os.environ[k] = v
