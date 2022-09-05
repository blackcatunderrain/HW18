
from dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_director_byid(self, id: int):
        return self.session.query(Director).filter(Director.id == id).one()
