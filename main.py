from src.BancoDados.dbConfig import conectar_bd, consultar_dados, executar_query
from src.Classes import consultaPaciente, exame, paciente

teste = {"nome":"teste", "idade":22, "cpf":"123456", "rg":"2323232", "cep":"030303", "endereco":"av. teste", "complemento":"tes22", "num_casa":"20A", "email":"teste@teste.com", "nome_mae":"teste mae"}

paciente.cadastrar_paciente(teste)