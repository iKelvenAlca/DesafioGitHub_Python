try:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')
except ValueError:
    print('Erro: O número digitado não é inteiro.')