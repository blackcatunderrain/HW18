# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace
from dao.model.schema import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        """Get all director"""
        return director_schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        """Get all director by id"""
        return director_schema.dump([director_service.get_director_by(director_id)]), 200


