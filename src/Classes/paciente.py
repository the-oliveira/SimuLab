from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error


class paciente: 

    def __init__(self, nome = None, idade = None, cpf = None, rg = None, cep = None, endereco = None, complemento = None, num_casa = None, email = None, nome_mae = None, id = None):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.cep = cep
        self.endereco = endereco
        self.complemento = complemento
        self.num_casa = num_casa
        self.email = email
        self.nome_mae = nome_mae
        self.id = id

    
    def cadastrar_paciente(self):
        try:
            #Preparar dados para realizar a query
            if len(self.dados_paciente) > 0:
                if self.dados_paciente.get('cpf') and self.dados_paciente.get('nome') and self.dados_paciente.get('rg'):
                    query = "INSERT INTO pacientes (nome, idade, cpf, rg, cep, endereco, complemento, num_casa, email, nome_mae) " \
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    
                    params = (
                        self.dados_paciente.get('idade'),
                        self.dados_paciente.get('cpf'),
                        self.dados_paciente.get('rg'),
                        self.dados_paciente.get('nome'),
                        self.dados_paciente.get('cep'),
                        self.dados_paciente.get('endereco'),
                        self.dados_paciente.get('complemento'),
                        self.dados_paciente.get('num_casa'),
                        self.dados_paciente.get('email'),
                        self.dados_paciente.get('nome_mae')
                    )
                    executar_query(conectar_bd(), query, params)
                    return 'Cadastro realizado com sucesso'
                else:
                    return f'Dados do paciente vieram incompletos!'
            
            else:
                return f'Dados do paciente vieram incompletos!'

        except Error as e:
            return f'Erro ao executar cadastro de pacientes {e}'


    def consultar_pacientes_cpf(self):
        try:
            cpf = self.dados_paciente
            query_cpf = 'SELECT * FROM pacientes WHERE cpf = %s'
            params = (cpf,)
            res = consultar_dados(conectar_bd(), query_cpf, params)
            print(res)
            if res: print('Dados retornados com sucesso!')
            return res
        
        except Error as e:
            print(f'consulta retornou com erro {e}')


    def consultar_pacientes_ra(self):
        try:
            ra = self.dados_paciente
            query_ra = 'SELECT * FROM pacientes WHERE id = %s'
            params = (ra,)
            res = consultar_dados(conectar_bd(), query_ra, params)
            print(res)
            if res: print('Dados consultados com sucesso')
            return res
        
        except Error as e:
            print(f'Erro ao consultar dados {e}')