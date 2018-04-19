#!/usr/bin/env python3

import psutil
import os

filterUserName = os.environ.get('Z_HUNTER_USERNAME')
filterProcess= os.environ.get('Z_HUNTER_PROCESS_NAME')
for proc in psutil.process_iter():
     try:
         p = proc.as_dict(attrs=['ppid', 'pid', 'name', 'username', 'status', 'cmdline'])
     except psutil.NoSuchProcess:
         pass
     else:
         if p['status'] == 'zombie':
            killZombie = True
            if filterUserName != None and p['username'] != filterUserName:
                 killZombie = False

            if filterProcess != None and filterProcess not in p['cmdLine']:
                killZombie = False

            if True == killZombie:
                print("killing " + str(p['pid']))
                os.system("sudo gdb -p " + str(p['ppid']) + " -batch -ex 'call waitpid("+ str(p['pid'])+",0,0)' -ex quit")
            else:
                    print("process [" + str(p['pid']) + "] is a zombie but does not match process or user filter")
