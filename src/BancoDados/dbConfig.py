import mysql.connector
from mysql.connector import Error
import os


"""
def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('host'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            database=os.getenv('database')
        )

        if conn.is_connected():
            #Conexão feita com sucesso
            print('Conexão bem sucedida')
            return conn
    except Error as e:
        print(f'Erro ao conectar com o banco de dados {e}')
        return None
"""
    

def executar_query(conexao, query, params=None):
    cursor = None
    try:
        if conexao and conexao.is_connected():
            cursor = conexao.cursor(dictionary = True) #Para retornar dicionarios como resultado
            cursor.execute(query, params or ())
            conexao.commit()
            print('Query executada com sucesso') 
            return True

    except Error as e:
        print(f'Erro ao executar query: {e}')
        if conexao:
            conexao.rollback()
            return False
    finally:
        if cursor:
            cursor.close()
            print('Cursor fechado, executar query finalizado.')
    return False


def consultar_dados(conexao, query, params=None):
    cursor = None
    try:
        if conexao and conexao.is_connected():
            cursor = conexao.cursor(dictionary = True)
            cursor.execute(query, params or ())
            resultados = cursor.fetchall()
            print('Consulta de dados finalizada com sucesso')
            return resultados
    
    except Error as e:
        print(f'Erro ao executar query de consulta: {e}')
    
    finally:
        if cursor:
            cursor.close()
    
    return None