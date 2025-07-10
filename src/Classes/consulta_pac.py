from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error


    
def consultar_pacientes_cpf(dados_paciente):
    try:
        cpf = dados_paciente
        query_cpf = 'SELECT * FROM pacientes WHERE cpf = %s'
        params = (cpf,)
        res = consultar_dados(conectar_bd(), query_cpf, params)
        print(res)
        if res: print('Dados retornados com sucesso!')
        return res
    
    except Error as e:
        print(f'consulta retornou com erro {e}')


def consultar_pacientes_ra(dados_paciente):
    try:
        ra = dados_paciente
        query_ra = 'SELECT * FROM pacientes WHERE id = %s'
        params = (ra,)
        res = consultar_dados(conectar_bd(), query_ra, params)
        print(res)
        if res: print('Dados consultados com sucesso')
        return res
    
    except Error as e:
        print(f'Erro ao consultar dados {e}')