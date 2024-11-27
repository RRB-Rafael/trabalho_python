#Peça ao usuário dois números e um operador matemático (+, -, *, /). Realize a operação correspondente e exiba o
#resultado. Caso o operador informado seja inválido, exiba uma mensagem de erro.
ope= input("Qual operação deseja realizar com os números inseridos? (Subtração, Adição, Multiplicação ou Divisão) ")
num1= int(input("Insira um número: "))
num2= int(input("Insira um número: "))


if ope=="Subtração":
    sub=num1-num2
    print(sub)
elif ope=="Adição":
    ad= num1+num2
    print(ad)
elif ope=="Multiplicação":
    mult= num1*num2
    print(mult)
elif ope=="Divisão":
    div= num1/num2
    print(div)
else: 
    print("Oxi??")