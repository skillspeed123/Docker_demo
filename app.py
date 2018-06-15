From flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to skillspeed, you have successfully completed the docker project'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')