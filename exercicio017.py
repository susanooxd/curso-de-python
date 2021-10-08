# ======= Desafio 017 =========
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
import math
oposto = int (input('Informe o cateto Oposto: '))
adjacente = int (input('Infome o cateto Adjacente: '))
soma = (oposto*oposto) + (adjacente*adjacente )
raiz = math.sqrt(soma)


print('a Hipotenusa do cateto oposto {} e do cateto Adjacente {} é {}'.format(oposto, adjacente, raiz))