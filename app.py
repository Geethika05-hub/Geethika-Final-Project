from flask import Flask, render_template, request, send_file, redirect, url_for
from agents.topic_agent import process_topic
from agents.question_agent import generate_questions
from agents.tips_agent import generate_tips
from agents.resume_agent import generate_resume_points
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('questions'))

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    questions = []
    if request.method == 'POST':
        if 'generate' in request.form:
            topic = request.form['topic']
            tech_q, behav_q = generate_questions(topic)
            questions = tech_q + behav_q
        elif 'export' in request.form:
            topic = request.form['topic']
            tech_q, behav_q = generate_questions(topic)
            questions = tech_q + behav_q
            filename = os.path.join('export', f"{topic.replace(' ', '_')}_questions.csv")
            os.makedirs('export', exist_ok=True)
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Question', 'Type', 'Difficulty'])
                writer.writerows(questions)
            return send_file(filename, as_attachment=True)
    return render_template('questions.html', questions=questions)

@app.route('/tips', methods=['GET', 'POST'])
def tips():
    tips = []
    if request.method == 'POST':
        job_desc = request.form['job_description']
        tips = generate_tips(job_desc)
    return render_template('tips.html', tips=tips)

@app.route('/practice', methods=['GET', 'POST'])
def practice():
    practice_questions = []
    if request.method == 'POST':
        topic_practice = request.form['topic_practice']
        tech_q, behav_q = generate_questions(topic_practice)
        practice_questions = tech_q + behav_q
    return render_template('practice.html', practice_questions=practice_questions)

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    resume_points = []
    if request.method == 'POST':
        job_desc_res = request.form['job_description_resume']
        resume_points = generate_resume_points(job_desc_res)
    return render_template('resume.html', resume_points=resume_points)

if __name__ == '__main__':
    app.run(debug=True)
