#Crie um programa que solicite 5 números e armazene-os em uma lista. Substitua o maior número da lista pelo valor
#0 e exiba a lista atualizada.

numsL= []

for i in range(5):
    nums= int(input(f"Digte o {i+1}° num: "))
    numsL.append(nums)

maxnum= max(numsL)

for i in range(len(numsL)):
    if numsL[i] == maxnum:
        numsL[i] = 0 
        break

print(f"Lista atualizada: {numsL}")

