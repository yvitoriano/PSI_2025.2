from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'PSI COM ALBA'
@app.route('/contato')
def contato():
    return 'yvitoriano@ifrn.edu.br'
if __name__ == '__main__':
    app.run()