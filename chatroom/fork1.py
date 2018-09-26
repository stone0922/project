# 创建二级子进程避免僵尸

import os
from time import sleep

def f1():
    sleep(3)
    print('first')

def f2():
    sleep(4)
    print('second')

pid = os.fork()

if pid < 0:
    print('error')
elif pid == 0:
    # 创建二级子进程
    p = os.fork()
    if p == 0:
        f2()  # 做f2
    else:
        os._exit(0)
else:
    os.wait()  # 等一级子进程退出
    f1()   # 做f1