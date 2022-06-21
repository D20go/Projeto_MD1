import random
#  1.Hemograma
#  2.Fezes e urina
#  3.Glicemia
# hr1 = '10:30h'
# hr2 = '12:45h'
# hr3 = '14:10h'


def resultado(usuario, exame=None, diaEhora=None, agend=None):
    continuar = True
    while(continuar):
        result = random.randrange(1, 3)
        escolha = int(input(
            "Deseja ver o resultado do exame ou do agendamento?\nEscolha [1] para Exame ou [2] para Agendamento: "))
        if (escolha == 1):  # Vai verificar o resultado do Exame
            if (exame == 1):  # Exame de hemograma,coloquei 3 opções aleatórias
                if (result == 1):
                    print(f"{usuario} indivíduo está saudável.")
                elif (result == 2):
                    print(f"{usuario} tem um excesso de gordura no sangue.")
                elif (result == 3):
                    print(f"{usuario} está com uma falta de ferro no sangue.")
            elif (exame == 2):  # Exame Parasitológico
                if (result == 1):
                    print(f"{usuario} está saudável.")
                elif (result == 2):
                    print(f"{usuario} está com vermes no intestino.")
                elif (result == 3):
                    print(f"{usuario} está com vermes na garganta.")
            elif (exame == 3):  # Exame Glicêmico
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
        if(escolha == 2):  # Vai verificar or resultado do Agendamento
            # Se agenda tem valor True,quer dizer que foi feito um agendamento no dia tal.
            if (diaEhora != None):
                # diaEhora = str(diaEhora)
                # diaEhora = diaEhora.replace("(", "")
                # diaEhora = diaEhora.replace(")", "")
                if (agend == 1):
                    if(diaEhora[1] == 1):
                        print(
                            f"Sua consulta está marcada para o dia {diaEhora[0]},10:30h.")
                    elif(diaEhora[1] == 2):
                        print(
                            f"Sua consulta está marcada para o dia {diaEhora[0]}, 12:45h.")
                    elif(diaEhora[1] == 3):
                        print(
                            f"Sua consulta está marcada para o dia {diaEhora[0]}, 14:10h.")
                elif(agend == 2):
                    if(diaEhora[1] == 1):
                        print(
                            f"Seu exame está marcado para o dia {diaEhora[0]},10:30h.")
                    elif(diaEhora[1] == 2):
                        print(
                            f"Seu exame está marcado para o dia {diaEhora[0]}, 12:45h.")
                    elif(diaEhora[1] == 3):
                        print(
                            f"Seu exame está marcado para o dia {diaEhora[0]}, 14:10h.")
            else:
                print("Sem Consulta ou Exame marcado.")
        opcao = int(input("Deseja continuar?\n[1]Sim\n[2]Não\n"))
        while(True):
            if (opcao == 1):
                break
            elif(opcao == 2):
                continuar = False
                break
            else:
                while (opcao != 1 and opcao != 2):
                    opcao = int(
                        input("Opção inválida,escolha [1] para Sim ou [2] para Não:\n"))


if(__name__ == "__main__"):
    resultado("Ronald Mc Donald", 1, (3,2), 2)  # Falta colocar o mês ...
