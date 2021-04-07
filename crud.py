"""CRUD operations"""

from model import db, User, Workout, Workout_exercise, Exercise, connect_to_db







if __name__ == '__main__':
    from server import app
    connect_to_db(app)