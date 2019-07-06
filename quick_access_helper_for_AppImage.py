#!/usr/bin/env python3

import sys
import os
import stat
import getpass

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
"""

# 软链接存放的文件夹路径
link_dir = r'/usr/local/bin'
# 当前AppImage文件存放的文件夹路径
app_dir = r'/home/duyanhan/soft_app'
# AppImage文件名
app_name = r'VNote-2.7.1-x86_64.AppImage'
# 软链接名称=>我喜欢的名字
link_name = r'vnote'

if __name__ == "__main__":

    # 获取当前用户
    user = getpass.getuser()
    if user == 'root':
        link_dir_temp = input('请输入目标可执行程序路径[默认为' + link_dir + ']：')
        if len(link_dir_temp) != 0:
            link_dir = link_dir_temp
        app_dir = input('请输入AppImage存放位置[必填]：')
        app_name = input('请输入AppImage的名称[必填]：')
        link_name = input('请输入最终要执行的命令名称[用于启动此AppImage，必填]：')



    else:
        print('[执行失败]>>>请以root用户执行当前脚本')
