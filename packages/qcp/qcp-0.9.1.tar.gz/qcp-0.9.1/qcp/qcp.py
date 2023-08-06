import sys
import getopt
import getpass
import os

help_msg = r'''
usage: 
qcp -h
qcp [-u togo] [-r] -i gpu1,gpu2 hahaha /abs_path/dir ./rel_path/file

-h : help
-u : username[default: current_username]
-i : ip[eg: gpu1 | gpu1,gpu2 | 192.168.1.1 192.168.2.2]
-r : reverse[default send, use -r to receive]
'''

if __name__ == '__main__':
    username = getpass.getuser()
    directory = os.path.abspath('.')
    ips = ''
    direction = 1 # 1 send, 0 recive
    opts,args = getopt.getopt(sys.argv[1:],"hru:i:",["help","reverse","username=","ip="])
    for k,v in opts:
        if k in ('-h','--help'):
            print(help_msg)
            sys.exit()
        if k in ('-u','--username'):
            username = v
        if k in ('-i','--ip'):
            ips = v
        if k in ('-r','--reverse'):
            direction = 0
    if ips == '':
        print("remote ip is needed! Refer help:")
        print(help_msg)
        sys.exit()
    ips = ips.split(',')
    if args == []:
        print("Files to be transferred should be determined! Refer help:")
        print(help_msg)
        sys.exit()
    objs = [v if v[0] == '/' else os.path.join(directory,v) for v in args]
    print("checking...")
    for v in objs:
        if not os.path.exists(v):
            print("{} does not exits!".format(v))
            sys.exit()
        if os.path.isdir(v):
            print("{} is directory!".format(v))
        if os.path.isfile(v):
            print("{} is file!".format(v))
    print("check OK")
    print("transferring...")
    print("ips={}".format(ips))
    print("objs={}".format(objs))
    for ip in ips:
        for obj in objs:
            obj = os.path.abspath(obj)
            dir,_ = os.path.split(obj)
            dir = dir+'/'
            print('dir:',dir)
            if direction:
                print(">"*40)
                cmd = "scp -r {obj} {username}@{ip}:{dst}".format(
                obj=obj,
                username=username,
                ip=ip,
                dst=dir)
            else:
                print("<"*40)
                cmd = "scp -r {username}@{ip}:{dst} {obj}".format(
                obj=obj,
                username=username,
                ip=ip,
                dst=dir)
            print("cmd={}".format(cmd))
            ret = os.system(cmd)
            if ret != 0:
                print("Failed, cmd = {}".format(cmd))
                assert(0)



