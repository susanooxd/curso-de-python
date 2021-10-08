#========= Desafio 19 =========
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
a1 = str(input('Informe o nome do aluno 1: '))
a2 = str(input('Informe o nome do aluno 2: '))
a3 = str(input('Informe o nome do aluno 3: '))
a4 = str(input('Informe o nome do aluno 4: '))
print('Sorteio: {}'. format(random.choice([a1, a2, a3, a4])))