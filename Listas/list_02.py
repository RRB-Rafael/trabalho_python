# Solicite ao usuário uma lista de números, separando-os por espaços (ex.: "1 2 3 4 5"). Converta a entrada para uma
# lista e exiba o maior e o menor número da lista

wa = input("Digite uma lista de números separados por espaços: ")
n = list(map(int, wa.split()))

maxn= max(n)
minn= min(n)

print(f"O maior número é: {maxn} - O menor número é: {minn}")
