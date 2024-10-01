
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder=r'C:\Users\Beacon Consulting\Downloads\flaskProject1\template')
app.config["MONGO_URI"] = "mongodb://localhost:27017/survey_db"  # Adjust URI as needed
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        "age": request.form['age'],
        "gender": request.form['gender'],
        "total_income": request.form['total_income'],
        "expenses": {
            "utilities": request.form['utilities'],
            "entertainment": request.form['entertainment'],
            "school_fees": request.form['school_fees'],
            "shopping": request.form['shopping'],
            "healthcare": request.form['healthcare']
        }
    }
    mongo.db.users.insert_one(user_data)  # Ensure 'users' collection exists
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)