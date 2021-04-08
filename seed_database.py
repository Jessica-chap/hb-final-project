"""Input data from test data user"""


import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb workouts')