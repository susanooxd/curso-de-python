#====== Desafio 13 ==========
# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe seu Salário atual: '))
aument = salario * 0.15
salarioAum = salario + aument
print('Seu salário de {}R$ recebeu {}R$ de aumento e foi para {}R$ com o aumento de 15%'.format(salario, aument, salarioAum))