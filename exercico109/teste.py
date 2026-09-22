
sair = int

while sair != 0:
    a = int(input('valor de A: '))
    b = int(input('Valor de B: '))
    print("\n\t== MENU == \n")
    print("1 - somar\n2 - Multiplicar\n3 - Dividir\n4 - Subtrair\n0 - Sair\n\n")
    opcao = int(input('Opção: '))

    match opcao:
        case 1:
            soma = a + b
            print(f'{a} + {b} = {soma}')
        case 2:
            mult = a * b
            print(f'{a} x {b} = {mult}')
        case 3:
            div = a // b
            print(f'{a} /  {b} = {div}')
        case 4:
            sub = a - b
            print(f'{a} - {b} = {sub}')
        case 0:
            break
        case _:
            print('opcao invalida!!')
         
    sair = int(input('Digite 0 encerrar a calculadora ou 9 para continuar: '))
    if sair == 0:
        break


