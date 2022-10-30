# -*- encoding: utf-8 -*-
import enum
import os
import threading
import click
import csv
import paramiko
import traceback
from threading import Thread

thread_lock = threading.Lock()
count = 0

TIMEOUT = 30

output_dir = 'output'

@click.group()
def cli():
    pass


def async_func(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async_func
def ssh_stage1(ip, password, wallet_passwd):

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
            client.connect(ip, 22, username='root',
                           password=password, timeout=TIMEOUT)
            # 互信方式远程连接
            # key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
            # ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)

            # 上传脚本
            sftp = client.open_sftp()
            sftp.put('inst_stage1.sh', '/root/inst_stage1.sh')

            # 修改权限
            client.exec_command('chmod +x /root/inst_stage1.sh')

            # 执行安装stage 1命令
            stdin, stdout, stderr = client.exec_command(
                f'sh /root/inst_stage1.sh {wallet_passwd}')

            if stdout.readable:
                output = str(stdout.read(), encoding='utf-8')
                print(f'stdout[{ip}]: {output}')
                log.write(output)

            if stderr.readable:
                output = str(stderr.read(), encoding='utf-8')
                print(f'stderr[{ip}]: {output}')
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

@async_func
def ssh_stage2(ip, password, owner_address, wallet_passwd):
    # 创建ssh客户端
    client = paramiko.SSHClient()

    node_output_dir = f'{output_dir}/{ip}'

    # Create node output directory.
    if not os.path.exists(node_output_dir):
        print(f'Error: output directory is not found.')
        return

    with open(f'{node_output_dir}/output.log', 'a+') as log, open(f'{node_output_dir}/error.log', 'a+') as errlog:
        try:
            # 第一次ssh远程时会提示输入yes或者no
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 密码方式远程连接
            client.connect(ip, 22, username='root',
                           password=password, timeout=TIMEOUT)
            # 互信方式远程连接
            # key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
            # ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)

            # 上传脚本
            sftp = client.open_sftp()
            sftp.put('inst_stage2.sh', '/root/inst_stage2.sh')

            # 修改权限
            client.exec_command('chmod +x /root/inst_stage2.sh')

            # 执行安装stage 2命令
            stdin, stdout, stderr = client.exec_command(
                f'sh /root/inst_stage2.sh {wallet_passwd} {owner_address}')

            if stdout.readable:
                output = str(stdout.read(), encoding='utf-8')
                print(f'stdout: {output}')
                log.write(output)

            if stderr.readable:
                output = str(stderr.read(), encoding='utf-8')
                print(f'stderr: {output}')
                errlog.write(output)

        except Exception as e:
            errlog.write(traceback.format_exc())
            traceback.print_exc()

        finally:
            client.close()

@async_func
def ssh_clean(ip, password):
    # 创建ssh客户端
    client = paramiko.SSHClient()

    node_output_dir = f'{output_dir}/{ip}'

    # Create node output directory.
    if not os.path.exists(node_output_dir):
        print(f'Error: output directory is not found.')
        return

    with open(f'{node_output_dir}/output.log', 'a+') as log, open(f'{node_output_dir}/error.log', 'a+') as errlog:
        try:
            # 第一次ssh远程时会提示输入yes或者no
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 密码方式远程连接
            client.connect(ip, 22, username='root',
                           password=password, timeout=TIMEOUT)
            # 互信方式远程连接
            # key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
            # ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)

            # 上传脚本
            sftp = client.open_sftp()
            sftp.put('clean.sh', '/root/clean.sh')

            # 修改权限
            client.exec_command('chmod +x /root/clean.sh')

            # 执行安装stage 2命令
            stdin, stdout, stderr = client.exec_command(
                f'sh /root/clean.sh')

            if stdout.readable:
                output = str(stdout.read(), encoding='utf-8')
                print(f'stdout: {output}')
                log.write(output)

            if stderr.readable:
                output = str(stderr.read(), encoding='utf-8')
                print(f'stderr: {output}')
                errlog.write(output)

        except Exception as e:
            errlog.write(traceback.format_exc())
            traceback.print_exc()

        finally:
            client.close()


@async_func
def ssh_cmd(ip, password, cmd):
    # 创建ssh客户端
    client = paramiko.SSHClient()

    try:
        # 第一次ssh远程时会提示输入yes或者no
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 密码方式远程连接
        client.connect(ip, 22, username='root',
                        password=password, timeout=TIMEOUT)
        # 互信方式远程连接
        # key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
        # ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)

        # 执行安装cmd命令
        stdin, stdout, stderr = client.exec_command(
            f'{cmd}')

        thread_lock.acquire()

        print('*'*50)
        global count
        count += 1
        print(f'Count: {count}')
        if stdout.readable:
            output = str(stdout.read(), encoding='utf-8')
            print(f'stdout[{ip}]: {output}')

        if stderr.readable:
            output = str(stderr.read(), encoding='utf-8')
            print(f'stderr[{ip}]: {output}')
        print('*'*50)

        thread_lock.release()

    except Exception as e:
        traceback.print_exc()

    finally:
        client.close()
class Procedure(enum.Enum):
    Stage1 = 1,
    Stage2 = 2,
    Cmd = 3,
    Clean = 4


@click.command()
@click.option('--assets', default='assets.csv', help='Assets file.')
def stage1(assets):
    main(Procedure.Stage1, assets)

@click.command()
@click.option('--assets', default='assets.csv', help='Assets file.')
def stage2(assets):
    main(Procedure.Stage2, assets)

@click.command()
@click.option('--assets', default='assets.csv', help='Assets file.')
@click.option('--cmd', help='Custom command.')
def run(assets, cmd):
    main(Procedure.Cmd, assets, cmd)

@click.command()
@click.option('--assets', default='assets.csv', help='Assets file.')
def clean(assets):
    main(Procedure.Clean, assets)

cli.add_command(stage1)
cli.add_command(stage2)
cli.add_command(run)
cli.add_command(clean)

def main(stage, assets, cmd = None):

    # Make sure that we have assets.csv.
    if not os.path.exists(assets):
        print('Assets path does not exists.')
        return

    # Create logs directory at current path.
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    nodes_list = []

    with open(assets, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)
            nodes_list.append(row)

    while len(nodes_list):
        node_part = nodes_list[0:10]

        for ip, passwd, address, wallet_passwd in node_part:
            # Do something here.
            if stage == Procedure.Stage1:
                ssh_stage1(ip, passwd, wallet_passwd)
            elif stage == Procedure.Stage2:
                ssh_stage2(ip, passwd, address, wallet_passwd)
            elif stage == Procedure.Clean:
                ssh_clean(ip, passwd)
            elif stage == Procedure.Cmd:
                ssh_cmd(ip, passwd, cmd)
            else:
                pass

        del nodes_list[0:10]


if __name__ == '__main__':
    cli()
