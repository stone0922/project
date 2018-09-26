import multiprocessing as mp
from time import sleep

a = 1

def fun():
    sleep(3)
    global a  # 全局还是在子进程中
    print('a=',a)
    a = 10000
    print('这是子进程')

# 创建进程对象
p = mp.Process(target = fun)

# 启动进程
p.start()

sleep(2)
print('这是父进程')
# 回收子进程
p.join(5)

print('parent a= ',a)
while True:
    pass