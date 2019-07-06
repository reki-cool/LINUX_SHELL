## 脚本简介

### hosts_for_github.py
#### 脚本作用：
用于向hosts文件中追加三条记录，以解决下载github资源速度慢的问题
#### 执行条件：
使用root用户执行
#### 补充：
如果没有生效，还需要重启一下网络  
```sudo /etc/init.d/networking restart```  
如果还是不行，需要通过代理解决
#### 相关：
这里是下载资源的加速办法，不一定有效；  
对应的有一个加速github页面访问的项目值得参考：https://github.com/dbarobin/github

---
### quick_access_helper_for_AppImage.py
 - 脚本目标：  
    习惯于在终端打开app或者关闭app的玩家，可能很需要这个脚本  
    桌面上导航栏比较短不可能放置过多的图标，所以就有了这个脚本  
    帮你根据你喜欢的名字在/usr/local/bin下快速创建一个用于开启应用和一个用于关闭应用的软链接  
    这个软链接就像个桌面上的快捷方式  
    当你需要打开或者关闭它时，你只需要快速打开终端，然后输入你对这个app的命名或者对应的killer的命名    
 - 脚本前置条件：  
    需要使用root用户执行此脚本  
    需要系统已经安装screen命令  
    本脚本使用python3执行  
 - 脚本参考：  
    创建软链接参考：https://www.runoob.com/python/os-symlink.html  
    路径拼接参考：https://blog.csdn.net/qq_42034590/article/details/80031241  
    两种引号都有的情况参考：https://blog.csdn.net/linshenwei1995/article/details/78987444  
    python获取命令行输入参数列表参考：https://blog.csdn.net/Lv_Victor/article/details/70699497  
 - 脚本执行参考：  
    python3 ./quick_access_helper_for_AppImage.py -L /usr/local/bin -A /home/duyanhan/soft_app -a electron-ssr-0.2.6.AppImage -l myssr  
