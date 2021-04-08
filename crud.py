"""CRUD operations"""

from model import db, User, Workout, Workout_exercise, Exercise, connect_to_db



def create_user(user_name, password, user_age, user_weight, user_zipcode ):
    """Create and return a new user."""

    user = User(user_name=user_name, password=password,
                user_age=user_age, user_weight=user_weight,
                user_zipcode=user_zipcode)

    db.session.add(user)
    db.session.commit()

    return user


def create_exercise(exercise_name, exercise_info):
    """create and return exercise"""

    exercise = exercise(exercise_name=exercise_name,
                        exercise_info=exercise_info)

    db.session.add(exercise)
    db.session.commit()

    return exercise



def create_workout(user, workout_date):
    """create and return workout"""

    workout = Workout(user_id=user.user_id, workout_date=workout_date)

    db.session.add(workout)
    db.session.commit()

    return workout


def create_workout_exercise(workout, exercise, we_sets, we_reps, we_weight, we_equipment):
    """create and return workout_exercise"""

    workout_exercise = Workout_exercise(workout_id=workout.workout_id,
                        exercise_id=exercise.exercise_id,
                        we_sets=we_sets, we_reps=we_reps,
                        we_weight=we_weight, 
                        we_equipment=we_equipment)

    db.session.add(workout_exercise)
    db.session.commit()

    return workout_exercise



















if __name__ == '__main__':
    from server import app
    connect_to_db(app)