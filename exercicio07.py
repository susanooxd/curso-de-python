#========== Desafio 07 =======
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nota1 = int (input('Digite a primeira nota sua: '))
nota2 = int (input('Digite a segunda nota sua: '))
media = (nota1 + nota2) / 2
print('Você tirou no primeiro semestre {}, no segundo semestre {}, a média das notas ficou {}'.format(nota1, nota2, media))
