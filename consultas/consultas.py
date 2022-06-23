import calendar
print(" "*100)
print("""Bem-Vindo ao aplicativo móvel Atende + """.upper())
print("-"*100)
print(" "*100)

ano_2022 = 2022
mes_7 = 7

def tracinho():
    print("-"*100)

def consulta(nome, nome_UBS):
    print(f"Olá {nome}, bem vindo ao Atende +, nosso portal de comunicação com o usuário. Por favor, digite sua escolha abaixo")
    print("_"*100)
    menu = True
    while(menu):
        usuario = int(input(
            f"Deseja marcar consulta? \n[1] Marcar consulta \n[2] Reagendar Consulta\n [3] Menu de Opções\n Digite:  "))
        if(usuario != 1 and usuario != 2 and usuario != 3):
            print("Opção inválida.")
            continue
        else:
            break
    if usuario == 1:
        usuario_digita = int(input(
            "Digite a área de atendimento da consulta: \n[1] Obstetra \n[2] Clínico Geral \n[3] Dentista \nDigite:  "))

    if usuario == 1:  # Abaixo o usuário deve escolher o dia da consulta
        if usuario_digita == 1:
            print(
                f"Abaixo, escolha o dia da consulta {calendar.month(ano_2022,mes_7)}")
            escolha_usuario = int(input(f"""Escolha o dia de agendamento da consulta: 
                [1] Dia 23 de  Julho
                [2] Dia 25 de  Julho
                [3] Dia 30 de  Julho
                Digite: """))

            if escolha_usuario == 1:
                dia = 23
                n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                    [1] 12:00 hs
                    [2] 13:30 hs
                    [3] 08:00 hs
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
                    [1] 12:00 hs
                    [2] 13:30 hs
                    [3] 08:00 hs
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
                [1] Dia 25 de  Julho
                [2] Dia 29 de  Julho
                Digite: """))
                
            if escolha_usuario == 1:
                dia_1 = 25
                n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                    [1] 11:00 hs
                    [2] 13:45 hs
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
                    [1] 11:00 hs
                    [2] 13:45 hs
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
                [1] Dia 15 de  Julho
                [2] Dia 18 de  Julho
                Digite: """))
                
            if escolha_usuario == 1:
                dia_1 = 15
                n = int(input(f"""Os horários disponíveis na unidade {nome_UBS} para essa data são:
                    [1] 07:00 hs
                    [2] 09:45 hs
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
                    [1] 07:00 hs
                    [2] 09:45 hs
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
                    [1] Obstetra
                    [2] Clínico Geral
                    [3] Dentista
                    Digite:  """))

    # if (reagendar_consulta) == 1 or (reagendar_consulta) == 2 or (reagendar_consulta) or 3:
    #     horario = int(input(f"Marque o turno de reagendamento da consulta:\n [1] Manhã \n [2] Tarde \n [3] Noite \n Digite:  "))

    if usuario == 2:
        reagendar_consulta = int(input("""Marque o dia de reagendamento da consulta:  
            [1] Dia 7 de Agosto
            [2] Dia 13 de Agosto
            [3] Dia 20 de Agosto
            Digite:  """))
        horario = int(input(
            f"Marque o turno de reagendamento da consulta:\n [1] Manhã \n [2] Tarde \n Digite:  "))
        if horario == 1:
            reagenda = int(input(f"""Os horários disponíveis para reagendamento na {nome_UBS} para essa data são:
                [1] 07:00 hs
                [2] 09:30 hs
                Digite:    """))
            if reagenda == 1:
                print("Seu reagendamento está marcado para a parte da manhã às 07:00 hs. Por favor, compareça!")
                return 1
            elif reagenda == 2:
                print("Seu reagendamento está marcado para a parte da manhã às 09:00 hs. Por favor, compareça!")

        elif horario == 2:
            reagenda_2 = int(input(f"""Os horários disponíveis para reagendamento na {nome_UBS} para essa data são:
                [1] 14:00 hs hs
                [2] 16:15 hs
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
                    [1] Obstetra
                    [2] Clínico Geral
                    [3] Dentista
                    Digite:  """))
                print(f"Obrigado, a {nome_UBS} agredece pela preferência")
        return usuario


resultado = consulta("Diego", "UBS Brasil")
print(resultado)
