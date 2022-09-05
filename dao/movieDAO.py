
from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movie_byid(self, id: int):
        return self.session.query(Movie).filter(Movie.id == id).one()

    def get_movie_by_director_id(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id).one()

    def get_movie_by_genre_id(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).one()

    def get_movie_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year).one()

    def create(self, **kwargs):
        try:
            self.session.add(
                Movie(
                    **kwargs
                )
            )
            self.session.commit()
        except Exception as e:
            print("Error creating Movie: %s" % e)
            self.session.rollback()

    def update(self, **kwargs):
        try:
            self.session.query(Movie).filter(Movie.id == kwargs.get('id')).update(**kwargs)
            self.session.commit()
        except Exception as e:
            print("Error updating Movie: %s" % e)
            self.session.rollback()

    def delete(self, id: int):
        try:
            self.session.query(Movie).filter(Movie.id == id).delete()
            self.session.commit()
        except Exception as e:
            print("Error delete Movie: %s" % e)
            self.session.rollback()






