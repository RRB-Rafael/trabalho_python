#Solicite ao usuário sua idade e verifique se ele é maior de idade (18 anos ou mais). Exiba uma mensagem informando
#se ele é maior ou menor de idade.

idade= int(input("Digite sua idade: "))

if idade>=18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")