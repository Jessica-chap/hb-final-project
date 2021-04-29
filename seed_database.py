"""Input data from test data user"""


import os
import json
# from random import choice, randint
from datetime import datetime

import crud 
import model
import server
import test_data

os.system('dropdb workouts')
os.system('createdb workouts')  

model.connect_to_db(server.app)
model.db.create_all()

test_data.example_data()