"""CRUD operations"""

from model import db, User, Workout, Workout_exercise, Exercise, connect_to_db
from datetime import datetime


#TODO fix dbworkouts and test last two functions


def create_user(user_name, password, user_age, user_weight, user_zipcode ):
    """Create and return a new user."""

    user = User(user_name=user_name, password=password,
                user_age=user_age, user_weight=user_weight,
                user_zipcode=user_zipcode)

    db.session.add(user)
    db.session.commit()

    return user

# riley = create_user(user_name='riley', password='dogs', user_age='101', 
#                 user_weight='100', user_zipcode='48076')


def create_exercise(exercise_name, exercise_info):
    """create and return exercise"""

    exercise = Exercise(exercise_name=exercise_name,
                        exercise_info=exercise_info)

    db.session.add(exercise)
    db.session.commit()

    return exercise

# boat_row = create_exercise(exercise_name='boat_row', exercise_info='row row row the boat')



def create_workout(user, workout_date):
    """create and return workout"""

    workout = Workout(user=user.user_id, workout_date=workout_date)

    db.session.add(workout)
    db.session.commit()

    return workout

# riley_wrkt = create_workout(user= riley.user_id, workout_date= datetime.now())


def create_workout_exercise(workout, exercise, we_sets, we_reps, we_weight, we_equipment):
    """create and return workout_exercise"""

    workout_exercise = Workout_exercise(workout=workout.workout_id,
                        exercise=exercise.exercise_id,
                        we_sets=we_sets, we_reps=we_reps,
                        we_weight=we_weight, 
                        we_equipment=we_equipment)

    db.session.add(workout_exercise)
    db.session.commit()

    return workout_exercise

# wrkt_boat_row = create_workout_exercise(workout= riley_wrkt.workout_id, 
#                                 exercise= boat_row.exercise_id,
#                                 we_sets= 1, we_reps=60, we_repunit='minutes',
#                                 we_weight=1, we_weightunit= 'bodyweight',
#                                 we_equipment='none')















if __name__ == '__main__':
    from server import app
    connect_to_db(app)