'''协程实现异步-版本1'''


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
    start_time = time.time()

    global gen
    gen = reqA()
    next(gen)
    # reqA()
    reqB()

    end_time = time.time()
    print(start_time)
    print(end_time)
    print('耗时：%s' % (end_time - start_time))
    while True:
        time.sleep(1)
        pass


if __name__ == '__main__':
    main()
