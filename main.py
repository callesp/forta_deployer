# -*- encoding: utf-8 -*-
import os
import sys
import time
import csv
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

    # 创建ssh客户端
    client = paramiko.SSHClient()
    try:
        # 第一次ssh远程时会提示输入yes或者no
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 密码方式远程连接
        client.connect(sys_ip, 22, username=username,
                       password=password, timeout=5)
        # 互信方式远程连接
        # key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
        # ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)
        # 执行命令
        for cmd_name, cmd in cmds:
            print('*'*10 + cmd_name + '*'*10)
            stdin, stdout, stderr = client.exec_command(cmd)
            # 获取命令执行结果,返回的数据是一个list
            result = stdout.readlines()

            if len(result) > 0:
                print(f'{sys_ip}:{str(result[0])}')
            else:
                result = stderr.readlines()
                print(f'{sys_ip}: {result}')

    except Exception as e:
        print(f'{sys_ip} error: {e}')

        traceback.print_exc()

    finally:
        client.close()


CMD_TIME_SYNC = 'systemctl enable systemd-timesyncd && systemctl start systemd-timesyncd && timedatectl status'
CMD_UNINSTALL_DOCKER = 'yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine'
CMD_INSTALL_DOCKER = 'yum install -y yum-utils \
    && yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo \
    && yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin'

CMD_CONFIG_DOCKER = '''echo "{
   "default-address-pools": [
        {
            "base":"172.17.0.0/12",
            "size":16
        },
        {
            "base":"192.168.0.0/16",
            "size":20
        },
        {
            "base":"10.99.0.0/16",
            "size":24
        }
    ]
}" > /etc/docker/daemon.json'''

CMD_START_DOCKER = 'systemctl start docker'


FORTA_INSTALLATION = zip(['time sync', 'uninstall docker', 'install docker', 'config docker', 'start docker'], [CMD_TIME_SYNC, CMD_UNINSTALL_DOCKER,
                                                                                                                CMD_INSTALL_DOCKER, CMD_CONFIG_DOCKER, CMD_START_DOCKER])


def main():
    # assets_path = sys.argv[1]
    assets_path = 'assets.csv'

    if not os.path.exists(assets_path):
        print('Assets path does not exists.')
        return

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
            ssh(ip, user, passwd, FORTA_INSTALLATION)

        del nodes_list[0:5]


if __name__ == '__main__':
    main()
