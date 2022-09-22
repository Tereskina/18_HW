# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from flask import request


from dao.model.schema import MovieSchema
from implemented import movie_dao


movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)
movie_schema_one = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Get all movies
        """
        if len(request.args) > 0:
            return movie_schema.dump(movie_dao.get_movies_by_many_filters(
                **request.args)
            )
        else:
            return movie_schema.dump(movie_dao.get_all_movies()), 200


    def post(self):
        """
        Create a movie
        """
        # Метод, который положит запись в БД
        if movie_dao.create(**request.json):

            return "", 201
        else:
            return "", 503



@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id: int):
        """
        Get movie by id
        """
        # Метод, который достанет из БД все сущности по id
        return movie_schema.dump([movie_dao.get_movie_by_movie_id(movie_id)]), 200

    def put(self, movie_id: int):
        """
        Add movie to db
        """
        movie_dao.update(**request.json)
        return "", 201

    def delete(self, movie_id: int):
        """
        Delete movie
        """
        movie_dao.delete(movie_id)

        return "", 204
