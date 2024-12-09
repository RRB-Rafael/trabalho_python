#Crie um programa que solicite ao usuário 10 números e os armazene em uma lista. Depois, exiba apenas os números pares da lista.

nL= []

for i in range(10):
    n= int(input(f"Digite o {i+1}° número: "))
    nL.append(n)

print(f"Os números em uma lista: {nL}")

print("De todos os números presentes na lista, estes são os pares: ")
for n in nL:
    if n%2==0:
        print(n)
