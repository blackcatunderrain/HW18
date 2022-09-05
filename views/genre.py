# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

genre_ns = Namespace('genre')


@genre_ns.route('/')
@genre_ns.param('director_id')
@genre_ns.param('genre_id')
@genre_ns.param('year')
class GenreView(Resource):
    def get(self):
        """Get all genre"""

        return "", 200

    def post(self):
        """Add a new genre"""
        return "", 201


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
        """Get all genre by id"""

        return "", 200

    def put(self, genre_id: int):
        """Add a new genre"""
        return "", 201

    def delete(self, genre_id: int):
        """Delete by id"""
        return "", 200
