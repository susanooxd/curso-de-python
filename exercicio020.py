#======== Desafio 20 =====
# 
# O mesmo professor do desafio anterior quer sortear a ordem de apresentaçãode trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
#
import random

a1 = (input('Informe o nome do aluno 1: '))
a2 = (input('Informe o nome do aluno 2: '))
a3 = (input('Informe o nome do aluno 3: '))
a4 = (input('Informe o nome do aluno 4: '))
n = [a1, a2, a3, a4]
sorteio = random.sample(a1, k4)
print('A ordem de apresentação é', sorteio)
