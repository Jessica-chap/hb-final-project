from flask import (Flask, render_template, request, flash, session,
                   url_for, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "sun"
app.jinja_env.undefined = StrictUndefined


##TODO cannot figure out how to get individual user page to show up, can 
## direct to general profile page but having issues with ID

##TODO work on more details for earch route with profile- login and create

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
def new_user():
    """Handle user input to create account"""
    #TODO handle data being returned


    return redirect('/user_profile', flash('Account Created Successfully'))



@app.route('/users', methods=['POST'])
def login_user():
    """Handle user input at login"""
##route checked
##need to work on verification/session

    user_name = request.form.get('user_name')
    password = request.form.get('password')

    user_name = crud.get_user_by_user_name(user_name)
    # user_id = crud.get_user_by_id(user_id)


    return redirect('/user_profile', 
                flash('Login success!'))




# @app.route('/users/<int:user_id>')
# def show_user(user_id):
#     """Show profile page of specific user."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_profile.html', user=user)


@app.route('/user_profile')
def user_profile_page():
    """Users profile page."""

    return render_template('user_profile.html')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
