"""Test file for some crud functions, routes, login and out, and session"""
import os
import unittest
import crud 
from server import app
from model import connect_to_db, db, User, Workout, Workout_exercise, Exercise
from flask import session 
import test_data
from datetime import datetime



class FlaskTestsHpCreateUserRoute(unittest.TestCase):

    def setUp(self): 
        """setup before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()

        
    def test_home(self):
        """Test homepage page."""

        result = self.client.get('/')
        self.assertIn(b'Welcome', result.data)


    def test_create_user_route(self):
        """Test create user page route."""

        result = self.client.get('/create_user')
        self.assertIn(b'Create an Account', result.data)

    



class FlaskTestsUserLogin(unittest.TestCase):

    def setUp(self):
        """Setup before test."""

        app.config['TESTING'] = True
        self.client = app.test_client()
 
        connect_to_db(app, "postgresql:///testdb", echo=False)
        db.create_all()
        test_data.example_data()


    def test_users_login(self): 
        """Test login page."""
       
        return self.client.post('/users', data= dict(
                                    user_name = 'jess',
                                    password = 'wifu'),
                                    follow_redirects=True)
        self.assertIn(b'Login success!', result.data)


    def test_user_logout(self):
        """Test logout route."""

        result = self.client.get('/logout', 
                                follow_redirects=True)
        self.assertIn(b'Bye! See you tomorrow for another awesome workout!', result.data)



class FlaskTestsLoggedInwithDb(unittest.TestCase):

    def setUp(self):
        """setup before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'sun'
        self.client = app.test_client()

        connect_to_db(app, "postgresql:///testdb", echo=False)
        db.create_all()
        test_data.example_data()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1


    def test_new_users_creation(self):
        """New users route to create new account"""

        return self.client.post('/new_users', data= dict(
                                user_name='dock', password='test', 
                                user_age=50, user_weight=100, 
                                user_zipcode='01234'),
                                follow_redirects=True)
        self.assertIn(b'Age: 50', result.data)




class FlaskTestsCrudFunctions(unittest.TestCase):

    def setUp(self): 
        """setup before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()

        connect_to_db(app, "postgresql:///testdb", echo=False)
        db.create_all()
        test_data.example_data()
    

    def test_crud_create_user(self):
        """Crud function to create user instance"""
        
        user = crud.create_user(user_name='dock', password='test', 
                                user_age=50, user_weight=100, 
                                user_zipcode='01234') 
                                #data returned

        self.assertEqual('dock', user.user_name)


    def test_crud_create_exercise(self):
       """Crud function to create exericse instance"""

       exercise = crud.create_exercise(exercise_name= 'basic_exercise',
                                        exercise_info= 'description of exercise',
                                        api_id=10)

       self.assertEqual('basic_exercise', exercise.exercise_name)
               


    def test_crud_create_workout(self):
        """Crud function to create workout instance"""

        user = User.query.filter(User.user_name == 'jess').first()
        workout = crud.create_workout(user=user, 
                                    workout_name='Monday', 
                                    workout_date=datetime.now())
        
        self.assertEqual('Monday', workout.workout_name)


    def test_crud_create_we(self):
        """Crud function to create workout exercise instance"""

        exercise = Exercise.query.filter(Exercise.exercise_name == 'squat')
        workout = Workout.query.filter(Workout.workout_id== 1).first() 

        wrkt_exercise = crud.create_workout_exercise(workout= workout, 
                                                    exercise= exercise,
                                                    we_sets= 3, we_reps=12, 
                                                    we_repunit='reps',
                                                    we_weight=10, 
                                                    we_weightunit= 'lb',
                                                    we_equipment='dumbell')

        self.assertEqual('dumbell', workout_exercises.we_equipment )




    


# final commit




if __name__ == "__main__":
    
    unittest.main()