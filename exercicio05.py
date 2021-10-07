# ====== Desafio 05 =========
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um númrero: '))
antecessor = 1  
sucessor = 1
resultAntecessor = numero - antecessor
resultSucessor = sucessor + numero
print('seu número é {}, antecessor é {}, e sucessor {}  '.format(numero, resultAntecessor, resultSucessor))