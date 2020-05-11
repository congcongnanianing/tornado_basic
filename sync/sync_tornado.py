'''同步'''

import tornado.web
import tornado.ioloop
import tornado.httpclient

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 获取查询参数q的值
        q = self.get_argument('q')
        client = tornado.httpclient.HTTPClient()
        resp = client.fetch('https://cn.bing.com/search?q=%s' % q)
        print(resp)
        self.write('查询成功')


def make_app():
    return tornado.web.Application(handlers=[
        (r'/sync/', IndexHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
