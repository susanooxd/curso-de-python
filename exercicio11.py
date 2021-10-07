#========= Desafio 11 ============
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta, pinta uma áre de 2m quadrados

altura = float (input('Informe a altura da parede em Metros: '))
largura = float (input('Informe a largura da parede em Metros: '))
area = altura * largura
tintas = area / 2
print('A area dessa parede é {}M , sera necessario {}L de tinta para pintá-la.'.format(area, tintas))