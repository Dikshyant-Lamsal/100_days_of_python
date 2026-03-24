from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return "hello"

@app.route("/guess/<name>",methods=["GET"])
def guess_things(name):
    gender = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = gender["gender"]
    age = requests.get(f"https://api.agify.io?name={name}").json()
    age = age["age"]
    return render_template("index.html",name=name,age=age,gender=gender)
if __name__=="__main__":
    app.run(debug=True) 

