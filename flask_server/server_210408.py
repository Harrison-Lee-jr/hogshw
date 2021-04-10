from flask import Flask
from flask_restful import Resource,Api
from flask import request

app=Flask(__name__)
api=Api(app)
app.config['testcase']=[]

class TestCaseServer(Resource):
    # 定义get方法
    def get(self):
        # get请求的参数
        print(request.args)
        if 'id' in request.args:
            # 从用例库中找对应的用例
            for i in app.config['testcase']:
                # 返回用例
                if i['id']==int(request.args['id']):
                    return i
        else:
            return app.config['testcase']
    # 定义post方法
    def post(self):
        # post请求的参数
        print(request.json)
        # 每条testcase要有ID，description，steps
        if 'id' not in request.json:
            return {'result':'error','errcode':'404','errmessage':'need testcase id'}
        app.config['testcase'].append(request.json)
        return {'result':'ok','errcode':'0'}

api.add_resource(TestCaseServer,'/testcase')

if __name__=='__main__':
    app.run(debug=True)
    # 开启debug模式，运行的情况实时反馈到服务中