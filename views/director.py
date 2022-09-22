from flask_restx import Resource, Namespace

from implemented import director_dao
from dao.model.schema import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
        Get all directors
        """
        return director_schema.dump(director_dao.get_all_directors()), 200


@director_ns.route('/<int:director_id>')
class DirectorsView(Resource):
    def get(self, director_id: int):
        """
        Get director by id
        """
        return director_schema.dump([director_dao.get_director_by_director_id(director_id)]), 200


