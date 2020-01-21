from flask import Flask

app = Flask(__name__)


@app.route('/hello-world')
def hello():
    return "hello world"


app.run(debug=True, host='0.0.0.0', port=5000)
