from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(32))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

    @property #함수지만 변수처럼 사용할 수 있게 해줌 - 모델에서 시리얼라이즈 변수에 접근하면 딕셔너리 값이 나옴.
    def serialize(self):
        return {
            'id': self.id,
            'number': self.number,
            'userid': self.userid,
            'username': self.username,
        }