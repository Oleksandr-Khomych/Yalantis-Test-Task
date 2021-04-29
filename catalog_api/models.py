from app import db


class Course(db.Model):
    __tablename__ = 'catalog'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    lectures_count = db.Column(db.Integer)

    def __repr__(self):
        return f'<Course(id={self.id}, name={self.name}, start_date={self.start_date}, end_date={self.end_date})>'
