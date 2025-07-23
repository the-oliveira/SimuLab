from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Response
import xml.etree.ElementTree as et
#from BancoDados import dbConfig, examesDB, pacientesDB
from src.Classes import exame as exa, paciente as pac

#from utilidades import validadores


app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return 'Ola mundo'


@app.route('/pacientes', methods=['GET'])
def get_todos_pacientes():
    try:
        dados = pac.Paciente.buscar_todos()
        return [vars(pac) for pac in dados], 200
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


@app.route('/pacientes/cpf/<cpf>', methods=['GET'])
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
        return jsonify({'erro':str(e)}), 500


@app.route('/pacientes/<int:id>', methods=['PUT'])
def atualizar_paciente(id):
    dados_pac_att = request.get_json()
    if not dados_pac_att:
        return jsonify({'erro':'Dados JSON ausentes'}), 400
    
    try:
        atualiPac = pac.Paciente.atualizar_pac(id, dados_pac_att)
        return jsonify(atualiPac), 200

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

    
@app.route('/web/pacientes', methods=['GET'])
def  list_pac():
    try:
        lista_pacientes = pac.Paciente.buscar_todos()
        
        return render_template('pacientes.html', pacientes = lista_pacientes)
    
    except Exception as e:
        return jsonify({'erro':f'erro ao listar pacientes {e}'}), 500


@app.route('/web/pacientes/novo', methods=['GET'])
def novo_pac():
    try:
        return render_template('form_paciente.html')
    
    except Exception as e:
        return jsonify({'erro':f'erro ao cadastrar novo paciente {e}'}), 500
    

@app.route('/web/pacientes/editar/<int:id>', methods=['GET'])
def editar_pac(id):
    try:
        buscar_paciente = pac.Paciente.buscar_por_id(id)
        if buscar_paciente:
            return render_template('form_paciente.html', paciente = buscar_paciente)
        else:
            return 'Paciente não encontrado', 404

    except Exception as e:
        return jsonify({'erro':f'erro ao cadastrar novo paciente {e}'}), 500


@app.route('/pacientes/<int:id>/exames', methods=['POST'])
def atribuir_exame(id):
    dados_exames = request.get_json()
    if not dados_exames:
        return jsonify({'erro':'Dados JSON ausentes'}), 400
    
    validar_paciente = pac.Paciente.buscar_por_id(id)
    if validar_paciente == None:
        return jsonify({'erro':'ID não atribuido a paciente.'}), 404

    try:
        exames_inst = exa.Exame(
            id_exame = dados_exames.get('id_exame'),
            nom_exame = dados_exames.get('nom_exame'),
            data = dados_exames.get('data'),
            status = dados_exames.get('status'),
            paciente_id = id
        )
    
        salvar_exam_pac = exames_inst.salvar_exam()

        if salvar_exam_pac:
            return jsonify(salvar_exam_pac), 201
        else:
            return jsonify({'erro':'Falha ao salvar exames'}), 400
    
    except Exception as e:
        return jsonify({'erro':f'{str(e)}'}), 500


@app.route('/pacientes/<int:paciente_id>/exames', methods=['GET'])
def procurar_exames_pac(paciente_id):
    try:
        dados_exame = exa.Exame.buscar_exame_por_paciente(paciente_id)
        return jsonify([exame.to_dict() for exame in dados_exame]), 200
    
    except Exception as e:
        return jsonify({'erro':f'erro interno ao buscar pacientes {str(e)}'}), 500


@app.route('/exames/<int:id>/pedido.xml', methods=['GET'])
def exame_xml(id):
    try:
        dados_exame = exa.Exame.buscar_exame_por_id(id)
        if dados_exame is None:
            return jsonify({'erro':'exame não encontrado'}), 404

        dados_paciente = pac.Paciente.buscar_por_id(dados_exame.paciente_id)
        if dados_paciente is None:
            return jsonify({'erro':'ID do paciente incorreto ou não encontrado.'}), 404

        #Montar a estrutura do XML
        raiz_pedido = et.Element("pedido_exame")
        raiz_pedido.set("id_exame", str(dados_exame.id_exame))
        
        #Construir a tag de paciente
        elemento_paciente = et.SubElement(raiz_pedido, "paciente")
        elemento_paciente.set("id", str(dados_paciente.id))
        et.SubElement(elemento_paciente, "nome").text = str(dados_paciente.nome) if dados_paciente.nome is not None else ""
        et.SubElement(elemento_paciente, "idade").text = str(dados_paciente.idade) if dados_paciente.idade is not None else ""
        et.SubElement(elemento_paciente, "cpf").text = str(dados_paciente.cpf) if dados_paciente.cpf is not None else ""
        et.SubElement(elemento_paciente, "rg").text = str(dados_paciente.rg) if dados_paciente.rg is not None else ""
        et.SubElement(elemento_paciente, "cep").text = str(dados_paciente.cep) if dados_paciente.cep is not None else ""
        et.SubElement(elemento_paciente, "endereco").text = str(dados_paciente.endereco) if dados_paciente is not None else ""
        et.SubElement(elemento_paciente, "complemento").text = str(dados_paciente.complemento) if dados_paciente.complemento is not None else ""
        et.SubElement(elemento_paciente, "num_casa").text = str(dados_paciente.num_casa) if dados_paciente.num_casa is not None else ""
        et.SubElement(elemento_paciente, "email").text = str(dados_paciente.email) if dados_paciente.email is not None else ""
        et.SubElement(elemento_paciente, "nome_mae").text = str(dados_paciente.nome_mae) if dados_paciente.nome_mae is not None else ""

        #Construir a tag de exame
        elemento_exame = et.SubElement(raiz_pedido, "exame")
        et.SubElement(elemento_exame, "nom_exame").text = str(dados_exame.nom_exame) if dados_exame.nom_exame is not None else ""
        et.SubElement(elemento_exame, "data").text = dados_exame.data.isoformat() if dados_exame.data is not None else ""
        et.SubElement(elemento_exame, "status").text = str(dados_exame.status) if dados_exame.status is not None else ""

        xml_string = et.tostring(raiz_pedido, encoding='unicode', pretty_print=True)

        return Response(xml_string, mimetype='application/xml')

    except Exception as e:
        return jsonify({'erro':f'erro ao construir XML {str(e)}'}), 500
    
if __name__ == '__main__':
    app.run(debug=True)