'''协程实现异步-版本3

版本二中有个问题：版本1/2中都使用了全局变量gen，需要将它去掉，通过修改装饰器来实现。
'''


import threading
import time


def genCoroutine(func):
    def wrapper(*args, **kwargs):
        gen1 = func()   # 获取reqA的生成器对象
        gen2 = next(gen1)   # 获取longIo的生成器对象

        def run(g):
            res = next(g)
            try:
                gen1.send(res)  # 返回数据给reqA
            except StopIteration as e:
                pass
        threading.Thread(target=run, args=(gen2,)).start()
    return wrapper


def longIo():
    '''模拟耗时操作'''

    print('开始耗时操作')
    time.sleep(5)
    print('结束耗时操作')

    yield 'joy is a good boy'


@genCoroutine
def reqA():
    print('开始处理reqA')
    res = yield longIo()
    print('接收到longIo的响应数据：', res)
    print('结束处理reqA')


def reqB():
    print('开始处理reqB')
    time.sleep(2)
    print('结束处理reqB')


def main():
    # global gen
    # gen = reqA()
    # next(gen)

    reqA()
    reqB()

    while True:
        time.sleep(1)
        pass


if __name__ == '__main__':
    main()
