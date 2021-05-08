# -*-coding:utf-8-*-
# @ Auth:zhao xy
# @ Time:2021/5/7 18:44
# @ File:timer.py

# 定时器(Timer)简单实现
# 其原理为执行函数中置定时函数Timer()，递归调用自己。

# import threading
# import time
#
# exec_count = 0
# def heartbeat():
#     print(time.strftime('%Y-%m-%d %H:%M:%S'))
#     global exec_count
#     exec_count += 1
#     # 15秒后停止定时器
#     if exec_count < 15:
#         threading.Timer(1, heartbeat).start()
#         # Call a function after a specified number of seconds
# 	    # 第一个参数表示多长时间后调用第二个参数指明的函数。
# heartbeat()



# import threading
# import time
#
# cancel_tmr = False
# def heart_beat():
#     print(time.strftime('%Y-%m-%d %H:%M:%S'))
#     if not cancel_tmr:
#         threading.Timer(1, heart_beat).start()
#
# heart_beat()
# # 15秒后停止定时器
# time.sleep(15)
# cancel_tmr = True



import threading
import time

def fun_timer():
    print('Hello Timer!')
    global timer
    timer = threading.Timer(2, fun_timer)
    timer.start()

timer = threading.Timer(1, fun_timer)
timer.start()
time.sleep(10) # 10秒后停止定时器
timer.cancel()
# Stop the timer if it hasn't finished yet