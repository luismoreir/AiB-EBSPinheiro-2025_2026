# Calcular o perímetro e a área de um círculo
from math import pi, pow
#Perímetro
def perimetro_circulo(raio):
    perimetro = 2 * 3.14 * raio
    return perimetro

#Área
def area_circulo(raio):
    area = pi * pow(raio, 2)
    return area

#pedir ao utilizador o valor do raio
raio = float(input("Digite o valor do raio do círculo: "))
print("Perímetro do círculo: ", perimetro_circulo(raio))
print("Área do círculo: ", area_circulo(raio))
