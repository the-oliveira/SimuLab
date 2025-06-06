#inicio
#Menu com opções |Cadastro| ou |Consulta|
    #cadastro
        #coletar dados do PACIENTE
            #Nome, idade, CPF, RG, RA, CEP, endereço, complemento, numero_casa, nome_mãe
            #Cadastrar EXAMES ou Salvar e sair
                #Cadastrar EXAMES
                    #Adiciona o nome e a sigla do exame e data prevista para realizar
                        #Opção de adicionar mais exames
                            #Quando finalizar, selecionar Salvar
                                #MENU PRINCIPAL
                        #OPção de Salvar e finalizar
                            #Salva no BD e Finaliza
                                #MENU PRINCIPAL
                #Salvar e Sair
                    #Caso não tenha exames para adicionar
                        #MENU PRINCIPAL
    #consultar dados
        #dados por CPF
            #Verifica se o CPF está cadastrado
                #Se sim:
                    #Visualiza dados do paciente e exames 
                        #Adicionar exames
                            #Direciona para tela de exames
                        
                        #Editar dados do paciente
                        
                        #Excluir paciente
                        
                        #Voltar para o menu
                            #MENU PRINCIPAL
                #Se não: 
                    #Mensagem de não encontrado.
        #dados por RA
            #Verifica se o RA está cadastrado
                #Se sim: 
                    #Visualiza dados do paciente e exames 
                    
                    #Adicionar exames
                        #Direciona para tela de exames
                    
                    #Editar dados do paciente

                    #Excluir paciente
                    
                    #Voltar para o menu
                        #MENU PRINCIPAL
                #Se não:
                    #Mensagem de não encontrado.