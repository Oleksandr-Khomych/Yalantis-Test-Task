# -*- coding: utf-8 -*-

from app import app, api
from catalog_api.models import db
from catalog_api import views


api.add_resource(views.CreateCourse, '/create')
api.add_resource(views.Catalog, '/catalog')
api.add_resource(views.Course, '/course/<string:course_id>')
api.add_resource(views.FindCourse, '/search')
api.add_resource(views.Home, '/')


if __name__ == '__main__':
    db.create_all()
    app.run()
