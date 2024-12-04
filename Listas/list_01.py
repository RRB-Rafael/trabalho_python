#Crie um programa que solicite ao usuário 5 números e os armazene em uma lista. Em seguida, exiba a lista completa.
lista= [0,0,0,0,0]
wa=0
for i in range(1,6):
    n= int(input("Insira um número: "))
    lista[wa]=n
    wa+=1

print(lista)

