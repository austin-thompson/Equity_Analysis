from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'testing'
fileObject = open("mongourl.txt", "r")
uri = fileObject.read()
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

db = client.finance_db  #Creating/accessing etf_db

etf_collection = db.etf_collection


@app.route("/")
@app.route("/main")
def main():
    return render_template('index.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = etf_collection
        signup_user = users.find_one({'username': request.form['username']})

        if signup_user:
            flash(request.form['username'] + ' username is already exist')
        else:

            hashed = bcrypt.generate_password_hash(request.form['password'],10).decode('utf-8')
            users.insert_one({'username': request.form['username'], 'password': hashed, 'email': request.form['email']})
        return redirect(url_for('signin'))

    return render_template('signup.html')

@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])

    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        users = etf_collection
        signin_user = users.find_one({'username': request.form['username']})

        if signin_user:
            if bcrypt.check_password_hash(signin_user['password'], request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        else:
            flash('Username and password combination is wrong')
            return render_template('signin.html')

    return render_template('signin.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
    app.run()