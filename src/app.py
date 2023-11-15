from tkinter.messagebox import QUESTION
from urllib import request
from flask import Flask, render_template, request, Response, jsonify
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import B0
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

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

@app.route('/enviar', methods=['POST']) 
def enviar():
    questions = [
        {
            'question': 'Qual é a principal responsabilidade do Scrum Master em relação aos impedimentos no Scrum?',
            'correct_answer': 'c'
        },
        {
            'question': 'Qual é um dos exemplos práticos de atividades que um Scrum Master pode realizar, conforme mencionado no texto?',
            'correct_answer': 'c'
        },
        {
            'question': 'De acordo com o texto, qual é uma das responsabilidades fundamentais de um Product Owner?',
            'correct_answer': 'c'
        },
        {
            'question': 'Qual é uma das principais responsabilidades dos membros da equipe de desenvolvimento (Team Dev) mencionada no texto?',
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
           
            
    num_correct = 0 
    for result in results:
        if "Correta" in result:
            num_correct += 1
    num_questions = len(questions)

    if num_correct < num_questions:
        message = "Continue praticando e revise os conteúdos das questões erradas!"
    else:
        message = ""
        
    return render_template('conclusao1.html', results=results, message=message)

    
@app.route('/teste_modulo2')
def testemodulo2():
    return render_template('teste_modulo2.html')

@app.route('/send', methods=['POST']) 
def send():
    questions = [
        {
            'question': 'Qual das seguintes afirmações sobre o Product Backlog está correta?',
            'correct_answer': 'd'
        },
        {
            'question': 'Qual é a principal função da Sprint Backlog?',
            'correct_answer': 'd'
        },
        {
            'question': 'O que é um Product Increment?',
            'correct_answer': 'c'
        },
        {
            'question': 'Quem é geralmente responsável por priorizar os itens no Product Backlog?',
            'correct_answer': 'd'
        }
    ]

    user_answers = [request.form[f'q{i}'] for i in range(1, 5)]
    results = []

    for i, answer in enumerate(user_answers):
        if answer == questions[i]['correct_answer']:
            results.append(f'Pergunta {i + 1}: Correta')
        else:
            results.append(f'Pergunta {i + 1}: Incorreta')

    num_correct = 0 
    for result in results:
        if "Correta" in result:
            num_correct += 1
    num_questions = len(questions)

    if num_correct < num_questions:
        message = "Continue praticando e revise os conteúdos das questões erradas!"
    else:
        message = ""
        
    return render_template('conclusao2.html', results=results, message=message)

        


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

    num_correct = 0 
    for result in results:
        if "Correta" in result:
            num_correct += 1
    num_questions = len(questions)

    if num_correct < num_questions:
        message = "Continue praticando e revise os conteúdos das questões erradas!"
    else:
        message = ""

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

@app.route('/pacer')
def pacer():
    return render_template('pacer.html')


@app.route('/salvar_nome', methods=['POST'])
def salvar_nome():
    global name
    name = request.form['nome']

    # Puxando a fonte de fora
    LsBold = "src/static/font/LeagueSpartan-Bold.ttf"  
    GiBold = "src/static/font/GlacialIndifference-Bold.ttf"
    GiRegular = "src/static/font/GlacialIndifference-Regular.ttf"
    Ft = "src/static/font/Fontspring-theseasons-lt.ttf"
    pdfmetrics.registerFont(TTFont("LeagueSpartan", LsBold))
    pdfmetrics.registerFont(TTFont("GlacialIndifference-Regular", GiRegular))
    pdfmetrics.registerFont(TTFont("GlacialIndifference-Bold", GiBold))
    pdfmetrics.registerFont(TTFont("Fontspring-theseasons-lt", Ft))

    # caminho para o arquivo PDF
    pdf_path = os.path.join('src', 'static', 'docs', 'certificado.pdf')

    #Crindo o arquivo pdf com o tamano 2000px, 1414px
    cnv = canvas.Canvas('certificado.pdf', pagesize = (2000, 1414))

    # Dcor de fundo como azul 
    cnv.setFillColor(colors.HexColor("#0058bce1"))  # Azul

    # retângulo que cobre toda a página para definir a cor de fundo
    cnv.rect(0, 0, 2000, 1414, fill=True)

    # retângulo branco que sobrebrepoe o fundo 
    cnv.setFillColor(colors.HexColor("#FFFFFF"))  # Branco
    cnv.rect(150, 100, 1700, 1214, fill=True) #tamanho e posicionamento

    # adicionando a imagem 
    cnv.drawImage("logo.jpg", 920, 930, width=170, height=170)

    # Textos do certificado

    # Texto do centro
    cnv.setFont("LeagueSpartan", 70)  # Tamanho da fonte
    cnv.setFillColor(colors.HexColor("#0058bce1"))  # Cor do texto (azul)
    text_centro = "CERTIFICADO DE PARTICIPAÇÃO"
    cnv.drawString(500, 800, text_centro)

    # Texto subtitulo
    cnv.setFont("GlacialIndifference-Bold", 40)  # Tamanho da fonte
    cnv.setFillColor(colors.black)  # Cor do texto 
    text_sub = "Este certificado vai para"
    cnv.drawString(770, 720, text_sub)

    # Nome da pesoa 
    cnv.setFont("Fontspring-theseasons-lt", 100)  # Tamanho da fonte
    # Centralizar o texto do nome
    text_width = cnv.stringWidth(name, "Fontspring-theseasons-lt", 100)
    x = (2000 - text_width) / 2
    y = (1414 - 100) / 2
    cnv.drawString(x, y - 100, name) # escrever o nome

    # Texto final
    cnv.setFont("GlacialIndifference-Regular", 40)  # Tamanho da fonte
    text_final1 = "Por ter completado os estudos referente ao"
    text_final2 = "método Scrum da plataforma Srun IT."
    #conta para poder alinhar os textos 
    y1 = (1414 - 40) / 2  # Coordenada y da primeira linha
    y2 = y1 - 44  # Coordenada y da segunda linha
    cnv.drawString(650, y1 - 250, text_final1)
    cnv.drawString(700, y2 - 250, text_final2)

    cnv.save()

    return f"Nome '{name}' salvo com sucesso."




app.run(debug=True)