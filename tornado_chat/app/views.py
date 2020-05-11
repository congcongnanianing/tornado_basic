import tornado.web
import tornado.websocket


class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        errmsg = ''
        self.render('login_1.html', errmsg=errmsg)

    def post(self):

        username = self.get_argument('username')
        password = self.get_body_argument('password')

        if username in['joy', 'boby'] and password == '123456':
            self.set_cookie('username', username)
            self.render('chat.html', username=username)
        else:
            errmsg = '账号或密码错误'
            self.render('login_1.html', errmsg=errmsg)


class ChatHandler(tornado.websocket.WebSocketHandler):
    # 存储所有用户信息
    user_online = list()

    # 当进入chat.html页面时, 会主动触发该函数
    def open(self, *args, **kwargs):
        self.user_online.append(self)
        for user in self.user_online:
            username = self.get_cookie('username')
            user.write_message('系统提示：【%s】已进入聊天室' % username)

    def on_message(self, message):
        username = self.get_cookie('username')
        for user in self.user_online:
            user.write_message('%s:%s' % (username, message))

    def on_close(self):
        self.user_online.remove(self)
        username = self.get_cookie('username')
        for user in self.user_online:
            user.write_message('系统提示：【%s已退出群聊】' % username)
