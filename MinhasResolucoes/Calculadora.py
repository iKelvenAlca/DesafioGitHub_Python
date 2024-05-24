n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if isinstance(n1, int) and isinstance(n2, int):
    escolha = int(input('Digite 1 para somar, 2 para subtrair, 3 para multiplicar e 4 para dividir: '))
    if escolha == 1:
        print(n1 + n2)
    elif escolha == 2:
        print(n1 - n2)
    elif escolha == 3:
        print(n1 * n2)
    elif escolha == 4:
        if n2 != 0:
            print(n1 / n2)
        else:
            print('Erro: Divisão por zero não é permitida.')
    else:
        print('Opção inválida.')
else:
    print('Erro: Os números digitados devem ser inteiros.')