from flask import Flask, session, escape, request, url_for, redirect

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8r\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return """Logged in as %s <br>
        To change your username <a href="/change">click</a>""" % escape(session['username'])
    return "You are not logged in"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return """
        <form method='POST'>
        Username <input type='text' name='username'>
        <p><button type='submit'>Submit</button>
        </form>
    """

@app.route('/change', methods=['GET', 'POST'])
def change():
    if session:
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return """Change your username
            <form method='POST'>
            Username<input type='text' name='username'>
            <p><button type='submit'>Submit</button>
            </form>
            """
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
