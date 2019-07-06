#!/usr/bin/env python3

import sys
import os
import stat
import getpass

# 要添加的DNS：用于下载github文件的dns，来源于：https://www.ipaddress.com/
HOST_GITHUB = ["#GITHUB1",
               "192.30.253.113    github.com",
               "151.101.185.194   github.global.ssl.fastly.net",
               "192.30.253.120    codeload.github.com"]


# 在host中搜索内容
def search_host(host_value, host_path):
    search_content = '\n' + '\n'.join(host_value) + '\n'
    f = open(host_path, 'r')
    lines = f.readlines()
    f.close()
    # 读取出来的each_line中每一行字符串都包含'\n'，所以连接时不需要再使用'\n'进行连接
    return search_content in ''.join(lines)


# 查看host所有内容
def show_host(host_path):
    f = open(host_path, 'r')
    all_content = ''.join(f.readlines())
    f.close()
    print(all_content)


# 在host中追加指定内容
def write_host(host_value, host_path):
    output = open(host_path, 'a')
    output.write('\n' + '\n'.join(host_value) + '\n')
    output.close()


# 在host中删除指定内容
def remove_host(host_value, host_path):
    need_remove = '\n' + '\n'.join(host_value) + '\n'
    f = open(host_path, 'r')
    hosts_new_content = ''.join(f.readlines()).replace(need_remove, '')
    f.close()
    output = open(host_path, 'w')
    output.write(hosts_new_content)
    output.close()


# 权限rwxrwxrwx
def chmod777(host_path):
    os.chmod(host_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)


# 权限rw-r--r--
def chmod644(host_path):
    os.chmod(host_path, stat.S_IRUSR + stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":

    # 获取当前用户
    user = getpass.getuser()
    # 确定hosts文件路径
    if sys.platform == "linux":
        # ubuntu hosts文件位置
        host_path = r'/etc/hosts'

    if user == 'root':
        # 修改hosts文件权限
        chmod777(host_path)

        if search_host(HOST_GITHUB, host_path):
            print("HOSTS文件中GITHUB相关的DNS记录已经存在...")
        else:
            write_host(HOST_GITHUB, host_path)
            print('已经成功向HOSTS文件中写入GITHUB相关的DNS记录...')

        remove_host(HOST_GITHUB, host_path)
        print('已经成功从HOSTS文件中删除GITHUB相关的DNS记录...')

        # 查看HOSTS文件中当前的DNS记录
        # show_host(host_path)

        # 恢复hosts文件权限
        chmod644(host_path)

    else:
        print('[执行失败]>>>请以root用户执行当前脚本')
