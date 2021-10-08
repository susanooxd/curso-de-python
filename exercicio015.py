#========= Desafio 15 ========
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelo quaios ele foi alugado. Calcule o preço a pagar, sabendo q o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Kms o carro percorreu: '))
dias = int (input('Quantos dias alugado: '))
valor = ( dias * 60 ) + (km * 0.15 )
print('O carro alugado percorreu {}Km, foi alugado por {} Dias, o valor a pagar sera de {}'.format(km, dias, valor))