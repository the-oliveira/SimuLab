from src.BancoDados.dbConfig import conectar_bd, executar_query, consultar_dados
from mysql.connector import Error


def consultar_exames(cpf, data):
    try:
        query_consulta_exame = "SELECT * FROM exames WHERE cpf = cpf anda data_cadastro = data" \
                                "VALUES (%s, %s)"
        params = (
            cpf,
            data
        )
        res = consultar_dados(conectar_bd(), query_consulta_exame, params)
        if res: 
            print('Consulta realizada com sucesso')
            return res
        else:
            return 'Consulta não retornou dados! Verifique novamente'
    except Error as e:
        return f'Errou ao tentar relizar consulta dos exames {e}'
 