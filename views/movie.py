# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

from dao.model.schema import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movie')
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
@movies_ns.param('director_id')
@movies_ns.param('genre_id')
@movies_ns.param('year')
class MovieView(Resource):
    def get(self):
        """Get all movies"""
        return movies_schema.dump(movie_service.get_movies()), 200

    def post(self):
        """Add a new movie"""
        return "", 201


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        """Get all movies by id"""
        return movies_schema.dump([movie_service.get_movie_by(movie_id)]), 200

    def put(self, movie_id: int):
        """Add a new movie"""
        return "", 201

    def delete(self, movie_id: int):
        """Delete by id"""
        return "", 200
