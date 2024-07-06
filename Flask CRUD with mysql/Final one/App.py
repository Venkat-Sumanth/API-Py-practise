from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():
    # Here you would handle the form submission and insert the data into the database
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    # Code to insert this data into your database
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
