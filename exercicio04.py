print('\n ======== DESAFIO 04 implementado ========')
#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela

frase = str(input('Digite algo: '))
print('O tipo primitivo desse valor é {}'.format(type(frase)))
print('Só tem espaços? {}'.format(frase.isspace())) 
print('É um número? {} '.format(frase.isnumeric()))
print('É um alfabético? {} '.format(frase.isalpha()))
print('É um alfanumérico? {} '.format(frase.isalnum()))
print('Esta em maiúsculas? {}'.format(frase.isupper()))
print('Esta em minúsculo {}'.format(frase.islower()))
print('Esta copilatizado? {} '.format(frase.istitle()))
