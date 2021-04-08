
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
    
    workout_date = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', backref='workouts')


    def __repr__(self):
        return f'<Workout workout_id={self.workout_id} workout_date={self.workout_date}>'


class Workout_exercise(db.Model):
    """Exercise specific for workout"""

    __tablename__ = 'workout_exercises'

    ##TODO complete table columns/repr
    we_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.workout_id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.exercise_id'))
    
    we_sets = db.Column(db.Integer, nullable=False)
    we_reps = db.Column(db.Integer, nullable=False)
    we_repunit = db.Column(db.String, nullable=True)
    we_weight = db.Column(db.String, nullable=True)
    we_weightunit = db.Column(db.String, nullable=True) 
    we_equipment = db.Column(db.String, nullable=True)


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





def example_data():
    """Sample data to help with testing"""

    User.query.delete()
 
    jess = User(user_name='jess', password='wifu', user_age='75', 
                user_weight='130', user_zipcode='48189')
    ankit = User(user_name='ankit', password='hubs', user_age='35', 
                user_weight='180', user_zipcode='48076')
    lily = User(user_name='lily', password='cats', user_age='16', 
                user_weight='25', user_zipcode='75201')

    db.session.add_all([jess, ankit, lily])
    db.session.commit()


    Exercise.query.delete()

    kb_swing = Exercise(exercise_name='kb_swing', 
                exercise_info='two handed grip and hinge at hips')
    squat = Exercise(exercise_name='squat',
                exercise_info='spine straight drive through heels bend at knees')
    crunch = Exercise(exercise_name='crunch',
                exercise_info='lay on back on the floor lift shoulders off ground')
                
    db.session.add_all([kb_swing, squat, crunch])
    db.session.commit()
    

    Workout.query.delete()

    jess_wrkt = Workout(user_id = jess.user_id, workout_date= datetime.now())
    ankit_wrkt = Workout(user_id = ankit.user_id, workout_date= datetime.now())
    lily_wrkt = Workout(user_id = lily.user_id, workout_date= datetime.now())

    db.session.add_all([jess_wrkt, ankit_wrkt, lily_wrkt])
    db.session.commit()


    Workout_exercise.query.delete()
    
    wrkt_kb = Workout_exercise(workout_id= jess_wrkt.workout_id, 
                                exercise_id= kb_swing.exercise_id,
                                we_sets= 3, we_reps=20, we_repunit='repetitions',
                                we_weight=10, we_weightunit= 'lb',
                                we_equipment='kettlebell')

    wrkt_squat = Workout_exercise(workout_id= ankit_wrkt.workout_id, 
                                exercise_id= squat.exercise_id,
                                we_sets= 5, we_reps=30, we_repunit='seconds',
                                we_weight=1, we_weightunit= 'bodyweight',
                                we_equipment='none bodyweight')

    wrkt_crunch = Workout_exercise(workout_id= lily_wrkt.workout_id, 
                                exercise_id= crunch.exercise_id,
                                we_sets= 3, we_reps=30, we_repunit='until failure',
                                we_weight=5, we_weightunit= 'lb',
                                we_equipment='swiss ball')

    db.session.add_all([wrkt_kb, wrkt_squat, wrkt_crunch])
    db.session.commit()





def connect_to_db(flask_app, db_uri='postgresql:///workouts', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')




if __name__ == '__main__':
    from server import app

    # connect_to_db(app)
    connect_to_db(app, echo=False)