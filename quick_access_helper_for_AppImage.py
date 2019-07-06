#!/usr/bin/env python3

import sys
import os
import stat
import getpass
import getopt

"""
脚本目标：
    习惯于在终端打开app或者关闭app的玩家，可能很需要这个脚本
    桌面上导航栏比较短不可能放置过多的图标，所以就有了这个脚本
    帮你根据你喜欢的名字在/usr/local/bin下快速创建一个用于开启应用和一个用于关闭应用的软链接
    这个软链接就像个桌面上的快捷方式
    当你需要打开或者关闭它时，你只需要快速打开终端，然后输入你对这个app的命名或者对应的killer的命名
脚本前置条件：
    需要使用root用户执行此脚本
    需要系统已经安装screen命令
    本脚本使用python3执行
脚本参考：
    创建软链接参考：https://www.runoob.com/python/os-symlink.html
    路径拼接参考：https://blog.csdn.net/qq_42034590/article/details/80031241
    两种引号都有的情况参考：https://blog.csdn.net/linshenwei1995/article/details/78987444
    python获取命令行输入参数列表参考：https://blog.csdn.net/Lv_Victor/article/details/70699497
"""

# 软链接存放的文件夹路径
link_dir = ''
# 当前AppImage文件存放的文件夹路径
app_dir = ''
# AppImage文件名
app_name = ''
# 软链接名称=>我喜欢的名字
link_name = ''


# 权限rwxrwxrwx
def chmod777(host_path):
    os.chmod(host_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)


def write_file(file, content):
    output = open(file, 'w')
    output.write(content)
    output.close()


if __name__ == "__main__":

    # 获取脚本参数
    opts, args = getopt.getopt(sys.argv[1:], 'L:A:a:l:', ['link_dir=', 'app_dir=', 'app_name=', 'link_name='])
    for opt, arg in opts:
        if opt in ['-L', '--link_dir']:
            link_dir = arg
        elif opt in ['-A', '--app_dir']:
            app_dir = arg
        elif opt in ['-a', '--app_name']:
            app_name = arg
        elif opt in ['-l', '--link_name']:
            link_name = arg


    # 获取当前用户
    user = getpass.getuser()
    if user == 'root':
        if len(args) != 4:
            link_dir_temp = input('请输入目标可执行程序路径[例如/usr/local/bin]：')
            app_dir = input('请输入AppImage存放位置[例如/home/duyanhan/soft_app]：')
            app_name = input('请输入AppImage的名称[例如test.AppImage]：')
            link_name = input('请输入最终要执行的命令名称[用于启动此AppImage，例如test]：')
        # 创建link_name+'.sh'的文件在app_dir路径下面
        starter_sh = os.path.join(app_dir, link_name + '.sh')
        # 写入内容
        starter_content = '\n'.join([
            r'#!/bin/bash',
            r'work_path=$(dirname $(readlink -f $0))',
            r'screen -dmS ' + link_name + ' ${work_path}/' + app_name
        ])
        write_file(starter_sh, starter_content)
        # 授权
        chmod777(starter_sh)
        # 创建软链接
        os.symlink(starter_sh, os.path.join(link_dir, link_name))

        # 创建link_name+'killer.sh'的文件在app_dir路径下面
        killer_sh = os.path.join(app_dir, link_name + 'killer.sh')
        # 写入内容
        killer_content = '\n'.join([
            r'#!/bin/bash',
            '$(kill -9 $(screen -ls | grep .' + link_name + ' | awk -F "." \'{print $1}\')) >> /dev/null 2>&1 '
                                                            '&& $(screen -wipe) >> /dev/null 2>&1'
        ])
        write_file(killer_sh, killer_content)
        # 授权
        chmod777(killer_sh)
        # 创建软链接
        os.symlink(killer_sh, os.path.join(link_dir, link_name + 'killer'))
    else:
        print('[执行失败]>>>请以root用户执行当前脚本')
