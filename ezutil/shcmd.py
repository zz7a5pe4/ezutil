#!/usr/bin/python

import shlex, subprocess, os

import pexpect

#bash treat return value 0 as success
class ShellResult():
    #__slots__=["output", "error", "cmd", "ret"]
    output = ""
    error = ""
    cmd = ""
    ret = -1
    def __init__(self, cmd = ""):
        if cmd:
            self.cmd = cmd

    def __str__(self):
        if self.ret == 0:
            return "{cmdline} - Success\n{output}".format(cmdline = self.cmd, output=self.output)
        else:
            return "{cmdline} - Failed: {returnvalue}\n{errmsg}".format(returnvalue = self.ret, cmdline = self.cmd, errmsg=self.error)

    def __nonzero__(self):
        if self.ret == 0:
            return True
        else:
            return False


def syncexec(shellcmds):
    if not shellcmds:
        return None
    args = shlex.split(shellcmds)
    ret = ShellResult()
    ret.cmd = shellcmds
    p = subprocess.Popen(args,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret.output,ret.error = p.communicate()
    ret.ret = p.returncode
    return ret

def syncexec_timeout(shellcmds, t=600):
    if not shellcmds:
        return None
    ret = ShellResult()
    ret.cmd = shellcmds
    child = None
    try:
        child = pexpect.spawn(shellcmds, timeout=t)
        ret.output=""
        #index = p.expect ([pexpect.EOF, pexpect.TIMEOUT])
        while(1):
            i = child.readline()
            ret.output += i
            if not i:
                break
            ret.error = ret.output
    except pexpect.TIMEOUT as e:
        ret.error = "Timeout while running: {0}".format(shellcmds)
    except pexpect.ExceptionPexpect as e:
        ret.error = str(e)
    except KeyboardInterrupt as e:
        ret.output += "terminated by keyborad input from user"
    finally:
        if child:
            child.close()
            ret.ret = child.exitstatus
    return ret

def isroot():
    return os.getuid() == 0

def main():
    if len(sys.argv) < 2:
        cmd = r"ls -al ."
    else:
        cmd = " ".join(sys.argv[1:])

    os.environ["http_proxy"]=""
    r = syncexec_timeout(cmd,1)
    print r
    if not isroot():
        print "run as root please"
        sys.exit(-1)

if __name__ == '__main__':
    import sys
    main()
