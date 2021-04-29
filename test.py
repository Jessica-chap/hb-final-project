"""working on test file"""
from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data
from flask import sessionz

class FlaskTests(TestCase):

   def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn(b"Welcome", result.data)

    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                  data={"user_id": "rachel", "password": "123"},
                                  follow_redirects=True)
        self.assertIn(b"You are a valued user", result.data)
