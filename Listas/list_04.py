#Solicite ao usuário 5 nomes e armazene-os em uma lista. Exiba os nomes na ordem inversa à que foram digitados.
nomesL= []
for i in range(5):
    nomes= input(f"Digite o {i+1}° nome: ")
    nomesL.append(nomes)

for nomes in reversed(nomesL):
    print(nomes)