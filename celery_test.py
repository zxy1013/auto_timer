# -*-coding:utf-8-*-
# @ Auth:zhao xy
# @ Time:2021/5/7 19:57
# @ File:celery_test.py

# python 使用 celery
from celery import Celery
# tasks是给app起的名字
app = Celery('tasks',
             broker='redis://localhost',
             backend='redis://localhost') # backend 将结果写入redis
@app.task # 这是worker可以执行的任务
def add(x, y):
	print("running...", x, y)
	return x + y
@app.task
def cmd(cmdstr):
	print(cmdstr)

'''
cmd下启动redis
D:\wendang\redis>redis-server.exe redis.windows.conf

terminal下启动celery
celery -A celery_test worker --loglevel=info

terminal下输入
python
from celery_test import add
# 发给远程执行
t1 = add.delay(4, 4)
t1.get() # 拿取执行结果，没有返回就阻塞
'''