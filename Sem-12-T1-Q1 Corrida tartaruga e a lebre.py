#A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair n sua frente. 
# A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto. Faça um programa que 
# leia quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até que a lebre alcance 
# a tartaruga. Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.

lebre = 0
minutos= 0
tartaruga = int(input())
while lebre < tartaruga:
    tartaruga += 1
    lebre += 10
    minutos +=1
print(minutos)