from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error


    
def consultar_pacientes_cpf(dados_paciente):
    try:
        cpf = dados_paciente['cpf']
        query_cpf = f'SELECT * FROM pacientes WHERE cpf = {cpf}'
        res = consultar_dados(conectar_bd(), query_cpf)
        print(res)
        if res: print('Dados retornados com sucesso!')
        return res
    
    except Error as e:
        print(f'consulta retornou com erro {e}')


def consultar_pacientes_ra(dados_paciente):
    try:
        ra = dados_paciente['ra']
        query_ra = f'SELECT * FROM pacientes WHERE id = {ra}'
        res = consultar_dados(conectar_bd(), query_ra)
        print(res)
        if res: print('Dados consultados com sucesso')
        return res
    
    except Error as e:
        print(f'Erro ao consultar dados {e}')