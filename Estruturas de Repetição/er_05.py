#Peça ao usuário 5 números inteiros e exiba a soma desses números. Use um loop para realizar as entradas.

soma= 0

for i in range(5):
    num= int(input(f"Digite o {i+1}° número inteiro: "))
    soma+= num

print(f"A soma dos números é: {soma}")