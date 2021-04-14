from flask import (Flask, render_template, request, flash, session,
                   url_for, redirect)

from model import connect_to_db
from jinja2 import StrictUndefined
from datetime import datetime
import crud
import os


app = Flask(__name__)
app.secret_key = "sun"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ['WGER_KEY']


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
                        


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show profile page of specific user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user=user)



@app.route('/create_workout')
def new_workout_form():
    """Take user from personal page to page to start creating workout"""

    #TODO why is user_name session not being able to use in create_workout html
    user = crud.get_user_by_user_name(session['user_name'])
    new_workout = crud.create_workout(user, datetime.now())
    session['user_id'] = user.user_id
    session['workout_id'] = new_workout.workout_id

    exercise_list = crud.Exercise.query.all()
    # exercise_name = exercise_list.exercise_name
    # exercise_info = exercise_list.exercise_info
    #add to return? ex_name = exercise_name, 
                            # ex_info = exercise_info,

    return render_template('create_workout.html', 
                            exercise_list= exercise_list, 
                            name=user.user_name)

#TODO how do I add the response, and use to create
#object in table??
#How do I keep all on one page

@app.route('/create_exercise')
def create_exercises_for_workout():
    """handle api request for exercise information"""
    
    #make get request for exercises table information- 
    #exercise_name, exercise_info, and API key

    #url = https://wger.de/api/v2/exercise/

    #add data returned from request to payload
    # make request for a response that includes the url with
        #params set in payload
    #save the response data = 
    #TODO what is the _embedded


    pass




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
