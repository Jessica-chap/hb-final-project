"""CRUD operations"""

from model import db, User, Weight, Workout, Workout_exercise, Exercise, connect_to_db
from datetime import datetime
import json


####################USER FUNCTIONS#################################

def create_user(user_name, password, user_age=None, user_weight=None, user_zipcode=None ):
    """Create and return a new user.
    """

    user = User(user_name=user_name, password=password,
                user_age=user_age, user_weight=user_weight,
                user_zipcode=user_zipcode)

    db.session.add(user)
    db.session.commit()

    return user

# dock = create_user(user_name='dock', password='test', user_age=50, user_weight=100, user_zipcode=01234)

def get_user_by_user_name(user_name):
    """Return a user by user_name"""

    return User.query.filter(User.user_name == user_name).first()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def verify_valid_user(user_name):
    """Return true or false depending on whether user_name in database"""

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

# basic_exercise = create_exercise(exercise_name='basic_exercise', exercise_info='this should be description of exercise')

def verify_if_exercise(api_exercise):
    
    exercise = Exercise.query.filter(Exercise.api_id == api_exercise).first()

    return exercise


###################WEIGHT ENTRY FUNCTIONS####################################


def create_weight_entry(user, weight_input, weight_date):

    weight = Weight(user=user, weight_input=weight_input, 
                    weight_date=weight_date)
    
    db.session.add(weight)
    db.session.commit()

    return weight


def all_user_weight_entries(user_id):

    entries = Weight.query.filter(Weight.user_id== user_id).all()

    return entries


def weight_entries_dict(user_id):

    weight_entries = all_user_weight_entries(user_id)

    entries_dict = {}
    for entry in weight_entries:
        weight_date = entry.weight_date.strftime("%d %b %Y %H:%M")
        entries_dict[weight_date] = entry.weight_input
        
    json_dict = json.dumps(entries_dict)

    return json_dict


###################WORKOUT FUNCTIONS#########################################

def create_workout(user, workout_name, workout_date):
    """create and return workout"""

    workout = Workout(user=user, workout_name=workout_name, 
                        workout_date=workout_date)

    db.session.add(workout)
    db.session.commit()

    return workout

# dock_wrkt = create_workout(user= dock, workout_name= Today, workout_date= datetime.now())

def get_workout_by_id(workout_id):
    """Return a workout object with id"""

    workout = Workout.query.filter(Workout.workout_id== workout_id).first()
    
    return workout


 
def workouts_by_user_id(user_id):

    workouts = Workout.query.filter(Workout.user_id==user_id).all()
    
    return workouts

   

def delete_empty_wkt(workout_id):

   delete_wkt = Workout.query.filter(Workout.workout_id== workout_id).delete()
   db.session.commit()
 
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

# wrkt_basic_exercise = create_workout_exercise(workout= dock_wrkt, exercise= basic_exercise,
#                                 we_sets= 3, we_reps=12, we_repunit='reps',
#                                 we_weight=10, we_weightunit= 'lb', we_equipment='dumbell')

def exercises_from_workout(workout_id):

    exercises_from_workout = Workout_exercise.query.filter(Workout_exercise.workout_id == workout_id).all()
    
    return exercises_from_workout


def get_we_repunit():
   
    return ['reps','sec', 'min', 'mi.', 'km', 'until failure' ]

def get_we_weightunit():
   
    return ['lb', 'kg', 'bodyweight']










if __name__ == '__main__':
    from server import app
    connect_to_db(app)
   