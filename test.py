"""working on test file"""
import unittest
import server
from model import connect_to_db, db
from flask import session #may not need, depends on if have tests for session
# from datetime import datetime
import test_data



class FlaskTestsHpCreateUser(unittest.TestCase):

    def setUp(self): #working
        """setup before every test."""

        server.app.config['TESTING'] = True
        self.client = server.app.test_client()

        
    def test_home(self):#working
        """Test homepage page."""

        result = self.client.get('/')
        self.assertIn(b'Welcome', result.data)


    def test_create_user(self):#working
        """Test create user page."""

        result = self.client.get('/create_user')
        self.assertIn(b'Create an Account', result.data)
    



class FlaskTestsLogin(unittest.TestCase):

    def setUp(self):#working
        """setup before every test."""

        server.app.config['TESTING'] = True
        server.app.config['SECRET_KEY'] = 'sun'
        self.client = server.app.test_client()

    # def test_login(self, user_name, password): #not working
        """Test login page.
        Getting error, not sure how to write
        TypeError: test_login() missing 2 required positional arguments: 'user_name' and 'password'
        """
        
        # should it be return or result = then the self.assert
        # return self.client.post('/users', data= dict(
        #                             user_name = 'jess',
        #                             password = 'wifu'),
        #                             follow_redirects=True)
        # self.assertIn(b'Login success!', result.data)


class FlaskTestsDatabase(unittest.TestCase):

    def setUp(self):
        """Setup before test."""

        server.app.config['TESTING'] = True
        self.client = server.app.test_client()

        connect_to_db(server.app, "postgresql:///testdb")

        db.create_all()
        test_data.example_data()






if __name__ == "__main__":
    
    unittest.main()