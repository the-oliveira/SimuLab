from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados

def cadastrar_paciente(dados_paciente):
    
    try:
        #Preparar dados para realizar a query
        if len(dados_paciente) > 0:
            queryConstructor = "INSERT INTO pacientes (nome, idade, cpf, rg, cep, endereco, complemento, num_casa, email, nome_mae) " \
                                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",dados_paciente
            executar_query(conectar_bd(), queryConstructor)
            return 'Cadastro realizado com sucesso'

    except:
        return 'Tente novamente'
    
    