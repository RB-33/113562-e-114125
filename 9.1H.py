# -*- coding: utf-8 -*-
"""
Created on Fri May 16 13:43:39 2025

@author: rodri
"""

from graphics import *

def media(valores):
    return sum(valores) / len(valores)

def calcula_coeficientes(x, y):
    n = len(x)
    x_bar = media(x)
    y_bar = media(y)
    numerador = sum(x[i]*y[i] for i in range(n)) - n * x_bar * y_bar
    denominador = sum(x[i]**2 for i in range(n)) - n * x_bar**2
    m = numerador / denominador
    return m, x_bar, y_bar

def main():
    # Cria janela gráfica
    win = GraphWin("Regressão Linear", 600, 600)
    win.setCoords(0, 0, 100, 100)  # coordenadas do utilizador

    # Desenha botão "Concluído"
    botao = Rectangle(Point(5, 5), Point(20, 15))
    botao.setFill("lightgray")
    botao.draw(win)
    texto_botao = Text(Point(12.5, 10), "Concluído")
    texto_botao.draw(win)

    # Lista de pontos
    x_vals = []
    y_vals = []

    # Recebe pontos
    while True:
        click = win.getMouse()
        x, y = click.getX(), click.getY()
        
        if 5 <= x <= 20 and 5 <= y <= 15:
            break

        # Desenha ponto
        ponto = Circle(Point(x, y), 0.7)
        ponto.setFill("blue")
        ponto.draw(win)

        x_vals.append(x)
        y_vals.append(y)

    if len(x_vals) >= 2:
        # Calcula a regressão
        m, x_bar, y_bar = calcula_coeficientes(x_vals, y_vals)

        # Calcula extremos da linha de regressão
        x1 = min(x_vals)
        x2 = max(x_vals)
        y1 = y_bar + m * (x1 - x_bar)
        y2 = y_bar + m * (x2 - x_bar)

        # Desenha linha
        linha = Line(Point(x1, y1), Point(x2, y2))
        linha.setOutline("red")
        linha.draw(win)

    # Espera clique final para fechar
    win.getMouse()
    win.close()

main()
