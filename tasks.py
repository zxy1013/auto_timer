# -*-coding:utf-8-*-
# @ Auth:zhao xy
# @ Time:2021/5/7 20:48
# @ File:tasks.py


# 创建celery task
# 导入app对象
import time
from app import app
from celery import Celery

# 创建celery对象，其中broker设置为app.config['CELERY_BROKER_URL']
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
# Celery其它任何配置都可以直接用celery.conf.update()通过Flask的配置直接传递
# celery.conf.update(app.config)
# 设置结果过期时间为60s
celery.conf.update(result_expires=600)

# 表明该函数是一个celery task
@celery.task
def celery_task_count(num):
    # 需要传入上下文 在celery下打印
    with app.app_context():
        print("celery get num:{}".format(num))
        time.sleep(5)
        print("celery end.")

@celery.task
def my_background_task(arg1, arg2):
    # 两数相加
    time.sleep(10)
    return arg1 + arg2