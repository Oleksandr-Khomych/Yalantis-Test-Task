# -*- coding: utf-8 -*-

from app import app, api, db
from models import Course
import views


api.add_resource(views.CreateCourse, '/create')
api.add_resource(views.Catalog, '/catalog')
api.add_resource(views.Course, '/course/<string:course_id>')
api.add_resource(views.FindCourse, '/search')


if __name__ == '__main__':
    db.create_all()
    app.run()
