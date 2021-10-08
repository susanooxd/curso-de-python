#
# ======== Desafio 018 =========
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

angulo = int(input('Informe o ângulo: '))
print('O seno é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}, do angulo{}'.format(math.sin(angulo),math.cos(angulo), math.tan(angulo), angulo) )