## flask app 

from flask import Flask

app = Flask(__name__)


## config
@app.route('/',methods=['GET'])
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
