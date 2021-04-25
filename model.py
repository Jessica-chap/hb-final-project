
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True,
                        primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    user_age = db.Column(db.Integer, nullable=True)
    user_weight = db.Column(db.Integer, nullable=True)
    user_zipcode = db.Column(db.Integer, nullable=True)


    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.user_name}>'


class Workout(db.Model):
    """User Workout"""

    __tablename__ = 'workouts'

    workout_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    workout_name = db.Column(db.String, unique=True, nullable=False)
    workout_date = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', backref='workouts')


    def __repr__(self):
        return f'<Workout workout_id={self.workout_id} workout_name={self.workout_name}>'


class Workout_exercise(db.Model):
    """Exercise specific for workout"""

    __tablename__ = 'workout_exercises'

    ##TODO complete table columns/repr
    we_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.workout_id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.exercise_id'))
    
    we_sets = db.Column(db.Integer, nullable=False)
    we_reps = db.Column(db.Integer, nullable=False)  
    we_repunit = db.Column(db.String, nullable=False)
    we_weight = db.Column(db.Integer, nullable=False)
    we_weightunit = db.Column(db.String, nullable=False) 
    we_equipment = db.Column(db.String, nullable=False)


    workout = db.relationship('Workout', backref='workout_exercises')
    exercise = db.relationship('Exercise', backref='workout_exercises')


    def __repr__(self):
        return f'<Workout_exercise we_id={self.we_id} we_sets={self.we_sets} we_reps={self.we_reps}>'


class Exercise(db.Model):
    """Specific exercise details"""

    __tablename__ = 'exercises'

    exercise_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
   
    exercise_name = db.Column(db.String, nullable=False)
    exercise_info = db.Column(db.Text, nullable=False)
    
    api_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Exercise exercise_id={self.exercise_id} exercise_name={self.exercise_name}>'





def connect_to_db(flask_app, db_uri='postgresql:///workouts', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')




if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    # connect_to_db(app, echo=False)