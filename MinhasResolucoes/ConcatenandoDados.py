x = input('Escreva algo: ')
y = input('Escreva mais algo, por favor: ')

if x==int:
    x = str(x)
if y==int:
    y = str(y)
    
print(f'Foi digitado {x} e {y}.')