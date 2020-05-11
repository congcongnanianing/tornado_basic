import tornado.web

from tornado_face.face.models import init_db, User
from tornado_face.utils.conn import session
from tornado_face.utils.faceId import face_register


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register_1.html')

    def post(self):
        face_img = self.get_argument('face_img')
        print(face_img)
        # 取出图片到data信息
        face = face_img.split(',')[-1]
        username = self.get_argument("username")
        realname = self.get_argument("realname")

        if not all([face_img, username, realname]):
            errmsg = '参数不完整'
            self.render('register_1.html', errmsg=errmsg)
        else:
            # 注册用户模型
            user = User(username=username, realname=realname)

            # 调用百度人脸注册接口
            res = face_register(face, user.id)
            if res:
                session.add(user)
                session.commit()
                # 注册成功，跳转到登录页面
                self.redirect('/login/')
            else:
                self.redirect('/register/')


class InitDbHandler(tornado.web.RequestHandler):
    def get(self):
        init_db()
        self.write('模型创建成功')


class LoginbHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login_1.html')

    def post(self):
        pass