import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

from app.views import IndexHandler, DbHandler, StuHandler, StusHandler

define('port', default=8888, type=int)


def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', IndexHandler),
        (r'/init_db/', DbHandler),
        (r'/stu/', StuHandler),
        (r'/stus/', StusHandler),
    ])


if __name__ == '__main__':
    parse_command_line()

    app = make_app()

    app.listen(options.port)

    tornado.ioloop.IOLoop.current().start()
