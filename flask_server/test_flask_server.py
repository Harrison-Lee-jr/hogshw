import os.path
from flask import Flask
from flask_restful import Resource, Api, abort
from flask import request
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://tmp:miaomiao.com@127.0.0.1:3306/tmp?charset=utf8mb4'
db = SQLAlchemy(app)
app.config['testcase']=[]

class TestCase(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    # 描述字段不唯一，可空
    description = db.Column(db.String(80), unique=False, nullable=True)
    file_name = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(300), unique=False, nullable=True)
    report=db.relationship('Report',backref='test_case',lazy=True)
    def __repr__(self):
        return '<TestCase %r>' % self.name
# 新建allure报告表
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 描述字段不唯一，可空
    description = db.Column(db.String(80), unique=False, nullable=True)
    dir = db.Column(db.String(300), unique=False, nullable=True)
    testcase_id=db.Column(db.String(80),db.ForeignKey('test_case.name'),nullable=False)

    def __repr__(self):
        return '<Report %r>' % self.id

class TestCaseStore(Resource):
    # 定义post方法
    def post(self):
        if 'file' in request.files and 'name' in request.form:
            # 取出post请求中含'file'的文件流
            f=request.files['file']
            name=request.form['name']
            file_name=f.filename
            # 转成字节流
            content=f.read()
            # 改造：文件用例，存到数据库时，也存入name值
            testcase=TestCase(name=name,file_name=file_name,content=content)
            db.session.add(testcase)
            db.session.commit()
            return 'ok'
        abort(404)

@app.route('/get_testcase',methods=['get'])
def run_testcase():
    if 'name' in request.args:
        # 通过name，指定要运行的用例
        name=request.args['name']
        # 从数据库中取出，以name为筛选取出第一条
        testcase=TestCase.query.filter_by(name=name).first()
        return testcase.content
    abort(404)

@app.route('/run',methods=['get'])
def run():
    if 'name' in request.args:
        name=request.args['name']
        testcase = TestCase.query.filter_by(name=name).first()
        J = Jenkins('http://127.0.0.1:7005/', username='admin', password='111f54f88fb0e03fd53e61b43fd8e9db05')
        # 打印看有多少个job
        # print(J.keys())
        J['tmp_test'].invoke(build_params={'name': name, 'file_name': testcase.file_name})
        return 'ok'
@app.route("/report_upload",methods=['post'])
def report_upload():
    if 'file' in request.files and 'name' in request.form:
        DIR=r'/Users/jinronglee/jenkins/workspace/tmp_test'
        f=request.files['file']
        name=request.form['name']
        file_name=f.filename
        dir = os.path.join(DIR , file_name)
        f.save(dir)
        report=Report(dir=dir,testcase_id=name)
        db.session.add(report)
        db.session.commit()
        return 'ok'

api.add_resource(TestCaseStore,'/store')

if __name__=='__main__':
    app.run(debug=True)
    # db.drop_all()
    # db.create_all()
