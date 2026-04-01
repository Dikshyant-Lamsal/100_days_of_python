from flask import Flask, flash, render_template, request
from forms import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '9068123'
bootstrap = Bootstrap5(app)

@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html',form=form)
   
if __name__ == '__main__':
    app.run(debug=True)
