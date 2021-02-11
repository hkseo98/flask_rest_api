from flask import jsonify, Flask
from . import api
from models import Student, db
from flask import request
from flask_jwt import jwt_required


@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        userid = data.get('userid')
        username = data.get('username')
        number = data.get('number')
        re_number = data.get('re-number')

        if not (userid and username and number and re_number):
            return jsonify({'error': 'No arguments'}), 400

        if number != re_number:
            return jsonify({'error': 'Wrong password'}), 400

        student = Student()
        student.userid = userid
        student.username = username
        student.number = number

        db.session.add(student)
        db.session.commit()

        return jsonify(), 201

    users = Student.query.all()
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    return jsonify([user.serialize for user in users])


@api.route('/users/<uid>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        user = Student.query.filter(Student.id == uid).first()
        return jsonify(user.serialize)
    elif request.method == 'DELETE':
        Student.query.delete(Student.id == uid)
        return jsonify(), 204  # 데이터가 삭제되었음을 알려주는 204 코드.

    data = request.get_json()
    Student.query.filter(Student.id == uid).update(data)
    user = Student.query.filter(Student.id == uid).first()
    return jsonify(user.serialize)