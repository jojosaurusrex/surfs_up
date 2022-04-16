from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/help')
def help():
    return 'Frequently Asked Questions n\ import issues?: is flask properly installed'
    # this is all still on one line, but it works!

# set FLASK_APP=app.py

if __name__ == "__main__":
    app.run(debug=True)

# flask run
#commented out commands need to be within the terminal