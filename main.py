import random
import calendar

nome = input(f'\nBem-vindo(a). Para iniciar o atendimento, insira seu nome: ')

start = input(f'\nBem-vindo (a) {nome} ao chatbot do Atende+. O que deseja fazer?\n\n1 - Consultas \n2 - Exames \n3 - Resultados \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')

while not start.isdigit():
        start = input('\nEntrada inválida. O que deseja fazer?\n\n1 - Consultas \n2 - Exames \n3 - Resultados \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')  
start = int(start)

## Consultas - Diego
if start == 1:

    print(" "*100)
    print("""Bem-Vindo ao aplicativo móvel Atende + """.upper())
    print(" "*100)

    ano_2022 = 2022
    mes_7 = 7

    def tracinho():
        print("-"*100)

    def consulta(nome, nome_UBS):
        print(f"\nOlá {nome}, bem vindo ao Atende +, nosso portal de comunicação com o usuário. Por favor, digite sua escolha abaixo")
        print("_"*100)
        menu = True
        while(menu):
            usuario = int(input(
                f"Deseja marcar consulta? \n1 - Marcar consulta \n2 - Reagendar Consulta \n3 - Menu de Opções \nDigite:  "))
            if(usuario != 1 and usuario != 2 and usuario != 3):
                print("Opção inválida.")
                continue
            else:
                break
        if usuario == 1:
            usuario_digita = int(input(
                "Digite a área de atendimento da consulta: \n1 - Obstetra \n2 - Clínico Geral \n3 - Dentista \nDigite:  "))

        if usuario == 1:  # Abaixo o usuário deve escolher o dia da consulta
            if usuario_digita == 1:
                print(
                    f"Abaixo, escolha o dia da consulta {calendar.month(ano_2022,mes_7)}")
                escolha_usuario = int(input(f"""Escolha o dia de agendamento da consulta: 
                    1 - Dia 23 de  Julho
                    2 - Dia 25 de  Julho
                    3 - Dia 30 de  Julho
                    Digite: """))

                if escolha_usuario == 1:
                    dia = 23
                    n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                        1 - 12:00 hs
                        2 - 13:30 hs
                        3 - 08:00 hs
                        Digite: """))
                    if (n == 1):

                        print(
                            f"O agendamento da consulta está marcado para o dia {dia} de {mes_7} às 12:00hs.")
                        return 1, dia, horario, None
                    elif(n == 2):
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia} de {mes_7} às 13:30hs.")
                        return 1, dia, n, None
                elif escolha_usuario == 2:
                    dia = 25
                    n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                        1 - 12:00 hs
                        2 - 13:30 hs
                        3 - 08:00 hs
                        Digite: """))
                    if (n == 1):
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia} de {mes_7} às 12:00hs.")
                        return 1, dia, n, None
                    elif(n == 2):
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia} de {mes_7} às 13:30hs.")
                        return 1, dia, n, None
                    elif(n == 3):
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia} de {mes_7} às 13:30hs.")
                        return 1, dia, n, None
            elif usuario_digita == 2:

                print(
                    f"Abaixo, escolha o dia da consulta {calendar.month(ano_2022,mes_7)}")
                escolha_usuario = int(input(f"""Escolha o dia de agendamento da consulta:
                    1 - Dia 25 de  Julho
                    2 - Dia 29 de  Julho
                    Digite: """))
                    
                if escolha_usuario == 1:
                    dia_1 = 25
                    n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                        1 - 11:00 hs
                        2 - 13:45 hs
                        Digite: """))

                    if n == 1:
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_1} de {mes_7} às 12:00hs.")
                        return 1, dia_1, n, None

                    elif(n == 2):
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_1} de {mes_7} às 13:30hs.")
                        return 1, dia_1, n, None
                
                elif escolha_usuario == 2:
                    dia_2 = 29
                    n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                        1 - 11:00 hs
                        2 - 13:45 hs
                        Digite: """))
                    
                    if n == 1:
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_2} de {mes_7} às 11:hs."
                        )

                    if n == 2:
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_2} de {mes_7} às 13:45 hs.")
                        return 1, dia_2, n, None
            
            elif usuario_digita == 3:

                print(
                    f"Abaixo, escolha o dia da consulta {calendar.month(ano_2022,mes_7)}")
                escolha_usuario = int(input(f"""Escolha o dia de agendamento da consulta:
                    1 - Dia 15 de  Julho
                    2 - Dia 18 de  Julho
                    Digite: """))
                    
                if escolha_usuario == 1:
                    dia_1 = 15
                    n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                        1 - 07:00 hs
                        2 - 09:45 hs
                        Digite: """))

                    if n == 1:
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_1} de {mes_7} às 07:00 hs.")
                        return 1, dia_1, n, None

                    elif(n == 2):
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_1} de {mes_7} às 09:45 hs.")
                        return 1, dia_1, n, None
                
                elif escolha_usuario == 2:
                    dia_2 = 29
                    n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                        1 - 07:00 hs
                        2 - 09:45 hs
                        Digite: """))
                    
                    if n == 1:
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_2} de {mes_7} às 07:00 hs.")

                    if n == 2:
                        print(
                            f"O agendamento da consulta está marcado para o dia {dia_2} de {mes_7} às 09:45 hs.")
                        return 1, dia_2, n, None

            else:
                while usuario_digita == True:
                    print("Entrada inválida. Digite novamente!")
                    usuario_digita = int(input("""Digite a área de atendimento da consulta:
                        1 - Obstetra
                        2 - Clínico Geral
                        3 - Dentista
                        Digite:  """))

        # if (reagendar_consulta) == 1 or (reagendar_consulta) == 2 or (reagendar_consulta) or 3:
        #     horario = int(input(f"Marque o turno de reagendamento da consulta:\n [1] Manhã \n [2] Tarde \n [3] Noite \n Digite:  "))

        if usuario == 2:
            reagendar_consulta = int(input("""Marque o dia de reagendamento da consulta:  
                1 -  Dia 7 de Agosto
                2 - Dia 13 de Agosto
                3 -  Dia 20 de Agosto
                Digite:  """))
            horario = int(input(
                f"Marque o turno de reagendamento da consulta:\n [1] Manhã \n [2] Tarde \n Digite:  "))
            if horario == 1:
                reagenda = int(input(f"""Os horários disponíveis para reagendamento na {nome_UBS} para essa data são:
                    1 - 07:00 hs
                    2 - 09:30 hs
                    Digite:    """))
                if reagenda == 1:
                    print("Seu reagendamento está marcado para a parte da manhã às 07:00 hs. Por favor, compareça!")
                    return 1
                elif reagenda == 2:
                    print("Seu reagendamento está marcado para a parte da manhã às 09:00 hs. Por favor, compareça!")

            elif horario == 2:
                reagenda_2 = int(input(f"""Os horários disponíveis para reagendamento na {nome_UBS} para essa data são:
                    1 - 14:00 hs hs
                    2 - 16:15 hs
                    Digite:    """))
                if reagenda_2 == 1:
                    print(f"Seu reagendamento está marcado para às 14:00 hs. Por favor, compareça!")
                elif reagenda_2 == 2:
                    print(f"Seu reagendamento está marcado para às 16:15 hs. Por favor, compareça!")

        if usuario == 3:
            menu_opcoes = int(
                input(f"Deseja voltar ao menu de opções?\n [1] Sim \n [2] Não \n Digite:  "))
            if menu_opcoes == 1:
                usuario_digita = int(input(
                    "Digite a área de atendimento da consulta: \n[1] Obstetra \n[2] Clínico Geral \n[3] Dentista \nDigite:  "))
            elif menu_opcoes == 2:
                continuar = True
                while continuar:
                    print("Entrada inválida. Digite novamente!")
                    usuario_digita = int(input("""Digite a área de atendimento da consulta:
                        1 - Obstetra
                        2 - Clínico Geral
                        3 - Dentista
                        Digite:  """))
                    print(f"Obrigado, a {nome_UBS} agredece pela preferência")
            return usuario

    resultado = consulta({nome}, "UBS Brasil")
    print(resultado)

## Resultado - Érick
elif start == 2:

    def resultado():
        continuar = True
        while(continuar):
            result = random.randrange(1, 3)
            escolha = int(input(
                "\nDeseja ver o resultado do exame ou do agendamento?\n\n1 - Exame \n2 - Agendamento \n3 - Retornar ao Menu Principal \n\nDigite aqui: "))
            if (escolha == 1):  # Vai verificar o resultado do Exame
                # Exame de hemograma,coloquei 3 opções aleatórias para serem escolhidas de maneira aleatória com o "random"
                if (diaEhoraE[3] == 1):
                    if (result == 1):
                        print(f"{usuario} indivíduo está saudável.")
                    elif (result == 2):
                        print(f"{usuario} tem um excesso de gordura no sangue.")
                    elif (result == 3):
                        print(f"{usuario} está com uma falta de ferro no sangue.")
                elif (diaEhoraE[3] == 2):  # Exame Parasitológico
                    if (result == 1):
                        print(f"{usuario} está saudável.")
                    elif (result == 2):
                        print(f"{usuario} está com vermes no intestino.")
                    elif (result == 3):
                        print(f"{usuario} está com vermes na garganta.")
                elif (diaEhoraE[3] == 3):  # Exame Glicêmico
                    if (result == 1):
                        print(
                            f"{usuario} tem uma quantidade de açucar baixa/média no sangue.")
                    elif (result == 2):
                        print(
                            f"{usuario} tem uma quantidade de açucar média/alta no sangue.")
                    elif(result == 3):
                        print(
                            f"{usuario} tem uma quantidade de açucar alta/alarmável no sangue.")
                else:
                    print("Nenhum exame ou consulta encontrada.")
                    
            elif(escolha == 2):  # Vai verificar or resultado do Agendamento
                while(True):
                    verifica = int(input(
                        "Deseja verificar o agendamento da Consulta ou do Exame?\n[1]Consulta\n[2]Exame\n"))
                    if (verifica == 1):
                        if (diaEhoraC != None):
                            if(diaEhoraC[2] == 1):
                                print(
                                    f"Sua consulta está marcada para o dia {diaEhoraC[1]} de Julho, 12:00h.")
                                break
                            elif(diaEhoraC[2] == 2):
                                print(
                                    f"Sua consulta está marcada para o dia {diaEhoraC[1]} de Julho, 13:30h.")
                                break
                            elif(diaEhoraC[2] == 3):
                                print(
                                    f"Sua consulta está marcada para o dia {diaEhoraC[1]} de Julho, 16:15h.")
                                break
                        else:
                            print("Sem consulta marcada.")
                    elif(verifica == 2):
                        if(diaEhoraE != None):
                            if(diaEhoraE[2] == 1):
                                print(
                                    f"Seu exame está marcado para o dia {diaEhoraE[1]} de Julho, 10:30h.")
                                break
                            elif(diaEhoraE[2] == 2):
                                print(
                                    f"Seu exame está marcado para o dia {diaEhoraE[1]} de Julho, 12:45h.")
                                break
                            elif(diaEhoraE[2] == 3):
                                print(
                                    f"Seu exame está marcado para o dia {diaEhoraE[1]} de Julho, 14:10h.")
                                break
                        else:
                            print("Sem exame marcado.")
                    else:
                        print("Escolha inválida!\nTente novamente...")
            elif(escolha == 3):
                print("Voltando para o Menu Principal.")
                break
            else:
                print("Opção inválida,tente novamente...")
                continue
            # Abaixo,caso o usuário ja tenha visto o resultado do agendamento ou do exame,será perguntado se deseja continuar
            opcao = int(input("Deseja continuar?\n[1]Sim\n[2]Não\n"))
            while(True):
                if (opcao == 1):
                    break
                elif(opcao == 2):
                    print("Voltando para o Menu Principal...")
                    continuar = False
                    break
                else:
                    while (opcao != 1 and opcao != 2):
                        opcao = int(
                            input("Opção inválida,escolha [1] para Sim ou [2] para Não:\n"))
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

    exames = input(f'\nOlá {nome}! Selecione o exame desejado: \n1 - {ex1} \n2 - {ex2} \n3 - {ex3} \n\nDigite aqui: ')
    
    while (exames != '1') and (exames != '2') and (exames != '3'):
        exames = input(f'Opção inválida, {nome}. Digite o exame desejado: \n1 - {ex1} \n2 - {ex2} \n3 - {ex3} \n\nDigite aqui: ')
            
    def ex(exames):
        if exames == '1':
            print (f'\nVocê selecionou exame de {ex1}. Selecione entre as datas disponíveis: \n\n {calendar.month(aa,mm)}')
            data = int(input('Digite um dia em formato dd: '))
            while (data < 1) or (data > 30):
                data = int(input('Dia inválido. Digite um dia em formato dd: '))

            hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
            hora_dict = {1:'10:30h', 2:'12:45h', 3:'14:10h'}

            while (hora <'1') or (hora >'3'):
                hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
            print (f"\nExame {ex1} agendado em {data}/07 no horário {hora_dict[1]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")

        
        elif exames == '2':
            print (f'\nVocê selecionou exame de {ex2}. Selecione entre as datas disponíveis: \n\n {calendar.month(aa,mm)}')
            data = int(input('Digite um dia em formato dd: '))
            while (data < 1) or (data > 30):
                data = int(input('Dia inválido. Digite um dia em formato dd: '))

            hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
            hora_dict = {1:'10:30h', 2:'12:45h', 3:'14:10h'}

            while (hora <'1') or (hora >'3'):
                hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
            print (f"\nExame {ex2} agendado em {data}/07 no horário {hora_dict[2]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")         
        
        elif exames == '3':
            data = int(input('Digite um dia em formato dd: '))
            while (data < 1) or (data > 30):
                data = int(input('Dia inválido. Digite um dia em formato dd: '))

            hora = input(f'\nEscolha uma opção de horário: \n\n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
            hora_dict = {1:'10:30h', 2:'12:45h', 3:'14:10h'}

            while (hora <'1') or (hora >'3'):
                hora = input(f'\nHorário não disponível. Escolha uma opção de horário: \n1 - {hr1} \n2 - {hr2} \n3 - {hr3} \n\nDigite aqui: ')
            print (f"\nExame {ex3} agendado em {data}/07 no horário {hora_dict[3]} com sucesso! Você receberá um SMS para a confirmação do seu agendamento.\n")
            
        else:
            ('Opção inválida. Encerrando atendimento.')

    ex(exames)

## Informações - Bárbara
elif start == 4:

    def informacoes ():
        
        print('\nINFORMAÇÕES\n')

        dados = input('Bem-vindo(a) ao setor de informações. Digite sua opção de escolha: \n\n1 - Informações sobre a UBS \n2 - Retirada de Medicamentos \n3 - Retirada de Exames \n4 - Voltar ao menu anterior \n5 - Sair \n\nDigite aqui: ')

        while not dados.isdigit():
            dados = input('\nEntrada inválida. Digite sua opção de escolha: \n\n1 - Informações sobre a UBS \n2 - Retirada de Medicamentos \n3 - Retirada de Exames \n4 - Voltar ao menu anterior \n5 - Sair \n\nDigite aqui: ')  
            
        dados = int(dados)
            
        if dados == 1:
            infos_ubs = input('\nEscolha a UBS que deseja informações: \n1 - UBS 1 \n2 - UBS 2 \n3 - UBS 3 \n4 - Voltar ao menu anterior \n5 - Sair \nDigite aqui: ')
            while not infos_ubs.isdigit():
                infos_ubs = input('\nEntrada inválida. Escolha a UBS que deseja informações: \n1 - UBS 1 \n2 - UBS 2 \n3 - UBS 3 \n4 - Voltar ao menu anterior \n5 - Sair \nDigite aqui: ') 
                
            infos_ubs = int(infos_ubs)
            
            if infos_ubs == 1:
                print('\nINFORMAÇÕES SOBRE A UBS 1\n\nEndereço: Rua dos Bobos, nº 0 \nTelefone: (00) 0000-0000 \nHorário de atendimento: 24 horas \n')
                ubs_1 = input(' 1 - Consultar informações sobre outra UBS \n2 - Sair \n\nDigite aqui: ')
                while not ubs_1.isdigit():
                    ubs_1 = input('\nEntrada inválida. Escolha uma opção: \n1 - Consultar informações sobre outra UBS \n2 - Sair \n\nDigite aqui: ')
                    
                ubs_1 = int(ubs_1)
                # if ubs_1 == 1:
                
                # elif ubs_1 == 2:
                #     print('\nEncerrando o programa.')
            elif infos_ubs == 2:
                print('\nINFORMAÇÕES SOBRE A UBS 2\n\nEndereço: Rua dos Bobos, nº 100 \nTelefone: (00) 0000-0000 \nHorário de atendimento: 24 horas \n')
                ubs_2 = input(' 1 - Consultar informações sobre outra UBS \n2 - Sair \n\nDigite aqui: ')
                while not ubs_2.isdigit():
                    ubs_2 = input('\nEntrada inválida. Escolha uma opção: \n1 - Consultar informações sobre outra UBS \n2 - Sair \n\nDigite aqui: ')
                    
                ubs_2 = int(ubs_2)
                # if ubs_2 == 1:
                
                # elif ubs_2 == 2:
                #     print('\nEncerrando o programa.')    
            elif infos_ubs == 3:
                print('\nINFORMAÇÕES SOBRE A UBS 2\n\nEndereço: Rua dos Bobos, nº 200 \nTelefone: (00) 0000-0000 \nHorário de atendimento: 24 horas \n')
                ubs_3 = input(' 1 - Consultar informações sobre outra UBS \n2 - Sair \n\nDigite aqui: ')
                while not ubs_3.isdigit():
                    ubs_3 = input('\nEntrada inválida. Escolha uma opção: \n1 - Consultar informações sobre outra UBS \n2 - Sair \n\nDigite aqui: ')
                    
                ubs_3 = int(ubs_3)
                # if ubs_3 == 1:
                
                # elif ubs_3 == 2:
                #     print('\nEncerrando o programa.')
                
            else:
                infos_ubs = input('\nEntrada inválida. Escolha a UBS que deseja informações: \n1 - UBS 1 \n2 - UBS 2 \n3 - UBS 3 \n4 - Voltar ao menu anterior \n5 - Sair \nDigite aqui: ')

        elif dados == 2:
            print('\nRETIRADA DE MEDICAMENTOS\n')
            
            medicamento = input('Qual o medicamento que deseja retirar? \n1 - Paracetamol \n2 - Ibuprofeno \n3 - Cetirizina \n4 - Voltar ao menu anterior \n5 - Sair \nDigite aqui: ')
            while not medicamento.isdigit():
                medicamento = input('\nEntrada inválida. Qual o medicamento que deseja retirar? \n1 - Paracetamol \n2 - Ibuprofeno \n3 - Cetirizina \n4 - Voltar ao menu anterior \n5 - Sair \nDigite aqui: ') 
            
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
            
            exames = input('Qual exame deseja retirar? \n1 - Exame de sangue \n2 - Exame de urina \n3 - Exame de óculos \n4 - Voltar ao menu anterior \n5 - Sair \nDigite aqui: ')
            while not exames.isdigit():
                exames = input('\nEntrada inválida. Qual exame deseja retirar? \n1 - Exame de sangue \n2 - Exame de urina \n3 - Exame de óculos \n4 - Voltar ao menu anterior \n5 - Sair \nDigite aqui: ') 
            
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
            dados = input('\nEntrada inválida. Digite sua opção de escolha: \n\n1 - Informações sobre a UBS \n2 - Retirada de Medicamentos \n3 - Retirada de Exames \n4 - Voltar ao menu anterior \n5 - Sair \n\nDigite aqui: ')  
            
    informacoes()
    
elif start == 5:
    print(f'\nAgradecemos seu contato {nome}. O Atende + te deseja um bom dia.\n')
    
else:
    start = input('\nEntrada inválida. O que deseja fazer?\n\n1 - Consultas \n2 - Exames \n3 - Resultados \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')