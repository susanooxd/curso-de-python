#====== Desafio 08 =======
# Escreve um programa que leia um valor em metros e o exiba convertido em centimentros a milimetros

valor = float(input('Digite um valor em metros para converter em centimentros e milimetros: '))
centimetros = 100
milimetros  = 100 * 0,001
valorCenti = valor * centimetros

print('O valor em metros é {}M, convertido em centimentros {}CM, convertido em milimetros {}MM'.format(valor, valorCenti, milimetros))

