from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error

def cadastrar_paciente(dados_paciente):
    try:
        #Preparar dados para realizar a query
        if len(dados_paciente) > 0:
            if dados_paciente['cpf'] and dados_paciente['nome'] and dados_paciente['rg']:
                queryConstructor = "INSERT INTO pacientes (nome, idade, cpf, rg, cep, endereco, complemento, num_casa, email, nome_mae) " \
                                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",dados_paciente
                executar_query(conectar_bd(), queryConstructor)
                return 'Cadastro realizado com sucesso'
            else:
                return f'Dados do paciente vieram incompletos!'
        
        else:
            return f'Dados do paciente vieram incompletos!'

    except Error as e:
        return f'Erro ao executar cadastro de pacientes {e}'


