from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api, reqparse, inputs
import models


# resource for a list of courses
class CourseList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title is provided',
            location=['form','json'])
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course url is provided.',
            location=['form', 'json'],
            type=inputs.url)
        # ensure the standard setup happens
        super().__init__()
    
    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}]})
    
    def post(self):
        args = self.reqparse.args()
        models.Course.create(**args)
        return jsonify({'courses': [{'title': 'Python Basics'}]})

class Course(Resource):
    def __init__():
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title is provided',
            location=['form','json'])
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course url is provided.',
            location=['form', 'json'],
            type=inputs.url)
        # ensure the standard setup happens
        super().__init__()
        
    def get(self, id):
        return jsonify({'title': 'Python Basics'})
    
    def put(self, id):
        return jsonify({'title': 'Python Basics'})
    
    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

# treat this file with this namespace and path as being another thing
courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(
    CourseList,
    '/api/v1/courses',
    endpoint='courses'
)
api.add_resource(
    Course,
    '/api/v1/courses/<int:id>',
    endpoint='course'
)
