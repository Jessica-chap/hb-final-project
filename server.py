from flask import (Flask, render_template, request, flash, session,
                   url_for, redirect, jsonify)

from model import connect_to_db
from jinja2 import StrictUndefined
from datetime import datetime
from pprint import pformat
import crud
import requests
import os


app = Flask(__name__)
app.secret_key = "sun"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ['WGER_KEY']



###        HANDLE USER ROUTES           ###

@app.route('/')
def homepage():
    """View homepage."""
##route checked
    return render_template('homepage.html')


@app.route('/create_user')
def create_new_user():
    """Create new user page insert profile data."""
##route checked

    return render_template('create_user.html')


@app.route('/new_users', methods=['POST'])
def handle_new_user():
    """Handle user input to create account"""

    user_name = request.form.get('user_name')
    password = request.form.get('password')
    user_age = request.form.get('user_age')
    user_weight = request.form.get('user_weight')
    user_zipcode = request.form.get('user_zipcode')

    if user_name == '' or password == '':
            flash('Both user name and password field are required, please try again')
            return redirect('/')
    
    else:
        is_valid_user = crud.verify_valid_user(user_name)

        if is_valid_user == False:

            user =  crud.create_user(user_name, password, user_age, user_weight, user_zipcode)
            session['user_name'] = user_name
            flash('Account Created')
            return redirect(f'/users/{user.user_id}')

        else:
            flash('Already an account for that user name, please login')
            return redirect('/')




@app.route('/users', methods=['POST'])
def handle_login():
    """Handle user input at login"""
    
    user_name = request.form.get('user_name')
    is_valid_user = crud.verify_valid_user(user_name)

    if is_valid_user == False:
        flash('No account with user name, please create account')
        return redirect('/')

    else:
        password = request.form.get('password')
        user = crud.get_user_by_user_name(user_name)
        
        if password == user.password:
            session['user_name'] = user_name
            flash('Login success!')
            return redirect(f'/users/{user.user_id}') 
        
        else:
            flash('Wrong password, please try again')
            return redirect('/')


@app.route('/logout')
def user_logout():
    """log user out of current session"""
    session.pop('user', None)
    flash('Bye! See you tomorrow for another awesome workout!')
    return redirect('/')     


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show profile page of specific user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user=user)



####    WORKOUT CREATION ROUTES     ####


@app.route('/create_workout')
def new_workout_form():
    """Take user from personal page to page to start creating workout"""

    user = crud.get_user_by_user_name(session['user_name'])
    new_workout = crud.create_workout(user, datetime.now())
    session['user_id'] = user.user_id
    session['workout_id'] = new_workout.workout_id

    api_exercise_selection = request.args.get('api_exercise_selection')
    ex_url = 'https://wger.de/api/v2/exercise/?language=2'


    api_exercise_equipment = request.args.get('api_exercise_equipment')
    equip_url = 'https://wger.de/api/v2/equipment/?language=2'
    
    payload = {'apikey': API_KEY, 
                'api_exercise_selection': api_exercise_selection, 
                'api_exercise_equipment' : api_exercise_equipment}

    ex_response = requests.get(ex_url, params=payload)
    ex_data = ex_response.json() #dictionary
    api_exercises_list = ex_data['results'] #list

    equip_response = requests.get(equip_url, params=payload)
    equip_data =equip_response.json() #dictionary
    api_equipment_list = equip_data['results'] #list
 
    repunit_list = crud.get_we_repunit()
    weightunit_list = crud.get_we_weightunit()
 

    return render_template('create_workout.html', 
                            api_exercises_list= api_exercises_list,
                            repunit_list=repunit_list,
                            weightunit_list=weightunit_list,
                            api_equipment_list=api_equipment_list, 
                            name=user.user_name,
                            user_id = user.user_id)



@app.route('/add_exercise', methods=['POST'])
def add_exercise_to_workout():

    api_exercise_selection = request.form.get('api_exercise_selection')

    we_equipment = request.form.get('api_exercise_equipment')

    exercise = crud.verify_if_exercise(api_exercise_selection)
    if exercise == None:
        ex_url = 'https://wger.de/api/v2/exercise/'+api_exercise_selection+'/?language=2'

        payload = {'apikey': API_KEY}
        res = requests.get(ex_url, params=payload)
        data = res.json()
        exercise= crud.create_exercise(data['name'], data['description'], data['id']) 
        session['exercise_id'] = exercise.exercise_id
    else:
        exercise = exercise
  
   
    workout = crud.Workout.query.get(session['workout_id'])

    we_sets = request.form.get('exercise_sets')
    we_reps = request.form.get('exercise_reps')
    we_repunit = request.form.get('exercise_repunit')
    we_weight = request.form.get('exercise_weight')
    we_weightunit = request.form.get('exercise_weightunit')
   
    create_we = crud.create_workout_exercise(workout, exercise, 
                                            we_sets, we_reps, 
                                            we_repunit, we_weight, 
                                            we_weightunit, we_equipment) 
                                            

    ##               "JS name": model.py name          
    res_dict= {"api_exercise_selection": create_we.exercise.exercise_name, 
                "exercise_sets": create_we.we_sets,
                "exercise_reps": create_we.we_reps,
                "exercise_repunit": create_we.we_repunit, 
                "exercise_info": create_we.exercise.exercise_info, 
                "exercise_weight": create_we.we_weight, 
                "exercise_weightunit": create_we.we_weightunit, 
                "api_exercise_equipment": create_we.we_equipment}     
                             
    
    return jsonify(res_dict)


@app.route('/save_workout', methods=['POST'])
def save_workout_to_profile():

    workout_name = request.form.get('user_saved_workout_name')
    workout_id = session['workout_id']
    
    session['workout_name'] = workout_name

    user_id = session['user_id']
    user = crud.get_user_by_id(user_id)
    
    return render_template('user_profile.html', 
                            user_id= user_id, 
                            workout_name=workout_name, 
                            workout_id=workout_id, 
                            user=user, 
                            saved_workout_id = {"name": workout_name, 
                            "workout_id": workout_id})     

    
# print('*'*20)
# print('*'*20)
# return redirect(f'/users/{user_id}') 
#new route, render workout when going from profile to saved page 
 # saved_exercises = crud.exercises_from_workout(session['workout_id'])










    


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
