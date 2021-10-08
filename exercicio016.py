#===== Desafio 016 =========
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: Digite um número: 6.127
# O número 6.127 tem a parte iteira 6.

from math import trunc
import math
num = float(input('Digite um número Real: '))
print('O número que você digitou é esse {} e sua porção inteira é {}'.format(num, math.trunc(num) ))
 