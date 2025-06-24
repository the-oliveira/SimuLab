from Classes import cad_exames, cad_paciente
from src.BancoDados.dbConfig import conectar_bd, consultar_dados, executar_query
from Classes import consulta_pac
from mysql.connector import Error
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("SimuLab"),
    autoescape=select_autoescape()
)

teste = {"nome":"teste", "idade":22, "cpf":"123456", "rg":"2323232", "cep":"030303", "endereco":"av. teste", "complemento":"tes22", "num_casa":"20A", "email":"teste@teste.com", "nome_mae":"teste mae"}

cad_paciente.cadastrar_paciente(teste)
