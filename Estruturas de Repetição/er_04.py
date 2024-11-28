#Solicite ao usuário um número inteiro positivo e calcule o fatorial desse número usando um loop. Exiba o resultado.

num= int(input("Insira um número: "))
fat=1

if num<0:
    print("Tá errado isso ae")
else:
    for i in range(1,num+1):
        fat*=i

print(f"A fatorial do número {num} é: {fat}")