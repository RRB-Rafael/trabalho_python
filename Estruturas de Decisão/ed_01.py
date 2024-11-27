#. Solicite ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero. Exiba a mensagem correspondente.

x= int(input("Insire um número: "))

if x ==0:
    print("Zero.")
elif x>0:
    print("Positivo.")
else: 
    print("Negativo.")