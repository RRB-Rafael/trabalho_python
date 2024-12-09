#Solicite ao usuário 10 números e os armazene em uma lista. Exiba a quantidade de números que são maiores que a média da lista.

numsL= []

for i in range(10):
    nums= int(input(f"Digite o {i+1}° número: "))
    numsL.append(nums)

media= (sum(numsL))/ 10

maiorMED= sum(1 for nums in numsL if nums > media)

print(f"Quantidade de números maiores que a a média: {maiorMED}")
