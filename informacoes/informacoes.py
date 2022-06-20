print('\nINFORMAÇÕES\n')

dados = input('Bem-vindo(a) ao setor de informações da UBS. Digite sua opção de escolha: \n\n 1 - Informações sobre a UBS \n 2 - Retirada de Medicamentos \n 3 - Retirada de Exames \n 4 - Voltar ao menu anterior \n 5 - Sair \n\nDigite aqui: ')

while not dados.isdigit():
    dados = input('\nEntrada inválida. Digite sua opção de escolha: \n\n 1 - Informações sobre a UBS \n 2 - Retirada de Medicamentos \n 3 - Retirada de Exames \n 4 - Voltar ao menu anterior \n 5 - Sair \n\nDigite aqui: ')  
    
dados = int(dados)
    
if dados == 1:
    infos_ubs = input('\nEscolha a UBS que deseja informações: \n 1 - UBS 1 \n 2 - UBS 2 \n 3 - UBS 3 \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ')
    while not infos_ubs.isdigit():
        dados = input('\nEntrada inválida. Escolha a UBS que deseja informações: \n 1 - UBS 1 \n 2 - UBS 2 \n 3 - UBS 3 \n 4 - Voltar ao menu anterior \n 5 - Sair \nDigite aqui: ') 
         
    if infos_ubs == 1:
        ubs_infos = input('Gostaria de qual informação sobre a UBS? \n\n 1 - Endereço \n 2 - Tempo de Espera \n 3 - Horário de Funcionamento \n 4 - Voltar ao menu anterior \n 5 - Sair \n\nDigite aqui: ')
        print(ubs_infos)