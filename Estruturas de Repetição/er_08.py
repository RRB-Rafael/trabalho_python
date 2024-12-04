#Escreva um programa que exiba a tabuada de multiplicação de 1 a 10 para um número informado pelo usuário.
n=int(input("Insira um número: "))
nn=1
for i in range(1,11):
    mult= n*nn
    print(f"{n} x {nn} = {mult}")
    nn+=1