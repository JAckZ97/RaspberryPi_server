from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route("/me")
def me():
    return render_template('about.html')

@app.route("/Setup")
def firstpost():
    return render_template('/pages/setup.html')

    
# @app.route('/login', methods = ["POST", "GET"])
# def login():
#     return render_template('login.html')

# @app.route('/<user>')
# def user(usr):
#     return "<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=3000)