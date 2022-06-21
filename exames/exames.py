import calendar
aa = 2022
mm = 7

while True:
    def ex(exames):
        if exames == '1':
            print (f'Você selecionou exame de {ex1}. Selecione entre as datas disponíveis: \n {calendar.month(aa,mm)}')
            data = int(input('Digite um dia em formato dd: \n '))
            while (data < 1) or (data > 30):
                data = int(input('Dia inválido. Digite um dia em formato dd: \n '))

            hora = input(f'Escolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n')
            while (hora <'1') or (hora >'3'):
                hora = input(f'Horário não disponível. \nEscolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n ')
            
            print (f"Exame {ex1} agendado em {data}/07 no horário {hora} com sucesso! \nVocê receberá um SMS para a confirmação do seu agendamento.")
            return data, hora
        
        elif exames == '2':
            print (f'Você selecinou exame {ex2}. Selecione entre as datas disponíveis: \n{calendar.month(aa,mm)} ')
            data = int(input('Digite um dia em formato dd: \n '))
            while (data < 1) and (data > 30):
                data = int(input('Dia inválido. Digite um dia em formato dd: \n '))

            hora = int(input(f'Escolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n'))
            while (hora <1) or (hora >3):
                hora = input(f'Horário não disponível. \nEscolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n ')

            print (f"Exame {ex2} agendado em {data}/07 no horário {hora} com sucesso! \nVocê receberá um SMS para a confirmação do seu agendamento.")
            return data, hora            
        
        elif exames == '3':
            print (f'Você selecionou exame de {ex3}. Selecione entre as datas disponíveis: \n{calendar.month(aa,mm)}')
            data = input ('Digite um dia em formato dd: \n ')
            while (data < '1') and (data > '30'):
                data = int(input('Dia inválido. Digite um dia em formato dd: \n '))

            hora = input(f'Escolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n')
            while (hora <'1') or (hora >'3'):
                hora = input(f'Horário não disponível. \nEscolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n ')

            print (f"Exame {ex1} agendado em {data}/07 no horário {hora} com sucesso! \nVocê receberá um SMS para a confirmação do seu agendamento.")
            return data, hora
  
    
    ex1 = 'Hemograma'
    ex2 = 'Parasitológico'
    ex3 = 'Glicemico'
    hr1 = '10:30h'
    hr2 = '12:45h'
    hr3 = '14:10h' 
    nome = str(input('Digite seu nome: '))
    exames = input(f'Olá {nome}! Selecione o exame desejado: \n 1.{ex1} \n 2.{ex2} \n 3.{ex3} \n ')
    while (exames != '1') and (exames != '2') and (exames != '3'):
        exames = input(f'Opção inválida, {nome}. Selecione o exame desejado: \n 1.{ex1} \n 2.{ex2} \n 3.{ex3} \n ')

    print(ex(exames))