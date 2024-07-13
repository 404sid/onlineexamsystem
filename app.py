from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for login
users = {
    'dilraj': 'miniproject',
    'user2': 'password2',
    'user3': 'password3'
}

@app.route('/')
def login():
    error = request.args.get('error')
    return render_template('login.html', error=error)

@app.route('/exam_details', methods=['POST'])
def exam_details():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return render_template('exam_details.html')
    else:
        error = "Invalid username or password. Please try again."
        return render_template('login.html', error=error)

# ... (rest of your routes)



@app.route('/mcq_questions', methods=['POST'])
def mcq_questions():
    return render_template('mcq_questions.html')

@app.route('/exam_result', methods=['POST'])
def exam_result():
    # Dummy scoring logic (replace with your own)
    score = 0
    answers = {'q1': 'b', 'q2': 'd', 'q3': 'c', 'q4': 'b', 'q5': 'c' , 'q6': 'b', 'q7': 'c' , 'q8': 'b', 'q9': 'a' , 'q10': 'b' }
    for question, answer in answers.items():
        if request.form.get(question) == answer:
            score += 1
    return render_template('exam_result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
