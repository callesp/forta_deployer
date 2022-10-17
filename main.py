# -*- encoding: utf-8 -*-
import os
import sys
import time
import paramiko
import traceback
from threading import Thread

def async_func(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@async_func
def ssh(sys_ip, username, password, cmds):
    try:
        # 创建ssh客户端
        client = paramiko.SSHClient()
        # 第一次ssh远程时会提示输入yes或者no
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 密码方式远程连接
        client.connect(sys_ip, 22, username=username, password=password, timeout=5)
        # 互信方式远程连接
        # key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
        # ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)
        # 执行命令
        stdin, stdout, stderr = client.exec_command(cmds,timeout=30)
        # 获取命令执行结果,返回的数据是一个list
        result = stdout.readlines()
        if len(result)>0:
            print(f'{sys_ip}:{str(result[0])}')
        else:
            print(f'{sys_ip}:none')

    except Exception as e:
        print(f'{sys_ip} error: {e}')

        traceback.print_exc()

    finally:
        client.close()
        
def main():
    file_path = sys.argv[1]
    
    print(file_path)
    
    # with open(file_path, 'r') as f:
        # pass    

    

if __name__ == '__main__':
    main()