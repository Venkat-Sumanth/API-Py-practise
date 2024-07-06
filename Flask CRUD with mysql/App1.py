from flask import Flask    #we imported the Flask instance

app = Flask(__name__)      #we instantiate the flask

@app.route('/')      #route is defined for the root URL ("/"), which returns the string "Hello, World!" when accessed.
def Index():
    return "Hello Flask Application"

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


-By writing if __name__ == "__main__":, you are telling Python to execute the block of code under this 
 condition only if the script is being run directly. This prevents the code from being executed if the script 
 is imported as a module in another script.
 
-The if __name__ == "__main__": block checks if the script is being run directly. 
 If true, it calls app.run(debug=True), which starts the Flask development server with debugging enabled.
 
-In the context of a Flask application, this block is used to start the development server. 
 It ensures that app.run(debug=True) is only called when you run the script directly. 
 If someone imports your script as a module, the server will not start automatically.