import random
import calendar
import funcoes as f

check = 0
escolha_usuario = []

nome = input(f'\nBem-vindo(a). Para iniciar o atendimento, insira seu nome: ')
        
while check == 0:

    start = input(f'\nBem-vindo (a) {nome} ao chatbot do Atende+. O que deseja fazer?\n\n1 - Consultas \n2 - Resultados \n3 - Exames \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')

    while not start.isdigit():
            start = input('\nEntrada inválida. O que deseja fazer?\n\n1 - Consultas \n2 - Resultados \n3 - Exames \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')  
    start = int(start)

    ## Consultas - Diego
    if start == 1:
        
        aa = 2022
        mm = 7
        hr1 = '08:00 h'
        hr2 = '12:00 h'
        hr3 = '13:30 h'
        espec_1 = 'Obstetra'
        espec_2 = 'Clínico Geral'
        espec_3 = 'Dentista'
        hr4 = '07:00 h'
        hr5 = '09:45 h'

        print(("\nBem-vindo(a) ao aplicativo móvel Atende +").upper())

        def consulta():
            print(f"\nOlá {nome}, bem vindo ao Atende +, nosso portal de comunicação com o usuário. Por favor, digite sua escolha abaixo.")
            
            usuario = input(f"\nO que deseja fazer?\n\n1 - Marcar consulta \n2 - Reagendar Consulta \n3 - Voltar ao menu principal \n\nDigite aqui: ")
            while not usuario.isdigit():
                usuario = input('\nEntrada inválida. O que deseja fazer?\n\n1 - Marcar consulta \n2 - Reagendar Consulta \n3 - Voltar ao menu principal \n\nDigite aqui:') 
            
            usuario = int(usuario)          

            if usuario == 1:
                usuario_digita = input("\nDigite a especialidade desejada: \n\n1 - Obstetra \n2 - Clínico Geral \n3 - Dentista \n\nDigite aqui: ")
                
                while not usuario_digita.isdigit():
                    usuario_digita = input('\nEntrada inválida. Digite a especialidade desejada: \n\n1 - Obstetra \n2 - Clínico Geral \n3 - Dentista \n\nDigite aqui: ') 
            
                usuario_digita = int(usuario_digita)
                
                usuario_dict = {1:'Obstetra', 2:'Clínico Geral', 3:'Dentista'}

                if usuario_digita == 1:
                    
                    print(f"\nAbaixo, escolha o dia da consulta \n\n {calendar.month(aa,mm)}")
                    escolha_usuario = input('Digite um dia em formato dd: ')
                    
                    while not escolha_usuario.isdigit():
                        escolha_usuario = input('\nEntrada inválida. Digite um dia em formato dd: ') 
            
                    escolha_usuario = int(escolha_usuario)

                    hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                    
                    while not hora.isdigit():
                        hora = input('\nEntrada inválida. Escolha uma opção de horário: \n\n1 - 08:00 h \n2 - 12:00 h \n3 - 13:00 h \n\nDigite aqui: ') 
            
                    hora = int(hora)
                    
                    hora_dict = {1:'08:00 h', 2:'12:00 h', 3:'13:30 h'}
                    
                    if hora == 1:
                        print (f"\n{nome}, sua consulta com {espec_1} foi agendada para {escolha_usuario}/07 às {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")   
                        
                        f.fim_programa()                  
                    elif hora == 2:
                        print (f"\n{nome}, sua consulta com {espec_1} foi agendada para {escolha_usuario}/07 às {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        
                        f.fim_programa()
                    elif hora == 3:
                        print (f"\n{nome}, sua consulta com {espec_1} foi agendada para {escolha_usuario}/07 às {hora_dict[3]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    else:
                        hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                    
                elif usuario_digita == 2:
                    
                    print(f"\nAbaixo, escolha o dia da consulta \n\n {calendar.month(aa,mm)}")
                    escolha_usuario = input('Digite um dia em formato dd: ')
                    
                    while not escolha_usuario.isdigit():
                        escolha_usuario = input('\nEntrada inválida. Digite um dia em formato dd: ') 
            
                    escolha_usuario = int(escolha_usuario)

                    hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                    
                    while not hora.isdigit():
                        hora = input('\nEntrada inválida. Escolha uma opção de horário: \n\n1 - 08:00 h \n2 - 12:00 h \n3 - 13:00 h \n\nDigite aqui: ') 
            
                    hora = int(hora)
                    
                    hora_dict = {1:'08:00 h', 2:'12:00 h', 3:'13:30 h'}
                    
                    if hora == 1:
                        print (f"\n{nome}, sua consulta com {espec_2} foi agendada para {escolha_usuario}/07 às {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    elif hora == 2:
                        print (f"\n{nome}, sua consulta com {espec_2} foi agendada para {escolha_usuario}/07 às {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    elif hora == 3:
                        print (f"\n{nome}, sua consulta com {espec_2} foi agendada para {escolha_usuario}/07 às {hora_dict[3]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    else:
                        hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                    
                elif usuario_digita == 3:
                    
                    print(f"\nAbaixo, escolha o dia da consulta \n\n {calendar.month(aa,mm)}")
                    escolha_usuario = input('Digite um dia em formato dd: ')
                    
                    while not escolha_usuario.isdigit():
                        escolha_usuario = input('\nEntrada inválida. Digite um dia em formato dd: ') 
            
                    escolha_usuario = int(escolha_usuario)

                    hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                    
                    while not hora.isdigit():
                        hora = input('\nEntrada inválida. Escolha uma opção de horário: \n\n1 - 08:00 h \n2 - 12:00 h \n3 - 13:00 h \n\nDigite aqui: ') 
            
                    hora = int(hora)
                    
                    hora_dict = {1:'08:00 h', 2:'12:00 h', 3:'13:30 h'}
                    
                    if hora == 1:
                        print (f"\n{nome}, sua consulta com {espec_3} foi agendada para {escolha_usuario}/07 às {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    elif hora == 2:
                        print (f"\n{nome}, sua consulta com {espec_3} foi agendada para {escolha_usuario}/07 às {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    elif hora == 3:
                        print (f"\n{nome}, sua consulta com {espec_3} foi agendada para {escolha_usuario}/07 às {hora_dict[3]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    else:
                        hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                        
                else:
                    print('Opção inválida')
                        
            elif usuario == 2: 
                usuario_digita = input("\nDigite a especialidade desejada: \n\n1 - Obstetra \n2 - Clínico Geral \n3 - Dentista \n\nDigite aqui: ")
                
                while not usuario_digita.isdigit():
                    usuario_digita = input('\nDigite a especialidade desejada: \n\n1 - Obstetra \n2 - Clínico Geral \n3 - Dentista \n\nDigite aqui: ') 
            
                usuario_digita = int(usuario_digita)
                
                usuario_dict = {1:'Obstetra', 2:'Clínico Geral', 3:'Dentista'}

                if usuario_digita == 1:
                    
                    print(f"\nAbaixo, escolha o dia para reagendamento \n\n {calendar.month(aa,mm)}")
                    escolha_usuario = input('Digite um dia em formato dd: ')
                    
                    while not escolha_usuario.isdigit():
                        escolha_usuario = input('\nEntrada inválida. Digite um dia em formato dd: ') 
            
                    escolha_usuario = int(escolha_usuario)

                    hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr4} \n2 - {hr5} \n\nDigite aqui: ')
                    
                    while not hora.isdigit():
                        hora = input('\nEntrada inválida. Escolha uma opção de horário: \n\n1 - 07:00 h \n2 - 09:45 h \n\nDigite aqui: ') 
            
                    hora = int(hora)
                    
                    hora_dict = {1:'07:00 h', 2:'09:45 h'}
                    
                    if hora == 1:
                        print (f"\n{nome}, sua consulta com {espec_1} foi agendada para {escolha_usuario}/07 às {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    elif hora == 2:
                        print (f"\n{nome}, sua consulta com {espec_1} foi agendada para {escolha_usuario}/07 às {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    else:
                        hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr4} \n2 - {hr5} \n\nDigite aqui: ')
                    
                elif usuario_digita == 2:
                    
                    print(f"\nAbaixo, escolha o dia para reagendamento \n\n {calendar.month(aa,mm)}")
                    escolha_usuario = input('Digite um dia em formato dd: ')
                    
                    while not escolha_usuario.isdigit():
                        escolha_usuario = input('\nEntrada inválida. Digite um dia em formato dd: ') 
            
                    escolha_usuario = int(escolha_usuario)

                    hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr4} \n2 - {hr5} \n\nDigite aqui: ')
                    
                    while not hora.isdigit():
                        hora = input('\nEntrada inválida. Escolha uma opção de horário: \n\n1 - 07:00 h \n2 - 09:45 h \n\nDigite aqui: ') 
            
                    hora = int(hora)
                    
                    hora_dict = {1:'07:00 h', 2:'09:45 h'}
                    
                    if hora == 1:
                        print (f"\n{nome}, sua consulta com {espec_2} foi agendada para {escolha_usuario}/07 às {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    elif hora == 2:
                        print (f"\n{nome}, sua consulta com {espec_2} foi agendada para {escolha_usuario}/07 às {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    else:
                        hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr4} \n2 - {hr5} \n\nDigite aqui: ')
                    
                elif usuario_digita == 3:
                    
                    print(f"\nAbaixo, escolha o dia para reagendamento \n\n {calendar.month(aa,mm)}")
                    escolha_usuario = input('Digite um dia em formato dd: ')
                    
                    while not escolha_usuario.isdigit():
                        escolha_usuario = input('\nEntrada inválida. Digite um dia em formato dd: ') 
            
                    escolha_usuario = int(escolha_usuario)

                    hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr4} \n2 - {hr5} \n\nDigite aqui: ')
                    
                    while not hora.isdigit():
                        hora = input('\nEntrada inválida. Escolha uma opção de horário: \n\n1 - 07:00 h \n2 - 09:45 h \n\nDigite aqui: ') 
            
                    hora = int(hora)
                    
                    hora_dict = {1:'07:00 h', 2:'09:45 h'}
                    
                    if hora == 1:
                        print (f"\n{nome}, sua consulta com {espec_3} foi agendada para {escolha_usuario}/07 às {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    elif hora == 2:
                        print (f"\n{nome}, sua consulta com {espec_3} foi agendada para {escolha_usuario}/07 às {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                        f.fim_programa()
                    else:
                        hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr4} \n2 - {hr5} \n\nDigite aqui: ')
                        
                else:
                    print('Opção inválida')
            
            elif usuario == 3:
                check = 0       
    
        consulta()
    
    ## Resultado - Érick
    elif start == 2:

        def resultado():
            result = random.randrange(1, 3)
            escolha = int(input("\nDeseja ver o resultado do exame ou do agendamento?\n\n1 - Exame \n2 - Agendamento \n3 - Voltar ao menu principal \n\nDigite aqui: "))
            
            if (escolha == 1):  
                
                resultado_exame = int(input(f'\n\nDeseja ver o resultado para qual exame? \n\n1 - Hemograma \n2 - Parasitológico \n3 - Teste Glicêmico \n\nDigite aqui: '))
                result_hemo = ['está saudável.', 'tem um excesso de gordura no sangue.', 'está com uma falta de ferro no sangue.']
                result_para = ['está saudável.', 'está com vermes no intestino.', 'está com vermes na garganta.']
                result_glic = ['tem uma quantidade de açucar baixa/média no sangue.', 'tem uma quantidade de açucar média/alta no sangue.', 'tem uma quantidade de açucar alta/alarmável no sangue.']
                
                if (resultado_exame == 1):
                    print(f'\n{nome}, o resultado do seu Hemograma é: {random.choice(result_hemo)}')
                    
                        
                elif (resultado_exame == 2): 
                    print(f'\n{nome}, o resultado do seu Exame Parasitológico é: {random.choice(result_para)}')
                        
                elif (resultado_exame == 3): 
                    print(f'\n{nome}, o resultado do seu Teste Gligêmico é: {random.choice(result_glic)}')
                else:
                    print("Nenhum exame encontrado.")
                    
                    
            elif (escolha == 2): 
                verifica = int(input("\nDeseja verificar o agendamento da Consulta ou do Exame? \n\n1 - Consulta \n2 - Exame \n3 - Voltar ao menu principal \n\nDigite aqui: "))
                    
                if (verifica == 1):     
                    escolha_usuario = random.randrange(1, 31)
                    print(f"\nSua consulta está marcada para o dia {escolha_usuario} de Julho, {random.randrange(8, 18)}:{random.randrange(00, 59)} h.")
                        
                elif (verifica == 2):     
                    escolha_usuario = random.randrange(1, 31)
                    print(f"\nSeu exame está marcada para o dia {escolha_usuario} de Julho, {random.randrange(8, 18)}:{random.randrange(00, 59)} h.")
                    
                elif(verifica == 3):
                    check = 0
                 
            elif (escolha == 3):
                check = 0    
    
        resultado()               

    ## Exames - Day  
    elif start == 3:
                
        aa = 2022
        mm = 7
        ex1 = 'Hemograma'
        ex2 = 'Parasitológico'
        ex3 = 'Glicemico'
        hr1 = '10:30h'
        hr2 = '12:45h'
        hr3 = '14:10h' 
                
        def exames():
            
            exames = int(input(f'\nOlá {nome}! Selecione o exame desejado: \n\n1 - {ex1} \n2 - {ex2} \n3 - {ex3} \n\nDigite aqui: '))
        
            while (exames != 1) and (exames != 2) and (exames != 3):
                exames = int(input(f'\nOpção inválida, {nome}. Digite o exame desejado: \n\n1 - {ex1} \n2 - {ex2} \n3 - {ex3} \n\nDigite aqui: '))
            
            if exames == 1:
                print (f'\nVocê selecionou exame de {ex1}. Selecione entre as datas disponíveis: \n\n {calendar.month(aa,mm)}')
                data = int(input('Digite um dia em formato dd: '))

                hora = int(input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: '))
                hora_dict = {1:'10:30h', 2:'12:45h', 3:'14:10h'}
                
                if hora == 1:
                    print (f"\nExame {ex1} agendado em {data}/07 no horário {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                elif hora == 2:
                    print (f"\nExame {ex1} agendado em {data}/07 no horário {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                elif hora == 3:
                    print (f"\nExame {ex1} agendado em {data}/07 no horário {hora_dict[3]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                else:
                    None
                      
            elif exames == 2:
                print (f'\nVocê selecionou exame de {ex2}. Selecione entre as datas disponíveis: \n\n {calendar.month(aa,mm)}')
                data = int(input('Digite um dia em formato dd: '))
                while (data < 1) or (data > 30):
                    data = int(input('Dia inválido. Digite um dia em formato dd: '))

                hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                hora_dict = {1:'10:30h', 2:'12:45h', 3:'14:10h'}

                if hora == 1:
                    print (f"\nExame {ex2} agendado em {data}/07 no horário {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                elif hora == 2:
                    print (f"\nExame {ex2} agendado em {data}/07 no horário {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                elif hora == 3:
                    print (f"\nExame {ex2} agendado em {data}/07 no horário {hora_dict[3]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                else:
                    hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')        
            
            elif exames == 3:
                print (f'\nVocê selecionou exame de {ex3}. Selecione entre as datas disponíveis: \n\n {calendar.month(aa,mm)}')
                data = int(input('Digite um dia em formato dd: '))
                while (data < 1) or (data > 30):
                    data = int(input('Dia inválido. Digite um dia em formato dd: '))

                hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                hora_dict = {1:'10:30h', 2:'12:45h', 3:'14:10h'}

                if hora == 1:
                    print (f"\nExame {ex3} agendado em {data}/07 no horário {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                elif hora == 2:
                    print (f"\nExame {ex3} agendado em {data}/07 no horário {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                elif hora == 3:
                    print (f"\nExame {ex3} agendado em {data}/07 no horário {hora_dict[3]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
                else:
                    hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
                
            else:
                ('Opção inválida. Encerrando atendimento.')
        
        exames ()
        
    ## Informações - Bárbara
    elif start == 4:

        def informacoes ():
            
            print('\nINFORMAÇÕES\n')

            dados = input('Bem-vindo(a) ao setor de informações. Digite sua opção de escolha: \n\n1 - Informações sobre a UBS \n2 - Retirada de Medicamentos \n3 - Retirada de Exames \n4 - Voltar ao menu anterior \n\nDigite aqui: ')

            while not dados.isdigit():
                dados = input('\nEntrada inválida. Digite sua opção de escolha: \n\n1 - Informações sobre a UBS \n2 - Retirada de Medicamentos \n3 - Retirada de Exames \n4 - Voltar ao menu anterior \n\nDigite aqui: ')  
                
            dados = int(dados)
                
            if dados == 1:
                infos_ubs = input('\nEscolha a UBS que deseja informações: \n1 - UBS 1 \n2 - UBS 2 \n3 - UBS 3 \n\nDigite aqui: ')
                while not infos_ubs.isdigit():
                    infos_ubs = input('\nEntrada inválida. Escolha a UBS que deseja informações: \n1 - UBS 1 \n2 - UBS 2 \n3 - UBS 3 \n\nDigite aqui: ') 
                    
                infos_ubs = int(infos_ubs)
                
                if infos_ubs == 1:
                    print('\nINFORMAÇÕES SOBRE A UBS 1\n\nEndereço: Rua dos Bobos, nº 0 \nTelefone: (00) 0000-0000 \nHorário de atendimento: 24 horas \n')
                elif infos_ubs == 2:
                    print('\nINFORMAÇÕES SOBRE A UBS 2\n\nEndereço: Rua dos Bobos, nº 100 \nTelefone: (00) 0000-0000 \nHorário de atendimento: 24 horas \n')  
                elif infos_ubs == 3:
                    print('\nINFORMAÇÕES SOBRE A UBS 2\n\nEndereço: Rua dos Bobos, nº 200 \nTelefone: (00) 0000-0000 \nHorário de atendimento: 24 horas \n')                    
                else:
                    infos_ubs = input('\nEntrada inválida. Escolha a UBS que deseja informações: \n1 - UBS 1 \n2 - UBS 2 \n3 - UBS 3 \n\nDigite aqui: ')

            elif dados == 2:
                print('\nRETIRADA DE MEDICAMENTOS\n')
                
                medicamento = input('Qual o medicamento que deseja retirar? \n1 - Paracetamol \n2 - Ibuprofeno \n3 - Cetirizina \n\nDigite aqui: ')
                while not medicamento.isdigit():
                    medicamento = input('\nEntrada inválida. Qual o medicamento que deseja retirar? \n1 - Paracetamol \n2 - Ibuprofeno \n3 - Cetirizina \n\nDigite aqui: ') 
                
                medicamento = int(medicamento)
                result_medi = ['a retirada do medicamento foi realizada com sucesso.', 'medicamento não disponível no momento.', 'a retirada do medicamento foi agendada com sucesso.']
                if medicamento == 1:
                    print(f'\n{nome}, {random.choice(result_medi)} Você receberá um SMS com mais informações.')
                elif medicamento == 2:
                    print(f'\n{nome}, {random.choice(result_medi)} Você receberá um SMS com mais informações')
                elif medicamento == 3:
                    print(f'\n{nome}, {random.choice(result_medi)} Você receberá um SMS com mais informações')
                else:
                    print('\nEntrada inválida. Encerrando o programa.\n')
                
            elif dados == 3:
                print('\nRETIRADA DE EXAMES\n')
                
                exames = input('Qual exame deseja retirar? \n1 - Exame de sangue \n2 - Exame de urina \n3 - Exame de óculos \n\nDigite aqui: ')
                while not exames.isdigit():
                    exames = input('\nEntrada inválida. Qual exame deseja retirar? \n1 - Exame de sangue \n2 - Exame de urina \n3 - Exame de óculos \n\nDigite aqui: ') 
                
                exames = int(exames)
                result_exames = ['retirada do exame foi realizada com sucesso.', 'resultado do exame não disponível no momento.', 'retirada do exame foi agendada com sucesso.']
                
                if exames == 1:
                    print(f'\n{nome}, {random.choice(result_exames)} Você receberá um SMS com mais informações')
                elif exames == 2:
                    print(f'\n{nome}, {random.choice(result_exames)} Você receberá um SMS com mais informações')
                elif exames == 3:
                    print(f'\n{nome}, {random.choice(result_exames)} Você receberá um SMS com mais informações')
                else:
                    print('\nEntrada inválida. Encerrando o programa.\n')
                    
            elif dados == 4:
                check = 0
                
            else:
                dados = input('\nEntrada inválida. Digite sua opção de escolha: \n\n1 - Informações sobre a UBS \n2 - Retirada de Medicamentos \n3 - Retirada de Exames \n\nDigite aqui: ')  
        
        informacoes()
        
    elif start == 5:
        print(f'\nAgradecemos seu contato {nome}. O Atende + te deseja um bom dia.\n')
        break
        
    else:
        start = input('\nEntrada inválida. O que deseja fazer?\n\n1 - Consultas \n2 - Resultados \n3 - Exames \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')