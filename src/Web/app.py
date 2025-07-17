from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#from BancoDados import dbConfig, examesDB, pacientesDB
from Classes import exame, paciente
#from utilidades import validadores


app = Flask(__name__)


@app.route('/')

def pagina_inicial():
    return 'Ola mundo'


if __name__ == '__main__':
    app.run(debug=True)



@app.route('/pacientes', methods=['GET'])

def get_pacientes():
    dados_pacientes = paciente.Paciente.buscar_todos