'''回调函数 实现异步'''

import tornado.web
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient

import certifi

AsyncHTTPClient.configure(None, defaults=dict(ca_certs=certifi.where()))


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous   # 不关闭通信通道
    def get(self):
        q = self.get_argument('q')
        client = AsyncHTTPClient()
        client.fetch('https://cn.bing.com/search?q=%s' % q, self.on_response)

        self.write('查询成功')

    def on_response(self, response):
        print(response)
        self.write('回调函数执行')
        # 回调函数执行之后结束跟服务器的连接
        self.finish()


def make_app():
    return tornado.web.Application(handlers=[
        (r'/async/', IndexHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
