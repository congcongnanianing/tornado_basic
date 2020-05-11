from datetime import datetime, timedelta
from typing import Optional, Awaitable

import pymysql
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

# 定义默认启动的监听端口为：8888
define('port', default=8888, type=int)


# 执行方法类，需要继承自 tornado.web.RequestHandler
class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        # name = self.get_argument('name')
        # name = self.get_query_argument('name')

        self.write('hello tornado')

    def post(self):
        name = self.get_argument('name')
        name = self.get_body_argument('name')

        self.write('tornado post')


class ResHandler(tornado.web.RequestHandler):

    def get(self):
        # 设置响应状态码，一般不用它
        self.set_status(200)
        self.set_cookie('token', '123456', expires_days=1)
        end_time = datetime.now() + timedelta(days=2)
        self.set_cookie('token_123', '66666', expires=end_time)

        # self.clear_cookie('token')
        self.clear_all_cookies()

        self.write('<h2>祝我拿下高薪Offer</h2>')

        # 重定向
        self.redirect('/')


class DaysHandler(tornado.web.RequestHandler):
    def get(self, year, month, day):
        self.write('{}年{}月{}日'.format(year, month, day))


class Days_Handler(tornado.web.RequestHandler):
    def get(self, month, year, day):
        self.write('{}年{}月{}日'.format(year, month, day))


# 切入点函数
class EntryHandler(tornado.web.RequestHandler):

    def initialize(self):
        print('_initialize')
        self.conn = pymysql.Connection(host='localhost', port=3306, user='root', password='root', database='ihome')
        self.cursor = self.conn.cursor()

    def prepare(self):
        print('prepare')

    def get(self):
        print('get')
        sql = 'select * from ih_area_info;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)

        self.write('查询所有信息成功')

    def on_finish(self):
        print('on_finish')
        self.conn.close()


def make_app():
    return tornado.web.Application(handlers=[
        # handlers 参数中定义路由匹配地址
        (r'/', MainHandler),
        (r'/res/', ResHandler),
        (r'/days/(\d{4})/(\d{2})/(\d{2})/', DaysHandler),
        (r'/days2/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/', Days_Handler),
        (r'/entry/', EntryHandler)
    ])


if __name__ == '__main__':
    # 解析启动命令（解析命令行中参数），python xxx.py --port=端口号
    parse_command_line()

    app = make_app()
    # 监听端口，options.port获取命令行中的参数port
    app.listen(options.port)

    # 监听启动的IO实例
    tornado.ioloop.IOLoop.current().start()
