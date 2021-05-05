from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(Configuration):
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    api = Api(app)

    import views as views
    api.add_resource(views.CreateCourse, '/create')
    api.add_resource(views.Catalog, '/catalog')
    api.add_resource(views.Course, '/course/<string:course_id>')
    api.add_resource(views.FindCourse, '/search')
    api.add_resource(views.Home, '/')

    return app
