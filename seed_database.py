"""Input data from test data user"""

##TODO WIP, may use more if add premade workouts, right 
##now only adding the test data created in model.py

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb workouts')
os.system('createdb workouts')  

model.connect_to_db(server.app)
model.db.create_all()

model.example_data()