# Escreva um programa que recebe um número inteiro e testa e imprime se ele é par ou impar

num = int(input("Digite um número: "))
check = num % 2
if check == 0:
  print(f"{num} é par.")
else:
  print(f"{num} é ímpar.")
