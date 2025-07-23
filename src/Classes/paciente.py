from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
import json


class Paciente: 

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


    def salvar(self):
        try:
            #Validação inicial dos dados obrigatórios
            if self.nome and self.idade and self.cpf and self.rg and self.cep and self.endereco and self.num_casa and self.nome_mae:
                #Verificar se o id está definido na chamada para montar os parametros
                if self.id:
                    params = (
                        self.nome,
                        self.idade,
                        self.cpf,
                        self.rg,
                        self.cep,
                        self.endereco,
                        self.complemento,
                        self.num_casa,
                        self.email,
                        self.nome_mae,
                        self.id
                    )
                    query = "UPDATE pacientes SET nome = %s, idade = %s, cpf = %s, rg = %s, cep = %s, endereco = %s, complemento = %s, num_casa = %s, email = %s, nome_mae = %s WHERE id = %s "
                    print('Atualizando dados do paciente.')
                else:
                    params = (
                        self.nome,
                        self.idade,
                        self.cpf,
                        self.rg,
                        self.cep,
                        self.endereco,
                        self.complemento,
                        self.num_casa,
                        self.email,
                        self.nome_mae,
                    )
                    query = "INSERT INTO pacientes (nome, idade, cpf, rg, cep, endereco, complemento, num_casa, email, nome_mae) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    print('Inserindo dados do paciente na tabela.')
  
            else:
                print(f'Dados do paciente vieram incompletos!')
                return None

            res = executar_query(conectar_bd(), query, params)
            
            print(f'Finalizando função Salvar com sucesso. {res}')
            return params
        
        except Exception as e:
            print(f'Erro ao executar cadastro de pacientes {str(e)}')
            return None


    @classmethod
    def buscar_todos(cls):
        query_busca = 'SELECT * FROM pacientes'
        res = consultar_dados(conectar_bd(), query_busca)
        lista_pacientes = []
        if res:
            print(f'Dados obtidos com sucesso')

            for pac in res:
                obj_paciente = Paciente(
                    nome=pac['nome'],
                    idade=pac['idade'],
                    cpf=pac['cpf'],
                    rg=pac['rg'],
                    cep=pac['cep'],
                    endereco=pac['endereco'],
                    complemento=pac['complemento'],
                    num_casa=pac['num_casa'],
                    email=pac['email'],
                    nome_mae=pac['nome_mae'],
                    id=pac['id']
                )
            
                lista_pacientes.append(obj_paciente)
            return lista_pacientes
        else:
            print(f'RES veio sem valores {res}')
            return None
        


    @classmethod
    def buscar_por_cpf(cls, cpf):
        try:
            if cpf:
                #Realiza a consulta de dados baseado no CPF se ele existir
                query_cpf = 'SELECT * FROM pacientes WHERE cpf = %s'
                params = (cpf,)
                res = consultar_dados(conectar_bd(), query_cpf, params)
                print(res)
                if res: 
                    print('Dados retornados com sucesso!')
                    return cls(*res[0])
                else:
                    res = None
                    return res
            else:
                print(f'Erro ao verificar CPF {cpf}')
                return None
        except Exception as e:
            print(f'consulta retornou com erro {str(e)}')
            return None

    @classmethod
    def buscar_por_id(cls, id):
        try:
            if id:
                #Realizar a busca utilizando o id do paciente se ele existir
                query_id = 'SELECT * FROM pacientes WHERE id = %s'
                params = (id,)
                res = consultar_dados(conectar_bd(), query_id, params)
                print(res)
                if res: 
                    print('Dados consultados com sucesso')
                    return cls(*res[0])
                else: 
                    return None
            
            else:
                print(f'Erro ao verificar id {id}')
                return None
        
        except Exception as e:
            print(f'Erro ao consultar dados {str(e)}')
            return None
        
    @classmethod
    def excluir_pac(cls, id, cpf):
        try:
            query_exclusao = 'DELETE FROM pacientes WHERE id = %s AND cpf = %s'
            params = (id, cpf)
            res = executar_query(conectar_bd() ,query_exclusao, params)
            if res:
                print('Exclusão executada com sucesso')
                return True
            else:
                return False
        
        except Exception as e:
            return False
        
    @classmethod
    def atualizar_pac(cls, id, dados_novos):
    
        dados_pac = cls.buscar_por_id(id)
        if dados_pac:

            dados_pac.nome= dados_novos.get('nome', dados_pac.nome)
            dados_pac.idade= dados_novos.get('idade', dados_pac.idade)
            dados_pac.cpf= dados_novos.get('cpf', dados_pac.cpf)
            dados_pac.rg= dados_novos.get('rg', dados_pac.rg)
            dados_pac.cep= dados_novos.get('cep', dados_pac.cep)
            dados_pac.endereco= dados_novos.get('endereco', dados_pac.endereco)
            dados_pac.complemento= dados_novos.get('complemento', dados_pac.complemento)
            dados_pac.num_casa= dados_novos.get('num_casa', dados_pac.num_casa)
            dados_pac.email= dados_novos.get('email', dados_pac.email)
            dados_pac.nome_mae= dados_novos.get('nome_mae', dados_pac.nome_mae)

        else:
            return dados_pac

        try:
            return dados_pac.salvar()

        except Exception as e:
            raise Exception(f'erro ao salvar {e}')