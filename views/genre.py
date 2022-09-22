from flask_restx import Resource, Namespace

from implemented import genre_dao
from dao.model.schema import GenreSchema


genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        Get all genres
        """
        return genre_schema.dump(genre_dao.get_all_genres()), 200


@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):
    def get(self, genre_id: int):
        """
        Get genre by id
        """
        return genre_schema.dump([genre_dao.get_genre_by_genre_id(genre_id)]), 200
    