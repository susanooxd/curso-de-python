# ==== Desafio 12 ===
#Faça um algortmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.


preco = float (input('Qual o valor do produto: '))
desc = preco * 0.05
precoDesc = preco - desc
print('O valor do produto é {}R$, voce recebeu {}R$ de desconto, o valor fica {}R$ '.format(preco, desc, precoDesc))