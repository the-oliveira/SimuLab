from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error
from datetime import datetime


def cadastrar_exames(nom_exame, cpf):
    try:
        data_cadastro = datetime.today()
        query_exame = f'INSERT INTO exames (cpf, nom_exame, data_cadastro) VALUES ({cpf}, {nom_exame}, {data_cadastro})'
        res = executar_query(conectar_bd(), query_exame)
        if 'Erro' not in res:
            print('Exame cadastrado!')
        return res
    
    except Error as e:
        return f'Erro ao cadastrar exame: {e}'
    
