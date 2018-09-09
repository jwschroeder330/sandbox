from flask import Flask
from flask import render_template

# name app after the namespace with __name__
# __main__ if run from cmd line
# simple_app if referenced in another file
app = Flask(__name__)

# define routes - can use multiple which is useful for building API
@app.route('/')
@app.route('/<name>') # capture whatever comes after / as name arg
def index(name='Jake'):
    return render_template('index.html', name=name)


@app.route('/add/<int:num1>/<int:num2>') # typing params
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    # flask needs to have a string as a return
    context = {'num1' : num1, 'num2' : num2}
    return render_template('add.html', **context)



# debug=True; the app restarts upon changes
# port; software port to listen on, like a door
# 0.0.0.0; listen on all addresses that can get here
app.run(port=8000, host='0.0.0.0')
