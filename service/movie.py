from dao.model.models import Movie
from dao.movieDAO import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list[Movie]:
        return self.movie_dao.get_all_movies()

    def get_movie_by(self, id, director_id=None, genre_id=None, year=None):
        if director_id is not None and genre_id is not None and year is not None:
            return self.movie_dao.get_movie_by_many_filters(
                director_id=director_id, genre_id=genre_id, year=year
            )

        if director_id is not None:
            return self.movie_dao.get_movie_by_director_id(director_id)
        elif genre_id is not None:
            return self.movie_dao.get_movie_by_genre_id(genre_id)
        elif year is not None:
            return self.movie_dao.get_movie_by_year(year)

        else:
            return []

    def add_film(self, data) -> None:
        self.movie_dao.create(**data)

    def update_film(self, data) -> None:
        self.movie_dao.update(**data)

    def delete_film_by_id(self, id) -> None:
        self.movie_dao.delete(id)