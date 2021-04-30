"""working on test file"""
import os
import unittest
from server import app
from model import connect_to_db, db, User, Workout, Workout_exercise, Exercise
from flask import session 
import test_data



class FlaskTestsHpCreateUser(unittest.TestCase):#all functions working 

    def setUp(self): 
        """setup before every test."""

        app.config['TESTING'] = True
        self.client = app.test_client()

        
    def test_home(self):
        """Test homepage page."""

        result = self.client.get('/')
        self.assertIn(b'Welcome', result.data)


    def test_create_user(self):
        """Test create user page."""

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

    



class FlaskTestsLoggedInwithDb(unittest.TestCase):

    def setUp(self):#working
        """setup before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'sun'
        self.client = app.test_client()

        # with self.client as c:
        #     with c.session_transaction() as sess:
        #         sess['user_id'] = 1


    




if __name__ == "__main__":
    
    unittest.main()