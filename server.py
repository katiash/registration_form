#Import Flash from Flask:
from flask import Flask, render_template, redirect, request, session, flash
#Import regular expression 're' module from Python:
import re

#Create a regular expression object that we can use to run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=["POST"])
def submit():
    #HERE START VALIDATION of the Email:
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!") 
        # just pass a string to the flash function, 
        # i.e. your validation error message
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        session['email']=request.form['email']
        #GO ON TO VALIDATE first_name:
        if len(request.form['first_name'])< 1:
            flash("First Name is a required field!")
        elif not request.form['first_name'].isalpha():
            flash("First Name field cannot contain non-alphabetic characters.\nPlease re-enter.")
        else:
            session['first_name']=request.form['first_name']
            #VALIDATE last_name field:
            if len(request.form['last_name'])<1:
                flash("Last Name is a required field!")
            elif not request.form['last_name'].isalpha():
                flash("Last Name field cannot contain non-alphabetic characters.\n Please re-enter.")
            else:
                session['last_name']=request.form['last_name']
                #VALIDATE password field:
                if len(request.form['password'])<9:
                    flash("The password should have 9 or more characters!")
                else:
                    session['password']=request.form['password']
                    #VALIDATE confirm_password field:
                    if request.form['confirm_password'] != session['password']:
                        flash("Your passwords do not match. Please re-confirm your password")
                    else:
                        flash("Thank you for submitting your information!\nYour email is {}\nFirst Name: {}\nLast Name: {}\n".format(session['email'], session['first_name'], session['last_name']))
                         # just pass a string to the flash function
    return redirect('/') #either way, the application should redirect back to the page again.

app.run(debug=True)