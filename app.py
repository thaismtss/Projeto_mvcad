from flask import Flask, request
from flask_restful import Resource, Api
from pessoa import retorna_pessoas, insert_pessoa

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return 'hello World'

class Pessoa(Resource):
    def get(self):
        pessoa = retorna_pessoas()
        return pessoa


    def post(self):
        pessoa = request.json
        insert_pessoa(pessoa)
        return "Pessoa Inserida com sucesso!"


api.add_resource(HelloWorld, '/')
api.add_resource(Pessoa, '/pessoas')


if __name__ == "__main__":
    app.run(debug=True)