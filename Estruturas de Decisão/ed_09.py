#Solicite ao usuário um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4 e não por 100,
#exceto se for divisível por 400.

ano= int(input("Insira um ano: "))

if ano % 4 == 0 or ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")