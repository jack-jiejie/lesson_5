__author__ = "yzj"
__data__ = "2020/4/12 14:10"

# from flask import Flask
# import flask_restful as restful
# # from flask.ext import restful
#
# # 实例化一个flask对象，用来启动
# app = Flask(__name__)
# api = restful.Api(app)
#
# class HelloWorld(restful.Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# api.add_resource(HelloWorld, '/')
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request
# from flask.ext.restful import Resource, Api
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {
    "todo2": "我想去打球"
}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class Todo1(Resource):
    def get(self):
        return {"do_something": "唱歌"}

class Todo2(Resource):
    def get(self):
        return {"task": "攻占日本岛"}, 200
# '/<string:todo_id>'是url地址
api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Todo1, '/1', '/1/')
api.add_resource(Todo2, '/2')

if __name__ == '__main__':
    app.run(debug=True)




