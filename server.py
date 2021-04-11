from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "sun"
app.jinja_env.undefined = StrictUndefined

##TODO work on more details for earch route with profile- login and create

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/create_user')
def create_new_user():
    """Create new user."""


    return render_template('create_user.html')


@app.route('/new_users', methods=['POST'])
def new_user():

    #TODO handle data being returned

    return redirect('/', flash('Success! Login!'))



@app.route('/users', methods=['POST'])
def login_user():

    user_name = request.form.get('user_name')
    password = request.form.get('password')

    user = crud.get_user_by_user_name(user_name)

    return redirect('/user_profile')


@app.route('/user_profile')
def user_profile_page():
    """Users profile page."""

    return render_template('user_profile.html')



##TODO NEED CRUD DEF
# @app.route('/users/<user_id>')
# def show_user(user_id):
#     """Show profile page of specific user."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
