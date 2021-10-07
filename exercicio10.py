#======== Desafio 10 ========
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#considerar U$1.00=3.27

dinheiro = float (input('Quanto de dinheiro você tem? '))
dolar = 3.2
result = dinheiro / dolar
print('Você tem {} de reais para comprar {} em dolar'.format(dinheiro, result))