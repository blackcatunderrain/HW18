from dao.model.models import Director
from dao.directorDAO import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> list[Director]:
        return self.director_dao.get_all_directors()

    def get_director_by(self, id):
        return self.director_dao.get_director_byid(id)




