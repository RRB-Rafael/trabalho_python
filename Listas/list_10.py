#Solicite ao usuário duas listas de 5 números cada. Em seguida, crie e exiba uma nova lista contendo a soma dos
#elementos correspondentes de cada lista.

list1= []
list2= []

for i in range(5):
    nums= int(input(f"igite o {i+1}° num: "))
    list1.append(nums)

print("Agora digite os 5 números para a segunda lista: ")
for i in range(5):
    nums=int(input(f"Digite o {i+1}° num: "))
    list2.append(nums)

soma= [list1[i] + list2[i] for i in range(5)]

print("O resultado da soma é: ")
print(soma)
