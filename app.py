#importando as bibliotecas 
from flask import Flask, render_template, request
import pandas as pd
app= Flask(__name__)
pessoas = []
bd= 'pessoas.json'
#Criando rota do html
@app.route('/')
def home():
    return render_template('home.html', pessoas=pessoas)

app.run(debug=True)