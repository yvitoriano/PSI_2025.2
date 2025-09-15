from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    return 'PSI COM ALBA'

if __name__ == '__main__':
    app.run()