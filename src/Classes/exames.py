from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error
from datetime import datetime


def cadastrar_exames(ra):
    try:
        nom_exame = input('Nome do Exame: ')
        data_exame = 'Data que deverá realizar o exame: '
        data_cadastro = datetime.today()
        query_exame = f'INSERT INTO exames (nom_exame, data_exame, data_cadastro) VALUES ({nom_exame}, {data_exame}, {data_cadastro}) WHERE ra = {ra}'
        res = executar_query(conectar_bd(), query_exame)
        if 'Erro' not in res:
            print('Exame cadastrado!')
        return res
    
    except Error as e:
        return f'Erro ao cadastrar exame: {e}'