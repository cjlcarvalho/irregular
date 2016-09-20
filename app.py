# -*- coding: utf8 -*-
from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from random import randint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app) 

db = SQLAlchemy(app)

class Question(db.Model):
    __tablename__ = 'questao'
    
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pergunta = db.Column(db.String(80), unique=True)
    resposta = db.Column(db.String(120), unique=True)

    def __init__(self, pergunta, resposta):
        self.pergunta = pergunta
        self.resposta = resposta

db.create_all()

verbs = [['awake', 'awoke'], ['be', 'was/were'], ['beat', 'beat'], ['become', 'became'], ['begin', 'began'], ['bend', 'bent'], ['bet', 'bet'], ['bid', 'bid'], ['bite', 'bit'], ['blow', 'blew'], ['break', 'broke'], ['bring', 'brought'], ['broadcast', 'broadcast'], ['build', 'built'], ['burn', 'burned/burnt'], ['buy', 'bought'], ['catch', 'caught'], ['choose', 'chose'], ['come', 'came'], ['cost', 'cost'], ['cut', 'cut'], ['dig', 'dug'], ['do', 'did'], ['draw', 'drew'], ['dream', 'dreamed/dreamt'], ['drive', 'drove'], ['drink', 'drank'], ['eat', 'ate'], ['fall', 'fell'], ['feel', 'felt'], ['fight', 'fought'], ['find', 'found'], ['fly', 'flew'], ['forget', 'forgot'], ['forgive', 'forgave'], ['freeze', 'froze'], ['get', 'got'], ['give', 'gave'], ['go', 'went'], ['grow', 'grew'], ['hang', 'hung'], ['have', 'had'], ['hear', 'heard'], ['hide', 'hid'], ['hit', 'hit'], ['hold', 'held'], ['hurt', 'hurt'], ['keep', 'kept'], ['know', 'knew'], ['lay', 'laid'], ['lead', 'led'], ['learn', 'learned/learnt'], ['leave', 'left'], ['lend', 'lent'], ['let', 'let'], ['lie', 'lay'], ['lose', 'lost'], ['make', 'made'], ['mean', 'meant'], ['meet', 'met'], ['pay', 'paid'], ['put', 'put'], ['read', 'read'], ['ride', 'rode'], ['ring', 'rang'], ['rise', 'rose'], ['run', 'ran'], ['say', 'said'], ['see', 'saw'], ['sell', 'sold'], ['send', 'sent'], ['show', 'showed'], ['shut', 'shut'], ['sing', 'sang'], ['sink', 'sank'], ['sit', 'sat'], ['sleep', 'slept'], ['speak', 'spoke'], ['spend', 'spent'], ['stand', 'stood'], ['stink', 'stank'], ['swim', 'swam'], ['take', 'took'], ['teach', 'taught'], ['tear', 'tore'], ['tell', 'told'], ['think', 'thought'], ['throw', 'threw'], ['understand', 'understood'], ['wake', 'woke'], ['wear', 'wore'], ['win', 'won'], ['write', 'wrote']]

for verb in verbs:
    v = Question(verb[0], verb[1])
    db.session.add(v)
db.session.commit()

@app.cache.memoize(50)
def random():
    num = Question.query.filter_by(_id=randint(1, len(verbs))).first()
    return num

@app.route('/question', methods=["GET", "POST"])
def question():
<<<<<<< HEAD
    
    questao = random()
=======
    questao = Question.query.filter_by(_id=random()).first()
>>>>>>> 84b08c7bd9847af08c0f09590130d7e45816b9fe
    pergunta = questao.pergunta
    session['correto'] = questao.resposta

    if request.method == "POST":
        resposta = request.form['resposta']
        session['resposta'] = resposta
        return redirect(url_for('answer'))
    
    return render_template('question.html', questao=pergunta.upper())

@app.route('/answer')
def answer():
    r = session.get('correto')
    s = session.get('resposta')
    app.cache.delete_memoized(random)
    if r == s:
        valida = True 
    else:
        valida = False

    return render_template('answer.html', valida=valida, correto=r, resposta=s)

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(port=8080, debug=True, host='0.0.0.0')
