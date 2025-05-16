# -*- coding: utf-8 -*-
"""
Created on Fri May 16 16:18:25 2025

@author: rodri
"""

from graphics import *

def rgb_to_color(r, g, b):
    """Converte RGB para string hexadecimal (formato usado em graphics.py)"""
    return color_rgb(r, g, b)

def criar_imagem(win, largura, altura, tam_pixel):
    """Desenha uma 'imagem' de quadrados coloridos (simulação de píxeis)"""
    for x in range(0, largura, tam_pixel):
        for y in range(0, altura, tam_pixel):
            # Cor original (pode ser aleatória ou baseada em posição)
            r = (x * 5) % 256
            g = (y * 5) % 256
            b = ((x + y) * 3) % 256

            cor = rgb_to_color(r, g, b)

            quadrado = Rectangle(Point(x, y), Point(x + tam_pixel, y + tam_pixel))
            quadrado.setFill(cor)
            quadrado.setOutline(cor)
            quadrado.draw(win)

def inverter_cores(win, largura, altura, tam_pixel):
    """Desenha a imagem negativa numa nova posição"""
    offset = largura + 20  # distância horizontal para a imagem negativa

    for x in range(0, largura, tam_pixel):
        for y in range(0, altura, tam_pixel):
            # Mesma cor da geração anterior
            r = (x * 5) % 256
            g = (y * 5) % 256
            b = ((x + y) * 3) % 256

            # Inverter cores
            r_neg = 255 - r
            g_neg = 255 - g
            b_neg = 255 - b

            cor_neg = rgb_to_color(r_neg, g_neg, b_neg)

            quadrado = Rectangle(Point(x + offset, y), Point(x + tam_pixel + offset, y + tam_pixel))
            quadrado.setFill(cor_neg)
            quadrado.setOutline(cor_neg)
            quadrado.draw(win)

def main():
    largura = 300
    altura = 200
    tam_pixel = 10

    win = GraphWin("Imagem e Negativo", 2 * largura + 40, altura)
    criar_imagem(win, largura, altura, tam_pixel)
    inverter_cores(win, largura, altura, tam_pixel)

    win.getMouse()  # Espera por clique
    win.close()

main()
