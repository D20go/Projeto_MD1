def informacoes ():

    print('\nINFORMAÇÕES\n')

    dados = input('Bem-vindo(a) ao setor de informações. Digite sua opção de escolha: \n\n 1 - Informações sobre a UBS \n 2 - Retirada de Medicamentos \n 3 - Retirada de Exames \n 4 - Voltar ao menu anterior \n 5 - Sair \n\nDigite aqui: ')

    while not dados.isdigit():
        dados = input('\nEntrada inválida. Digite sua opção de escolha: \n\n 1 - Informações sobre a UBS \n 2 - Retirada de Medicamentos \n 3 - Retirada de Exames \n 4 - Voltar ao menu anterior \n 5 - Sair \n\nDigite aqui: ')  
        
    dados = int(dados)
        
    if dados == 1:
        infos_ubs = input('\nEscolha a UBS que deseja informações: \n 1 - UBS 1 \n 2 - UBS 2 \n 3 - UBS 3 \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ')
        while not infos_ubs.isdigit():
            infos_ubs = input('\nEntrada inválida. Escolha a UBS que deseja informações: \n 1 - UBS 1 \n 2 - UBS 2 \n 3 - UBS 3 \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ') 
            
        infos_ubs = int(infos_ubs)
        
        if infos_ubs == 1:
            print('\nINFORMAÇÕES SOBRE A UBS 1\n \n Endereço: Rua dos Bobos, nº 0 \n Telefone: (00) 0000-0000 \n Horário de atendimento: 24 horas \n')
            ubs_1 = input(' 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
            while not ubs_1.isdigit():
                ubs_1 = input('\nEntrada inválida. Escolha uma opção: \n 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
                
            ubs_1 = int(ubs_1)
            # if ubs_1 == 1:
            
            # elif ubs_1 == 2:
            #     print('\nEncerrando o programa.')
        elif infos_ubs == 2:
            print('\nINFORMAÇÕES SOBRE A UBS 2\n \n Endereço: Rua dos Bobos, nº 100 \n Telefone: (00) 0000-0000 \n Horário de atendimento: 24 horas \n')
            ubs_2 = input(' 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
            while not ubs_2.isdigit():
                ubs_2 = input('\nEntrada inválida. Escolha uma opção: \n 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
                
            ubs_2 = int(ubs_2)
            # if ubs_2 == 1:
            
            # elif ubs_2 == 2:
            #     print('\nEncerrando o programa.')    
        elif infos_ubs == 3:
            print('\nINFORMAÇÕES SOBRE A UBS 2\n \n Endereço: Rua dos Bobos, nº 200 \n Telefone: (00) 0000-0000 \n Horário de atendimento: 24 horas \n')
            ubs_3 = input(' 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
            while not ubs_3.isdigit():
                ubs_3 = input('\nEntrada inválida. Escolha uma opção: \n 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
                
            ubs_3 = int(ubs_3)
            # if ubs_3 == 1:
            
            # elif ubs_3 == 2:
            #     print('\nEncerrando o programa.')
            
        else:
            infos_ubs = input('\nEntrada inválida. Escolha a UBS que deseja informações: \n 1 - UBS 1 \n 2 - UBS 2 \n 3 - UBS 3 \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ')

    elif dados == 2:
        print('\nRETIRADA DE MEDICAMENTOS\n')
        
        medicamento = input('Qual o medicamento que deseja retirar? \n 1 - Paracetamol \n 2 - Ibuprofeno \n 3 - Cetirizina \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ')
        while not medicamento.isdigit():
            medicamento = input('\nEntrada inválida. Qual o medicamento que deseja retirar? \n 1 - Paracetamol \n 2 - Ibuprofeno \n 3 - Cetirizina \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ') 
        
        medicamento = int(medicamento)
        
        if medicamento == 1:
            print('\nA retirada do medicamento foi realizada com sucesso. Aguarde novas informações.\n')
        elif medicamento == 2:
            print('\nMedicamento não disponível no momento. Aguarde novas informações.\n')
        elif medicamento == 3:
            print('\nA retirada do medicamento foi agendada com sucesso. Aguarde novas informações.\n')
        elif medicamento == 4:
            print('\nEncerrando o programa.')
        elif medicamento == 5:
            print('\nEncerrando o programa.')
        else:
            print('\nEntrada inválida. Encerrando o programa.\n')
        
    elif dados == 3:
        print('\nRETIRADA DE EXAMES\n')
        
        exames = input('Qual exame deseja retirar? \n 1 - Exame de sangue \n 2 - Exame de urina \n 3 - Exame de óculos \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ')
        while not exames.isdigit():
            exames = input('\nEntrada inválida. Qual exame deseja retirar? \n 1 - Exame de sangue \n 2 - Exame de urina \n 3 - Exame de óculos \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ') 
        
        exames = int(exames)
        
        if exames == 1:
            print('\nA retirada do exame foi realizada com sucesso. Aguarde novas informações.\n')
        elif exames == 2:
            print('\nResultado do exame não disponível no momento. Aguarde novas informações.\n')
        elif exames == 3:
            print('\nA retirada do exame foi agendada com sucesso. Aguarde novas informações.\n')
        elif exames == 4:
            print('\nEncerrando o programa.')
        elif exames == 5:
            print('\nEncerrando o programa.')
        else:
            print('\nEntrada inválida. Encerrando o programa.\n')
            
    # elif dados == 4:

    elif dados == 5:
        print('\nEncerrando o programa.')
        
    else:
        dados = input('\nEntrada inválida. Digite sua opção de escolha: \n\n 1 - Informações sobre a UBS \n 2 - Retirada de Medicamentos \n 3 - Retirada de Exames \n 4 - Voltar ao menu anterior \n 5 - Sair \n\nDigite aqui: ')  
        
informacoes()