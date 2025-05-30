# -*- coding: utf-8 -*-
"""
Created on Fri May 30 14:45:27 2025

@author: rodri
"""

def QuadradoElementos(numeros):
    for i in range(len(numeros)):
        numeros[i] = numeros[i] ** 2

def SomatorioLista(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma

def ConverteEmNumeros(ListaCaracteres):
    for i in range(len(ListaCaracteres)):
        ListaCaracteres[i] = float(ListaCaracteres[i])

# Programa principal
nome_ficheiro = input("Introduza o nome do ficheiro com a extensão(ex:. .txt): ")

# Ler o ficheiro usando readlines()
with open(nome_ficheiro, 'r') as f:
    linhas = f.readlines()

dados_limpos = [linha.strip() for linha in linhas]

ConverteEmNumeros(dados_limpos)


QuadradoElementos(dados_limpos)


resultado = SomatorioLista(dados_limpos)

print("A soma dos quadrados dos números é:", resultado)