from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from datetime import datetime


class Exame:

    def __init__(self, id_exame = None, nom_exame = None, data = None, status = None, paciente_id = None ):
        self.id_exame = id_exame
        self.nom_exame = nom_exame
        self.data = data
        self.status = status
        self.paciente_id = paciente_id


    def salvar(self):
        try:
            if self.nom_exame and self.status and self.paciente_id:
                if self.id_exame:
                    query_exame = "UPDATE exames SET nom_exame = %s, data_cadastro = %s, status = %s, paciente_id = %s where id_exame = %s "
                    params = (
                        self.nom_exame,
                        self.data,
                        self.status,
                        self.paciente_id,
                        self.id_exame
                    )
                else:
                    data_cadastro = datetime.today()
                    query_exame = "INSERT INTO exames (nom_exame, data_cadastro, status, paciente_id) " \
                                    "VALUES (%s, %s, %s, %s)"
                    params = (
                        self.nom_exame,
                        data_cadastro,
                        self.status,
                        self.paciente_id
                    )
                
                res = executar_query(conectar_bd(), query_exame, params)
                print(f'Dados salvos com sucesso! {res}')
                return None

            else:
                print('Dados de exame incompletos')
                return None
            
        except Exception as e:
            print(f'DEBUG: Erro ao cadastrar exame: {str(e)}')
            return None
        

    @classmethod
    def buscar_exame_por_id(cls, id_exame, data):
        try:
            query_consulta_exame = "SELECT * FROM exames WHERE id_exame = %s and data_cadastro = %s"
            params = (
                id_exame,
                data
            )
            res = consultar_dados(conectar_bd(), query_consulta_exame, params)
            if res: 
                print('Consulta realizada com sucesso')
                return cls(*res[0])
            else:
                print('Consulta não retornou dados! Verifique novamente')
                return None
        except Exception as e:
            print(f'Erro ao tentar relizar consulta de exames {str(e)}')
            return None
        

    @classmethod
    def buscar_exame_por_paciente(cls, paciente_id, data):
        try:
            query_consulta_exame = "SELECT * FROM exames WHERE paciente_id = %s and data_cadastro = %s"
            params = (
                paciente_id,
                data
            )
            res = consultar_dados(conectar_bd(), query_consulta_exame, params)
            
            if res:
                print('Consulta realizada com sucesso')
                return cls(*res[0])
            else:
                print('Consulta não retornou dados! Verifique novamente')
                return None
        
        except Exception as e:
            print(f'Erro ao tentar relizar consulta de exames {str(e)}')
            return None