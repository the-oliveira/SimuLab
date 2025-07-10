from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error

def cadastrar_paciente(dados_paciente):
    try:
        #Preparar dados para realizar a query
        if len(dados_paciente) > 0:
            if dados_paciente.get('cpf') and dados_paciente.get('nome') and dados_paciente.get('rg'):
                query = "INSERT INTO pacientes (nome, idade, cpf, rg, cep, endereco, complemento, num_casa, email, nome_mae) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                
                params = (
                    dados_paciente.get('nome'),
                    dados_paciente.get('idade'),
                    dados_paciente.get('cpf'),
                    dados_paciente.get('rg'),
                    dados_paciente.get('cep'),
                    dados_paciente.get('endereco'),
                    dados_paciente.get('complemento'),
                    dados_paciente.get('num_casa'),
                    dados_paciente.get('email'),
                    dados_paciente.get('nome_mae')
                )
                executar_query(conectar_bd(), query, params)
                return 'Cadastro realizado com sucesso'
            else:
                return f'Dados do paciente vieram incompletos!'
        
        else:
            return f'Dados do paciente vieram incompletos!'

    except Error as e:
        return f'Erro ao executar cadastro de pacientes {e}'


