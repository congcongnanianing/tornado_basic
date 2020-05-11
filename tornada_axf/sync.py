import time


def reqA():
    print('开始处理reqA')
    time.sleep(5)
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
    # start_time = time.time()
    main()
    # end_time = time.time()
    # print(start_time)
    # print(end_time)
    # print('耗时：%s' % (end_time - start_time))
