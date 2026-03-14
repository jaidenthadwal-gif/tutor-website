from flask import Flask, render_template

app = Flask(__name__)

# This is your "Database" of tutors. 
tutors = [
    {
        "name": "Alfie Sorace",
        "subject": "Mathematics",
        "bio": "Passionate about making science accessible and fun.",
        "rate": "£45/hr"
    },
    {
        "name": "Mohammad Yunis", 
        "subject": "Computer Science", 
        "bio": "Software Engineer teaching Python, HTML, and Java.", 
        "rate": "£50/hr"
    },
    {
        "name": "Reyhan Afzal", 
        "subject": "English Literature", 
        "bio": "Helping students with essay writing and critical reading.", 
        "rate": "£35/hr"
    }
]

@app.route('/')
def home():
    return render_template('index.html', tutors=tutors)
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    # This grabs the data from the form boxes
    name = request.form.get('name')
    email = request.form.get('email')
    
    # This prints it in your terminal so you can see it worked!
    print(f"New Inquiry from: {name} ({email})")
    
    return "<h1>Message Received! We will email you soon.</h1>"
if __name__ == '__main__':
    app.run(debug=True, port=8001)