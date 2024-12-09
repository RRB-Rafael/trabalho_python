#Peça ao usuário uma lista de números inteiros e calcule a soma de todos os elementos da lista.

ns= []
quant= int(input("Quantos númers você deseja que seja somado? "))

for i in range(quant):
    n= int(input(f"Digite o {i+1}° número: "))
    ns.append(n)

soma= sum(ns)
print(f"A soma de todos os números digitados é {soma}")