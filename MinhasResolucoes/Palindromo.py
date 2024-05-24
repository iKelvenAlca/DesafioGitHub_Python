def palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]
    return palavra, palavra_invertida

palavra = input('Digite uma palavra: ')

palavra_original, palavra_invertida = palindromo(palavra)

print(f'Palavra original: {palavra_original}')
print(f'Palavra invertida: {palavra_invertida}')
print(f'É um palíndromo? {palavra_original == palavra_invertida}')
