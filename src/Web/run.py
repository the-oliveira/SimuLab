from flask import Flask, render_template, request, redirect, url_for, flash
from BancoDados import dbConfig, examesDB, pacientesDB
from Classes import cad_exames, cad_paciente, consulta_exame, consulta_pac
from utilidades import validadores


