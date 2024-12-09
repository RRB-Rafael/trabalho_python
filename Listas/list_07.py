#Crie um programa que armazene os números de 1 a 20 em uma lista e exiba apenas os números múltiplos de 3.

numsL = list(range(1,21))

print("Os números multiplos de 3 é: ")

for nums in numsL: 
    if nums %3==0:
        print(nums)