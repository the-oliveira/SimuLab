from flask import Flask, render_template, request, redirect, url_for, flash
from BancoDados import dbConfig, examesDB, pacientesDB
from Classes import consulta_exame, consulta_pac, exame, paciente
from utilidades import validadores


