"""CRUD operations"""

from model import db, User, Workout, Workout_exercise, Exercise, connect_to_db
from datetime import datetime


####################USER FUNCTIONS#################################

def create_user(user_name, password, user_age=None, user_weight=None, user_zipcode=None ):
    """Create and return a new user."""

    user = User(user_name=user_name, password=password,
                user_age=user_age, user_weight=user_weight,
                user_zipcode=user_zipcode)

    db.session.add(user)
    db.session.commit()

    return user

# riley = create_user(user_name='riley', password='dogs', user_age='101', user_weight='100', user_zipcode='48076')

def get_user_by_user_name(user_name):
    """Return a user by user_name"""

    return User.query.filter(User.user_name == user_name).first()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def verify_valid_user(user_name):
    """Return true or false depending on whether user_name in database"""
    ## query for one record instead of all 

    user = User.query.filter(User.user_name == user_name).first()

    if user:
        return True
    
    return False



###################EXERCISE FUNCTIONS###########################################

def create_exercise(exercise_name, exercise_info, api_id):
    """create and return exercise"""

    exercise = Exercise(exercise_name=exercise_name,
                        exercise_info=exercise_info, 
                        api_id=api_id)

    db.session.add(exercise)
    db.session.commit()

    return exercise

# boat_row = create_exercise(exercise_name='boat_row', exercise_info='row row row the boat')

def verify_if_exercise(api_exercise):
    
    exercise = Exercise.query.filter(Exercise.api_id == api_exercise).first()

    return exercise


# def exercise_by_api_id(api_id):

#     exercise = Exercise.query.filter()

###################WORKOUT FUNCTIONS#########################################

def create_workout(user, workout_date):
    """create and return workout"""

    workout = Workout(user=user, workout_date=workout_date)

    db.session.add(workout)
    db.session.commit()

    return workout

# riley_wrkt = create_workout(user= riley, workout_date= datetime.now())

# def exercises_from_workout(workout_id):
#     # SELECT exercise_name FROM exercises JOIN workout_exercises ON exercises.exercise_id = workout_exercises.exercise_id  WHERE workout_id = 27;
#     workout_session = Exercise.


###################WORKOUT EXERCISE FUNCTIONS#############################

def create_workout_exercise(workout, exercise, we_sets, we_reps, we_repunit, we_weight, we_weightunit, we_equipment):
    """create and return workout_exercise"""

    workout_exercise = Workout_exercise(workout=workout,
                        exercise=exercise, we_sets=we_sets, 
                        we_reps=we_reps, we_repunit=we_repunit,
                        we_weight=we_weight, we_weightunit=we_weightunit, we_equipment=we_equipment)

    db.session.add(workout_exercise)
    db.session.commit()

    return workout_exercise

# wrkt_boat_row = create_workout_exercise(workout= riley_wrkt, exercise= boat_row,
#                                 we_sets= 1, we_reps=60, we_repunit='minutes',
#                                 we_weight=1, we_weightunit= 'bodyweight', we_equipment='row machine')
def get_we_repunit():
    """to test connection between server and html
    will update with API inormation"""
    return ['repetitions','seconds', 'minutes', 'until failure' ]

def get_we_weightunit():
    """to test connection betwen server and html
    will update with API information"""
    return ['lb', 'kg', 'bodyweight']


def get_workout_by_id(workout_id):
    """Return a workout object with id"""
    
    return User.query.get(user_id)


#query to get back workout object - 
# SELECT exercise_name FROM exercises JOIN workout_exercises ON exercises.exercise_id = workout_exercises.exercise_id  WHERE workout_id = 27;






if __name__ == '__main__':
    from server import app
    connect_to_db(app)