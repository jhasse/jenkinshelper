import os, subprocess

class PushDir(object):
    def __init__(self, new_dir):
        self.old_dir = os.getcwd()
        self.new_dir = new_dir
    def __enter__(self):
        os.chdir(self.new_dir)
    def __exit__(self, type, value, tb):
        os.chdir(self.old_dir)

def run(cmd, may_fail=False):
    print("\x1b[0;34m$ " + cmd + "\x1b[0m")
    if may_fail:
        subprocess.call(cmd, shell=True)
    else:
        subprocess.check_call(cmd, shell=True)
