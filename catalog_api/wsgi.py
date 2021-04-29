# -*- coding: utf-8 -*-

from app import app, api, db
from models import Course
import views


api.add_resource(views.CreateCourse, '/create')
api.add_resource(views.Catalog, '/<string:todo_id>')


if __name__ == '__main__':
    db.create_all()
    app.run()
