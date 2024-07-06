from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
    
output:
 * Serving Flask app 'App'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 267-338-796
127.0.0.1 - - [04/Jul/2024 15:42:01] "GET / HTTP/1.1" 200 