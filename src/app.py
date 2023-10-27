from tkinter.messagebox import QUESTION
from urllib import request
from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/modulo1')
def modulo1():
    return render_template('modulo1.html')
    
@app.route('/modulo2')
def modulo2():
    return render_template('modulo2.html')
   
@app.route('/modulo3')
def modulo3():
    return render_template('modulo3.html')

@app.route('/teste_modulo1')
def testemodulo1():
    return render_template('teste_modulo1.html')
       
@app.route('/teste_modulo2')
def testemodulo2():
    return render_template('teste_modulo2.html')

@app.route('/teste_modulo3')
def testemodulo3():
    return render_template('teste_modulo3.html')

@app.route('/submit', methods=['POST'])
def submit():
    questions = [
        {
            'question': 'É objetivo da Sprint Planning no Método Scrum?',
            'correct_answer': 'c'
        },
        {
            'question': 'Qual é o principal propósito da Daily Scrum no Método Scrum?',
            'correct_answer': 'c'
        },
        {
            'question': 'O que acontece durante o evento Sprint Review no método Scrum?',
            'correct_answer': 'b'
        },
        {
            'question': 'Qual é o objetivo da Sprint Retrospective no Método Scrum?',
            'correct_answer': 'c'
        }
    ]

    user_answers = [request.form[f'q{i}'] for i in range(1, 5)]
    results = []

    for i, answer in enumerate(user_answers):
        if answer == questions[i]['correct_answer']:
            results.append(f'Pergunta {i + 1}: Correta')
        else:
            results.append(f'Pergunta {i + 1}: Incorreta')

    num_correct = results.count('Pergunta Correta')
    num_questions = len(questions)

    if num_correct == num_questions:
        message = "Parabéns! Você acertou todas as perguntas desta etapa!"
    else:
        message = "Você completou o quiz. Continue praticando e revise as questões que você errou."

    return render_template('conclusao3.html', results=results, message=message)


@app.route('/conclusao1')
def conclusao1():
    return render_template('conclusao1.html')
   
@app.route('/conclusao2')
def conclusao2():
    return render_template('conclusao2.html')

@app.route('/conclusao3')
def conclusao3():
    return render_template('conclusao3.html')
                               
@app.route('/scrum_master')
def scrummaster():
    return render_template('scrum_master.html')
  
@app.route('/product_owner')
def productowner():
    return render_template('product_owner.html')
  
@app.route('/dev_team')
def devteam():
    return render_template('dev_team.html')

@app.route('/product_backlog')
def productbacklog():
    return render_template('product_backlog.html')

@app.route('/sprint_backlog')
def sprintbacklog():
    return render_template('sprint_backlog.html')

@app.route('/product_increment')
def productincrement():
    return render_template('product_increment.html')

@app.route('/sprint_planning')
def sprintplanning():
    return render_template('sprint_planning.html')

@app.route('/daily_scrum')
def dailyscrum():
    return render_template('daily_scrum.html')

@app.route('/sprint_review')
def sprintreview():
    return render_template('sprint_review.html')

@app.route('/retrospective')
def retrospective():
    return render_template('retrospective.html')

app.run(debug=True)