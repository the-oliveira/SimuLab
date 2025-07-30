from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Response
import xml.etree.ElementTree as et
#from BancoDados import dbConfig, examesDB, pacientesDB
from src.Classes import exame as exa, paciente as pac
#from utilidades import validadores
import unittest



#teste = {"nome":"teste", "idade":22, "cpf":"123456", "rg":"2323232", "cep":"030303", "endereco":"av. teste", "complemento":"tes22", "num_casa":"20A", "email":"teste@teste.com", "nome_mae":"teste mae"}

#cad_paciente.cadastrar_paciente(teste)
