from flask import Flask

app = Flask(__name__)


@app.route('/hello-world')
def hello():
    return "hello world"

@app.route('/hello-world-2')
def hello_two():
    return "hello world-2"


app.run(debug=True, host='0.0.0.0', port=5000)
