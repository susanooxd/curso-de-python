#========= Desafio 14 =========
# Escreva um programa que converta uma temperatura  digitando em graus Celsius e converta para graus Fahrenheit
c = float(input('Qual a temperatura em graus Celsius: '))
f = c * 1.8 + 32
print('A temperatura de {}C para {}F'.format(c, f))