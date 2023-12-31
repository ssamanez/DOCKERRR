from flask import Flask, render_template, request, flash, redirect,url_for, session

app = Flask(__name__)

app.secret_key = "Utec12345"

@app.route('/') # route     
def inicio():
    return render_template('index.html')  

@app.route('/templates/login.html') # route     
def login():
    return render_template('login.html')  

@app.route('/templates/password.html') # route     
def password():
    return render_template('password.html')  

@app.route('/templates/register.html') # route     
def register():
    return render_template('register.html')  

@app.route('/templates/temp.html') # route     
def temp():
    return render_template('temp.html')  



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7000,debug=True)
