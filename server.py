from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi!~~~~~!'


@app.route('/test/<id>')
def create(id):
    print(id)
    
    return 'TESTING' + id

app.run(port=5001, debug=True)