from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'PSI COM ALBA'
@app.route('/contato')
def contato():
    return '<h1>yvitoriano@ifrn.edu.br</h1>   <h3>testessss</h3>'
@app.route('/exemplo')
def exemplo():
    return render_template('teste1.html')
@app.route('/exemplo2')
def exemplo2():
    return render_template('teste2.html')
if __name__ == '__main__':
    app.run()