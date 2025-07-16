from Classes import paciente
from Classes import exame
from src.BancoDados.dbConfig import conectar_bd, consultar_dados, executar_query
from src.Classes import consulta_pac
from mysql.connector import Error



consulta_pac.consultar_pacientes_cpf('123456')