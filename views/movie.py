# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

movies_ns = Namespace('movie')


@movies_ns.route('/')
@movies_ns.param('director_id')
@movies_ns.param('genre_id')
@movies_ns.param('year')
class MovieView(Resource):
    def get(self):
        """Get all movies"""

        return "", 200

    def post(self):
        """Add a new movie"""
        return "", 201


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        """Get all movies by id"""

        return "", 200

    def put(self, movie_id: int):
        """Add a new movie"""
        return "", 201

    def delete(self, movie_id: int):
        """Delete by id"""
        return "", 200
