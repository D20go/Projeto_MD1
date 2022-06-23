def fim_programa():    
    check1 = input(f'\nDeseja realizar outra operação? \n\n1 - Sim \n2 - Não \n\nDigite aqui: ')

    while not check1.isdigit():
        check1 = input('\nEntrada inválida. Deseja realizar outra operação? \n\n1 - Sim \n2 - Não \n\nDigite aqui: ')

    check1 = int(check1)

    if check1 == 1:
        check = 0
    else:
        check = 1
        print(f'\nAgradecemos seu contato. O Atende + te deseja um bom dia.\n') 
        exit()
        