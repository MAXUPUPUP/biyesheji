# 编程课实验报告辅助评阅系统。
## 目前是非常不成熟的项目，等9月或者年底拿到东大的offer，我会再更新。
经历了前前后后20多天的开发，本项目终于以一种奇怪的方式跑起来了。但是由于当时实在是被托福折磨的十分痛苦，项目只能算一个残缺品。与最开始的架构有很大的出入，有许多功能没有实现。作为自己的本科毕设，还是有很多遗憾的。
下面介绍一下开发环境和项目部署：
1. 本项目全程在pycharm上开发
2. 在开始配置之前最好下载Anaconda维护Python环境。

1. 下载Python3.11， 并且配置在环境变量中。
2. conda active base
3. pip install django
4. pip install requests
5. pip install dashscope
6. pip install python-docx
7. ...缺什么模块就补什么模块
8. python manage.py runserver

http://127.0.0.1:8000/user/login/ 前端
http://127.0.0.1:8000/admin/  管理员界面 anteng tianshen
api-key = “需要自己配置”.