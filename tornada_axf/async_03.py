'''协程实现异步-版本2

版本一中有个问题：对于tornado服务器而言，reqA 和reqB 应该被同等调用（我们在main中调reqA的时候用了三行代码），
所以我们需要将reqA的方式改成跟reqB一样(通过装饰器实现)。
'''


import threading
import time


gen = None


def longIo():
    '''模拟耗时操作'''

    def run():
        print('开始耗时操作')
        time.sleep(5)
        try:
            global gen
            gen.send('joy is a good man')
        except StopIteration as e:
            pass
    # 开辟线程执行耗时操作
    threading.Thread(target=run).start()


def genCoroutine(func):
    def wrapper(*args, **kwargs):
        global gen
        gen = func()
        next(gen)
    return wrapper


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
