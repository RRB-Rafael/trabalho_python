'''
Crie um programa que peça ao usuário seu peso e sua altura, calcule o IMC (Índice de Massa Corporal) e informe:
 Abaixo do peso, se o IMC for menor que 18,5.
 Peso normal, se o IMC estiver entre 18,5 e 24,9.
 Acima do peso, se o IMC for maior que 24,9.
'''

p= int(input("Quanto você pesa? "))
al= float(input("Quanto de altura você tem? "))

imc= p/al**2

print(f"O seu IMC é {imc}.")

if imc<18.5:
    print("Abaixo do peso.")
elif imc>=18.5 and imc<24.9:
    print("Peso normal")
elif imc>=24.9:
    print("Acima do peso")