#Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. 
# Você deseja comprar um carro, mas o preço do carro sobe a taxa de 0,4% ao mês. 
# Escreva um programa que leia o preço de um carro hoje e calcule em quantos meses, 
# com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.
meses = 0
poupanca = 10000
carro = int(input())
while poupanca < carro:
    meses += 1
    carro = carro +carro * (0.4 /100) 
    poupanca += poupanca * (0.7 /100)
print(meses)


