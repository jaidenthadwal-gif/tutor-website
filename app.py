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
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    # Logic to find matches
    results = [t for t in tutors if query in t['subject'].lower() or query in t['name'].lower()]
    return render_template('results.html', tutors=results, query=query)

@app.route('/become-tutor')
def become_tutor():
    return render_template('become_tutor.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)