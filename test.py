"""working on test file"""
from unittest import TestCase
from server import app
from model import connect_to_db, db
from flask import session #may not need, depends on if have tests for session
# from datetime import datetime
import test_data


class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """set up before test."""
        self.client = app.test_client()

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
