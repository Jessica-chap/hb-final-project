
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

##TO DO 
###Work on relationships in tables


class User(db.Model):
    """A user"""
##add null values##
##for weight, kg or lb##

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True,
                        primary_key=True)
    user_name = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    user_age = db.Column(db.Integer)
    user_weight = db.Column(db.Integer)
    user_gender = db.Column(db.String)


    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.user_name}>'


class Workout(db.Model):
    """User Workout"""

    __tablename__ = 'workouts'

    workout_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    workout_date = db.Column(db.datetime)


    def __repr__(self):
        return f'<Workout workout_id={self.workout_id} workout_date={self.workout_date}>'


class Workout_exercise(db.Model):
    """Exercise specific for workout"""

    __tablename__ = 'workout_exercises'

    ##TODO complete table columns/repr


class Exercises(db.Model):
    """Specific exercise details"""

    __tablename__ = 'exercises'

    ##TODO complete tabel columns/repr

    













if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    # connect_to_db(app, echo=False)