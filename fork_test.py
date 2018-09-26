import os
from time import sleep

pid = os.fork()

def f1():
    sleep(3)
    print('f1 over')

def f2():
    sleep(4)
    print('f2 over')

if pid < 0:
    print('error')
elif pid == 0:
    f1()
else:
    f2()