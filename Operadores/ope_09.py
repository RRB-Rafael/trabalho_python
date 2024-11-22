#Crie um programa que solicite a distância percorrida (em km) e o tempo gasto (em horas) e calcule a velocidade
#média usando a fórmula: Velocidade Média = Distância / Tempo.
D= int(input("Qual a distância percorrida (em km)? "))
T= int(input("Qual foi o tempo gasto(em horas)? "))

VM= D/T
print(f"A velocidade média é: {VM}Km/h")
 
print("FIM-------------------------------------")