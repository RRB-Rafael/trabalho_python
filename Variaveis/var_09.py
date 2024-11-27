#. Peça ao usuário a quantidade de dias, horas, minutos e segundos. Armazene essas informações em variáveis e
#calcule o total de segundos.

d= int(input("Dias: "))
h= int(input("Horas: "))
m= int(input("Minutos: "))
s= int(input("Segundos: "))

seg= (m*60)+(h*3600)+(d*86400)+1

print(seg)