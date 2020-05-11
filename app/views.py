import tornado.web

from app.models import create_db, Student
from utils.conn import session


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('tornado index')


class DbHandler(tornado.web.RequestHandler):
    def get(self):
        create_db()
        self.write('创建表成功')


class StuHandler(tornado.web.RequestHandler):
    def post(self):
        stu = Student()
        stu.s_name = '小米'
        session.add(stu)
        session.commit()
        self.write('添加数据成功')


class StusHandler(tornado.web.RequestHandler):

    def get(self):
        stus = session.query(Student).filter(Student.s_name == 'xiaomi_0').all()
        print(stus)
        self.write('查询成功')

    def post(self):
        stu_list = list()
        for i in range(10):
            stu = Student()
            stu.s_name = 'xiaomi_%s' % i
            stu_list.append(stu)
        session.add_all(stu_list)
        session.commit()
        self.write('新增多条数据成功')

    def delete(self):
        # 删除方式一：session.delete()
        stu = session.query(Student).filter(Student.s_name == 'xiaomi_9').first()
        if stu:
            session.delete(stu)
            session.commit()
        # 删除方式二：delete()方法
        session.query(Student).filter(Student.s_name == 'xiaomi_8').delete()
        session.commit()
        self.write('删除成功')

    # 对部分属性修改
    def patch(self):
        # 修改方式一：
        # stu = session.query(Student).filter(Student.s_name == 'xiaomi_1').first()
        # stu.s_name = 'huawei'
        # session.add(stu)
        # session.commit()

        # 修改方式二：update()
        session.query(Student).filter(Student.s_name == 'xiaomi_2').update({'s_name': 'zhongxin'})
        session.commit()

        self.write('修改成功')
