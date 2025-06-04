import mysql.connector
from mysql.connector import Error

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='adminLab',
            password='123',
            database='simulab_db'
        )
        
        if conn.is_connected():
            #Conexão feita com sucesso
            return conn
    except Error as e:
        print(f'Erro ao conectar com o banco de dados {e}')
        return None
    

def executar_query(conexao, query, params=None):
    cursor = None
    try:
        if conexao and conexao.is_connected():
            cursor = conexao.cursor(dictionary = True) #Para retornar dicionarios como resultado
            cursor.execute(query, params or ())
            conexao.commit() 

    except Error as e:
        print(f'Erro ao executar query: {e}')
        if conexao:
            conexao.rollback()
            return None
    finally:
        if cursor:
            cursor.close()
    return None


def consultar_dados(conexao, query, params=None):
    cursor = None
    try:
        if conexao and conexao.is_connected():
            cursor = conexao.cursor(dictionary = True)
            cursor.execute(query, params or ())
            resultados = cursor.fetchall()
            return resultados
    
    except Error as e:
        print('Erro ao executar query de consulta: {e}')
    
    finally:
        if cursor:
            cursor.close()
    
    return None