from flask import Flask, render_template, request, session, jsonify

messages = []
app = Flask(__name__)
#Home
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not request.form.get('username'):
        return "Please enter a valid username!"
    else:
        session['username'] = request.form.get('username')
        return render_template('chat.html', username=session['username'])

@app.route('/messages')
def messageview():
    return render_template("messages.html", messages=messages[-20:])

@app.route('/set-data', methods = ['POST'])
def setdata():
    if not request.form.get('message') or not session['username']:
        return "invalid request"
    messages.append({'sender': session['username'], 'message': request.form.get('message')})
    return "appended"

if(__name__=="__main__"):
    app.secret_key = 'fossdaytutorial'
    app.run(host = '0.0.0.0', port = 80, debug=True)
