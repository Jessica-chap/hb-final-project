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
def handle_new_user():
    """Handle user input to create account"""
    #TODO zipcode is not adding- logic error
    #TODO is there a better way for the request?

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


# @app.route('/user_profile')
# def user_profile_page():
#     """Users profile page."""

#     return render_template('user_profile.html')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
