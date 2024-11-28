#Peça ao usuário um número inteiro de 1 a 7 e exiba o dia da semana correspondente (1 para domingo, 2 para
#segunda, e assim por diante). Caso o número não esteja no intervalo de 1 a 7, exiba uma mensagem de erro.

num= int(input("Insira um número de 1 a 7: "))

if num ==1:
    print("Domingo")
elif num==2:
    print("Segunda")
elif num ==3:
    print("Terça")
elif num ==4:
    print("Quarta")
elif num==5:
    print("Quinta")
elif num==6:
    print("Sexta")
elif num==7:
    print("Sabádo")
else:
    print("Não a nenhum dia da semana correspondente a este número")