# -*-coding:utf-8-*-
# @ Auth:zhao xy
# @ Time:2021/5/7 20:48
# @ File:app.py

from flask import Flask
# 从tasks导入需要异步操作的函数
from tasks import *


# 创建 Flask对象
app = Flask(__name__)
# borker_url  celey需要通过一个消息队列来启动worker来工作，这里用redis，也可以换成RabbitMQ
app.config[ 'CELERY_BROKER_URL' ] = 'redis://localhost:6379/0'
# backend选项只有在你要Celery任务的存储状态和运行结果的时候才是必须的
# 相当于需要从celery获取返回数据的时候才需要设置该字段
app.config[ 'CELERY_RESULT_BACKEND' ] = 'redis://localhost:6379/0'
# 将celery在redis内的结果保存时间设置为30s
# app.config['CELERY_TASK_RESULT_EXPIRES'] = 30


@app.route('/hello')
def hello_world():
    # 调用任务的delay函数来触发celery计算
    task = celery_task_count.delay(10)
    # 返回响应
    return 'Hello World!'

@app.route("/sum/<arg1>/<arg2>")
def sum_(arg1, arg2):
    # 发送任务到celery,并返回任务ID,后续可以根据此任务ID获取任务结果
    result = my_background_task.delay(int(arg1), int(arg2))
    return result.id

@app.route("/get_result/<result_id>")
def get_result(result_id):
    # 根据任务ID获取任务结果
    result = celery.AsyncResult(id=result_id)
    return str(result.get( ))

if __name__ == '__main__':
    # 启动flask web server
    app.run(debug=True, host='0.0.0.0', port='5000')


'''
cmd下启动redis
D:\wendang\redis>redis-server.exe redis.windows.conf

terminal下启动celery
celery -A tasks.celery worker -l info # 启动Celery worker，其中tasks.celery为worker对象

terminal下启动flask
python app.py

通过浏览器查看
127.0.0.1:5000/hello
127.0.0.1:5000/sum/3/4 得到任务id
127.0.0.1:5000/get_result/06a0c145-c0c6-48be-97a4-e82415c9dbae
'''