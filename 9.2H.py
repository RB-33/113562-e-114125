# -*- coding: utf-8 -*-
"""
Created on Fri May 16 13:54:36 2025

@author: rodri
"""

from graphics import *

def rgb2gray(r, g, b):
    # Fórmula de brilho ponderado
    return int(round(0.299 * r + 0.587 * g + 0.114 * b))

def main():
    # Nome do ficheiro de entrada (GIF ou PPM)
    nome_entrada = input("Nome do ficheiro de imagem (GIF ou PPM): ")

    # Cria imagem original com a imagem fornecida
    img = Image(Point(0, 0), nome_entrada)
    largura = img.getWidth()
    altura = img.getHeight()

    # Cria nova imagem em branco para tons de cinza
    img_gray = Image(Point(largura/2, altura/2), largura, altura)

    # Percorre cada pixel e converte para cinzento
    for y in range(altura):
        for x in range(largura):
            r, g, b = img.getPixel(x, y)
            brilho = rgb2gray(r, g, b)
            img_gray.setPixel(x, y, color_rgb(brilho, brilho, brilho))
        print(f"Linha {y+1}/{altura} processada.")

    # Cria janela com tamanho adequado
    win = GraphWin("Imagem em tons de cinza", largura, altura)
    img_gray.draw(win)

    # Pede nome de saída
    nome_saida = input("Nome para guardar imagem em cinzento (ex: saida.ppm): ")
    img_gray.save(nome_saida)

    win.getMouse()
    win.close()

main()

