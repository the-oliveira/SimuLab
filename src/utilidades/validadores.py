from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error


def verificar_consulta(dados_paciente, tipo_consulta):
    try:
        if tipo_consulta == 'cpf':
            cpf = dados_paciente['cpf']
            query_cpf = 'SELECT cpf FROM pacientes WHERE cpf = cpf'
            params = (cpf,)
            res = consultar_dados(conectar_bd(), query_cpf, params)
            print(res)
            if len(res) > 5:
                print('CPF encontrado, seguir com a consulta')
                return True

            else:
                print('CPF não encontrado ou inválido')
                return False
        
        elif tipo_consulta == 'id':
            id = dados_paciente['id']
            query_id = 'SELECT id FROM pacientes WHERE id = id'
            params = (id,)
            res = consultar_dados(conectar_bd(), query_id, params)
            print(res)
            if len(res) > 1:
                print('Id encontrado, seguir com a consulta')
                return True
            else:
                print('Id não encontrado ou inválido')
                return False

    except Error as e:
        return f'Erro ao consultar valores {e}'