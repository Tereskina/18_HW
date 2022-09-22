# файл для создания DAO, чтобы импортировать их везде
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from setup_db import db

movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
