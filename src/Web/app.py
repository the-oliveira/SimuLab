from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#from BancoDados import dbConfig, examesDB, pacientesDB
from Classes import exame as exa, paciente as pac
#from utilidades import validadores


app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return 'Ola mundo'


@app.route('/pacientes', methods=['GET'])
def get_todos_pacientes():
    try:
        dados = pac.Paciente.buscar_todos()
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({'erro':f'erro interno ao buscar pacientes{str(e)}'}), 500

@app.route('/pacientes/id/<int:id>', methods=['GET'])
def get_paciente_id(id):
    try:
        dados = pac.Paciente.buscar_por_id(id)
        if dados:
            return jsonify(vars(dados)), 200
        else:
            return jsonify({'erro':f'Paciente com id {id} não encontrado!'}), 404
    except Exception as e:
        return jsonify({'erro':f'erro ao buscar paciente por id {str(e)}'}), 500


@app.route('/pacientes/cpf/<str:cpf>', methods=['GET'])
def get_paciente_cpf(cpf):
    try:
        dados = pac.Paciente.buscar_por_cpf(cpf)
        if dados:
            return jsonify(vars(dados)), 200
        else:
            return jsonify({'erro':f'Paciente com cpf {cpf} não encontrado!'}), 404
    
    except Exception as e:
        return jsonify({'erro':f'erro ao buscar paciente por cpf {str(e)}'}), 500


@app.route('/pacientes', methods=['POST'])
def post_paciente():
    dados_pac = request.get_json()
    if not dados_pac:
        return jsonify({'erro':'Dados JSON ausentes'}), 400
    
    try:
        pac_inst = pac.Paciente(
            nome= dados_pac.get('nome'),
            idade= dados_pac.get('idade'),
            cpf= dados_pac.get('cpf'),
            rg= dados_pac.get('rg'),
            cep= dados_pac.get('cep'),
            endereco= dados_pac.get('endereco'),
            complemento= dados_pac.get('complemento'),
            num_casa= dados_pac.get('num_casa'),
            email= dados_pac.get('email'),
            nome_mae= dados_pac.get('nome_mae'),
        )

        salvar_pac = pac_inst.salvar()
        if salvar_pac:
            return jsonify(salvar_pac), 201
        else:
            return jsonify({'erro':'Falha ao salvar paciente'}), 400
        
    except Exception as e:
        return jsonify({'erro':str(e)}, 500)


@app.route('/pacientes/<int:id>', methods=['PUT'])
def put_paciente(id):
    dados_pac_att = request.get_json()
    if not dados_pac_att:
        return jsonify({'erro':'Dados JSON ausentes'}), 400
    
    dados_pac_antigo = pac.Paciente.buscar_por_id(id)
    if dados_pac_antigo:
            pac_inst = pac.Paciente(
                nome= dados_pac_att.get('nome'),
                idade= dados_pac_att.get('idade'),
                cpf= dados_pac_att.get('cpf'),
                rg= dados_pac_att.get('rg'),
                cep= dados_pac_att.get('cep'),
                endereco= dados_pac_att.get('endereco'),
                complemento= dados_pac_att.get('complemento'),
                num_casa= dados_pac_att.get('num_casa'),
                email= dados_pac_att.get('email'),
                nome_mae= dados_pac_att.get('nome_mae'),
                id=dados_pac_antigo.id
        )
    else:
        return jsonify({'erro':f'Paciente id:{id} não encontrado para atualização'}), 404

    try:
        salvar_pac = pac_inst.salvar()
        return jsonify(salvar_pac), 200

    except Exception as e:
        return jsonify(f'erro interno: {str(e)}'), 500


@app.route('/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    dados = request.get_json()
    if not dados:
        return jsonify({'erro':'Dados JSON ausentes.'}), 400
    
    if 'cpf' not in dados:
        return jsonify({'erro':'Dados recebidos não possuem CPF.'}), 400
    cpf = dados.get('cpf')

    try:
        deletar_pac = pac.Paciente.excluir_pac(id, cpf)
        if deletar_pac:
            return jsonify({'res':'Deletado com sucesso.'}), 204    
        else:
            return jsonify({'erro':'Paciente não encontrado ou cpf ausente.'}), 404
    
    except Exception as e:
        return jsonify({'erro':f'Erro ao excluir paciente{e}'}), 500

    



if __name__ == '__main__':
    app.run(debug=True)