#Peça ao usuário três números e troque os valores da seguinte forma: o valor da primeira variável deve ser atribuído
#à segunda, o da segunda para a terceira e o da terceira para a primeira. Exiba os novos valores das variáveis.

num1=int(input("Primeiro Número: "))
num2=int(input("Segundo Número: "))
num3=int(input("Terceiro Número: "))

print(f"Os números originais: Número 1: {num1}, Número 2: {num2} e por fim Número 3: {num3}")

num1,num2,num3 = num2,num3,num1

print(f"Os números originais: Número 1: {num1}, Número 2: {num2} e por fim Número 3: {num3}")