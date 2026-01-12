# Funções matemáticas básicas
#Soma
def soma (n1,n2):
    soma = n1 + n2
    return soma

#Subtração
def subtracao (n1,n2):
    subtracao = n1 - n2
    return subtracao

#Multiplicação
def multiplicacao (n1,n2):
    multiplicacao = n1 * n2
    return multiplicacao

#Divisão
def divisao (n1,n2):
    if n2 == 0:
        return "Erro: Divisão por zero não é permitida."
    divisao = n1 / n2
    return divisao

#Potência
def potencia (n1,n2):
    potencia = n1 ** n2
    return potencia

#Raiz Quadrada
def raiz_quadrada (n1):
    if n1 < 0:
        return "Erro: Raiz quadrada de número negativo não é permitida."
    raiz_quadrada = n1 ** 0.5
    return raiz_quadrada

#Raiz Cúbica
def raiz_cubica (n1):
    raiz_cubica = n1 ** (1/3)
    return raiz_cubica

#Percentagem
def percentagem (n1,n2):
    percentagem = (n1 / 100) * n2
    return percentagem

#Fatorial
def fatorial (n1):
    if n1 < 0:
        return "Erro: Fatorial de número negativo não é definido."
    fatorial = 1
    for i in range(1, n1 + 1):
        fatorial *= i
    return fatorial

#Logaritmo
def logaritmo (n1, base=10):   
    import math
    if n1 <= 0:
        return "Erro: Logaritmo de número não positivo não é definido."
    logaritmo = math.log(n1, base)
    return logaritmo

#Funções trigonométricas
#Seno, Cosseno e Tangente
def seno (n1):
    import math
    seno = math.sin(math.radians(n1))
    return seno

def cosseno (n1):
    import math
    cosseno = math.cos(math.radians(n1))
    return cosseno

def tangente (n1):
    import math
    tangente = math.tan(math.radians(n1))
    return tangente


#Outras funções matemáticas
def arredondar (n1):
    arredondar = round(n1)
    return arredondar

def valor_absoluto (n1):
    valor_absoluto = abs(n1)
    return valor_absoluto

def minimo (n1, n2):
    minimo = min(n1, n2)
    return minimo

def maximo (n1, n2):
    maximo = max(n1, n2)
    return maximo

def media (lista):
    if len(lista) == 0:
        return "Erro: A lista está vazia."
    media = sum(lista) / len(lista)
    return media
