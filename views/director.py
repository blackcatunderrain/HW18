# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
@director_ns.param('director_id')
@director_ns.param('director_id')
@director_ns.param('year')
class DirectorView(Resource):
    def get(self):
        """Get all director"""

        return "", 200

    def post(self):
        """Add a new director"""
        return "", 201


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        """Get all director by id"""

        return "", 200

    def put(self, director_id: int):
        """Add a new director"""
        return "", 201

    def delete(self, director_id: int):
        """Delete by id"""
        return "", 200
