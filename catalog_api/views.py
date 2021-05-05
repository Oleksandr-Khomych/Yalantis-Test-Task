from flask_restful import Resource, reqparse

import db_methods
from utils import transfer_date, validate_lectures_count, abort_if_course_doesnt_exist, validate_dates


class Home(Resource):
    def get(self):
        return {"message": "CatalogAPI home page"}


class CreateCourse(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('start_date', type=transfer_date, required=True)
        parser.add_argument('end_date', type=transfer_date, required=True)
        parser.add_argument('lectures_count', type=validate_lectures_count, required=True)
        args = parser.parse_args(strict=True)
        validate_dates(args["start_date"], args["end_date"])
        id_ = db_methods.add_course(args['name'], args['start_date'], args['end_date'], args['lectures_count'])
        return {"message": {'id': id_, 'name': args['name'], 'start_date': str(args['start_date']),
                            'end_date': str(args['end_date']), 'lectures_count': args['lectures_count']}}, 201


class Catalog(Resource):
    def get(self):
        courses = db_methods.get_all_course()
        courses_list = []
        for course in courses:
            courses_list.append({'id': course.id, 'name': course.name, 'lectures_count': course.lectures_count})
        return {"message": {"courses": courses_list}}, 200


class Course(Resource):
    def get(self, course_id):
        course = db_methods.get_course_by_id(course_id)
        if course:
            course_info = {'id': course.id, 'name': course.name, 'start_date': str(course.start_date),
                           'end_date': str(course.end_date), 'lectures_count': course.lectures_count}
            return {"message": {"course": course_info}}, 200
        else:
            return {"message": {"course": f"Course with id={course_id} not found"}}, 400

    def delete(self, course_id):
        abort_if_course_doesnt_exist(course_id)
        db_methods.delete_course_by_id(course_id)
        return {"message": {"delete": f"Course with id={course_id} successfully deleted!"}}, 200

    def patch(self, course_id):
        abort_if_course_doesnt_exist(course_id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('start_date', type=transfer_date)
        parser.add_argument('end_date', type=transfer_date)
        parser.add_argument('lectures_count', type=validate_lectures_count)
        args = parser.parse_args(strict=True)
        update_data = {}
        for key, value in args.items():
            if value:
                update_data[key] = value
        if len(update_data) == 0:
            return {"message": {"patch": "No arguments passed"}}, 400
        # --- ValidateDates
        start_date = args['start_date']
        end_date = args['end_date']
        course = db_methods.get_course_by_id(course_id)
        if start_date is None:
            start_date = course.start_date
        if end_date is None:
            end_date = course.end_date
        validate_dates(start_date, end_date)

        db_methods.update_course_info(course_id, update_data)
        course = db_methods.get_course_by_id(course_id)
        course_info = {'id': course.id, 'name': course.name, 'start_date': str(course.start_date),
                       'end_date': str(course.end_date), 'lectures_count': course.lectures_count}
        return {"message": {"course": course_info}}, 200


class FindCourse(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('start_date[gte]', type=transfer_date)
        parser.add_argument('start_date[lte]', type=transfer_date)
        parser.add_argument('end_date[gte]', type=transfer_date)
        parser.add_argument('end_date[lte]', type=transfer_date)

        args = parser.parse_args(strict=True)
        courses = db_methods.find_courses(args)
        courses_list = []
        for course in courses:
            courses_list.append({'id': course.id, 'name': course.name, 'start_date': str(course.start_date),
                                 'end_date': str(course.end_date), 'lectures_count': course.lectures_count})
        return {"message": {"courses": courses_list}}
