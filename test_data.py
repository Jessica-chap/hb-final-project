"""test data for database"""
 


from model import db, User, Workout, Workout_exercise, Exercise, connect_to_db

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



def example_data():
    """Sample data to help with testing"""

    Workout_exercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()
    User.query.delete()
    Weight.query.delete()
 
    jess = User(user_name='jess', password='wifu', user_age='75', 
                user_weight='130', user_zipcode='48189')
    ankit = User(user_name='ankit', password='hubs', user_age='35', 
                user_weight='180', user_zipcode='48076')
    lily = User(user_name='lily', password='cats', user_age='16', 
                user_weight='25', user_zipcode='75201')
    riley = User(user_name='riley', password='dogs', user_age='101', 
                user_weight='100', user_zipcode='48076')

    db.session.add_all([jess, ankit, lily, riley])
    db.session.commit()
   

    kb_swing = Exercise(exercise_name='kb_swing', 
                exercise_info='two handed grip and hinge at hips')
    squat = Exercise(exercise_name='squat',
                exercise_info='spine straight drive through heels bend at knees')
    crunch = Exercise(exercise_name='crunch',
                exercise_info='lay on back on the floor lift shoulders off ground')
    boat_row = Exercise(exercise_name='boat_row', 
                exercise_info='row row row the boat')


    db.session.add_all([kb_swing, squat, crunch, boat_row])
    db.session.commit()
    

   

    jess_wrkt = Workout(user_id = jess.user_id, 
                        workout_name= 'Monday',
                        workout_date= datetime.now())
    ankit_wrkt = Workout(user_id = ankit.user_id, 
                        workout_name= 'Tuesday',
                        workout_date= datetime.now())
    lily_wrkt = Workout(user_id = lily.user_id,
                        workout_name= 'Wednesday',
                        workout_date= datetime.now())
    riley_wrkt = Workout(user_id = riley.user_id,
                        workout_name= 'Thursday',
                        workout_date= datetime.now())

    db.session.add_all([jess_wrkt, ankit_wrkt, lily_wrkt, riley_wrkt])
    db.session.commit()


    
    
    wrkt_kb = Workout_exercise(workout_id= jess_wrkt.workout_id, 
                                exercise_id= kb_swing.exercise_id,
                                we_sets= 3, we_reps=20, we_repunit='repetitions',
                                we_weight=10, we_weightunit= 'lb',
                                we_equipment='kettlebell')

    wrkt_squat = Workout_exercise(workout_id= ankit_wrkt.workout_id, 
                                exercise_id= squat.exercise_id,
                                we_sets= 5, we_reps=30, we_repunit='seconds',
                                we_weight=1, we_weightunit= 'bodyweight', 
                                we_equipment='none')

    wrkt_crunch = Workout_exercise(workout_id= lily_wrkt.workout_id, 
                                exercise_id= crunch.exercise_id,
                                we_sets= 3, we_reps=30, we_repunit='until failure',
                                we_weight=5, we_weightunit= 'lb',
                                we_equipment='swiss ball')

    wrkt_boat_row = Workout_exercise(workout_id= riley_wrkt.workout_id, 
                                exercise_id= boat_row.exercise_id,
                                we_sets= 1, we_reps=60, we_repunit='minutes',
                                we_weight=1, we_weightunit= 'bodyweight',
                                 we_equipment='row machine')


    db.session.add_all([wrkt_kb, wrkt_squat, wrkt_crunch, wrkt_boat_row])
    db.session.commit()





if __name__ == '__main__':
    from server import app

    connect_to_db(app)
