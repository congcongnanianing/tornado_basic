'''回调函数实现异步'''

import threading
import time


def longIo(callback):
    '''模拟耗时操作'''

    def run(cb):
        print('开始耗时操作')
        time.sleep(5)
        print('结束耗时操作')
        cb('jpy is a good boy')
    # 开辟线程执行耗时操作
    threading.Thread(target=run, args=(callback,)).start()


def on_finish(data):
    print('开始执行回调函数')
    print('接收到longIo响应数据：', data)
    print('结束执行回调函数')


def reqA():
    print('开始处理reqA')
    longIo(on_finish)
    print('结束处理reqA')


def reqB():
    print('开始处理reqB')
    time.sleep(2)
    print('结束处理reqB')


def main():
    start_time = time.time()
    reqA()
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
