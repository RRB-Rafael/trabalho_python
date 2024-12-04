# Peça ao usuário uma palavra e exiba cada letra separadamente em linhas diferentes, usando um loop

pal= str(input("Digite uma palavra: "))
Lpa= list(pal)
q= len(Lpa)
n=0
for i in range(1,q+1):
    print(Lpa[n])
    n+=1

