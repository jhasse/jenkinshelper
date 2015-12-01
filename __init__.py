import os, subprocess

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
