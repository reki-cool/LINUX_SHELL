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