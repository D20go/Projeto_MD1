print('\nINFORMAÇÕES\n')

dados = 0
dados = input('Bem-vindo(a) ao setor de informações da UBS. Digite sua opção de escolha: \n\n 1 - Informações sobre a UBS \n 2 - Retirada de Medicamentos \n 3 - Retirada de Exames \n 4 - Voltar ao menu anterior \n 5 - Sair \n\nDigite aqui: ')

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
        
        if ubs_1 == 1:
           
        elif ubs_1 == 2:
            print('\nEncerrando o programa.')
    
     if infos_ubs == 2:
            print('\nINFORMAÇÕES SOBRE A UBS 2\n \n Endereço: Rua dos Bobos, nº 0 \n Telefone: (00) 0000-0000 \n Horário de atendimento: 24 horas \n')
        ubs_2 = input(' 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
        while not ubs_2.isdigit():
            ubs_2 = input('\nEntrada inválida. Escolha uma opção: \n 1 - Consultar informações sobre outra UBS \n 2 - Sair \n\nDigite aqui: ')
            
        ubs_2 = int(ubs_2)
        
        if ubs_2 == 1:
           
        elif ubs_2 == 2:
            print('\nEncerrando o programa.')
