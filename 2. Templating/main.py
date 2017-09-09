from flask import Flask, render_template

app = Flask(__name__)
#Home
@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/user/<username>')
def user(username):
	return render_template("user.html", username=username)

if(__name__=="__main__"):
    app.run(host = '0.0.0.0', port = 80, debug=True)
