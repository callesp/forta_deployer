# -*- encoding: utf-8 -*-
from base64 import encode
from nis import match
import os
import sys
import time
import csv
import paramiko
import traceback
from threading import Thread

output_dir = 'output'


def async_func(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async_func
def ssh(ip, username, password):

    # 创建ssh客户端
    client = paramiko.SSHClient()

    node_output_dir = f'{output_dir}/{ip}'

    # Create node output directory.
    if not os.path.exists(node_output_dir):
        os.mkdir(node_output_dir)

    with open(f'{node_output_dir}/output.log', 'w+') as log, open(f'{node_output_dir}/error.log', 'w+') as errlog:
        try:
            # 第一次ssh远程时会提示输入yes或者no
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 密码方式远程连接
            client.connect(ip, 22, username=username,
                           password=password, timeout=5)
            # 互信方式远程连接
            # key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
            # ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)

            # 上传脚本
            sftp = client.open_sftp()
            sftp.put('install.sh', '/root/install.sh')

            # 修改权限
            client.exec_command('chmod +x /root/install.sh')

            # 执行命令
            stdin, stdout, stderr = client.exec_command(
                f'sh /root/install.sh passwd owner_addres')

            if stdout.readable:
                output = str(stdout.read(), encoding='utf-8')
                print(f'stdout: {output}')
                log.write(output)

            if stderr.readable:
                output = str(stderr.read(), encoding='utf-8')
                print(f'stderr: {output}')
                errlog.write(output)

            # Get account address.
            stdin, stdout, stderr = client.exec_command(
                f'su - forta -c "forta account address" 2>&1')

            if stdout.readable:
                token = str(stdout.read(), encoding='utf-8')

                if token:
                    token_dir = f'{node_output_dir}/{token}'
                    os.mkdir(f'{token_dir}')
                    for sub_item in sftp.listdir('/home/forta/.forta/.keys'):
                        sftp.get(
                            f'/home/forta/.forta/.keys/{sub_item}', f'{token_dir}/{sub_item}')

        except Exception as e:
            errlog.write(traceback.format_exc())
            traceback.print_exc()

        finally:
            client.close()


def main():
    # assets_path = sys.argv[1]
    assets_path = 'assets.csv'

    # Make sure that we have assets.csv.
    if not os.path.exists(assets_path):
        print('Assets path does not exists.')
        return

    # Create logs directory at current path.
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    nodes_list = []

    with open(assets_path, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)
            nodes_list.append(row)

    while len(nodes_list):
        node_part = nodes_list[0:5]

        for ip, user, passwd in node_part:
            # Do something here.
            ssh(ip, user, passwd)

        del nodes_list[0:5]


if __name__ == '__main__':
    main()
