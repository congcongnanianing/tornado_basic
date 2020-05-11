'''协程 实现异步'''

# todo 可以将get方法中耗时操作单独封装成一个方法（也用到装饰器）

import tornado.web
import tornado.ioloop
# import tornado.httpclient
from tornado.httpclient import AsyncHTTPClient

import certifi

AsyncHTTPClient.configure(None, defaults=dict(ca_certs=certifi.where()))


class IndexHandler(tornado.web.RequestHandler):
    # @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        q = self.get_argument('q')
        url = 'https://cn.bing.com/search?q=%s' % q
        client = AsyncHTTPClient()
        resp = yield client.fetch(url)
        print(resp)
        self.write('异步测试2成功')


def make_app():
    return tornado.web.Application(handlers=[
        (r'/async2/', IndexHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
