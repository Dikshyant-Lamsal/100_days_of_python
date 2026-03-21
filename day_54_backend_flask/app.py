from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return 'Hello World'

def make_bold(value):
    def wrapper_function():
        return '<b>'+value()+'</b>'
    return wrapper_function

def make_italic(value):
    def wrapper_function():
        return '<em>'+value()+'</em>'
    return wrapper_function

def make_underline(value):
    def wrapper_function():
        return '<u>'+value()+'</u>'
    return wrapper_function


@app.route('/bye',methods=['GET'])
@make_bold
@make_italic
@make_underline
def bye_function():
    return 'Bye!'


@app.route("/name/<name>",methods=['GET'])
def print_name(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(debug=True)