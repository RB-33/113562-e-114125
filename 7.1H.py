import tkinter as tk

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Circulo:
    def __init__(self, centro, raio, cor="black"):
        self.centro = centro
        self.raio = raio
        self.cor = cor
        self.id = None  

    def move(self, dx, dy):
        self.centro.move(dx, dy)

    def desenha(self, canvas):
        x, y = self.centro.x, self.centro.y
        r = self.raio
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.cor, outline="black")

class GrupoGrafico:
    def __init__(self, ancora):
        self.ancora = ancora
        self.objetos = []

    def retornaAncora(self):
        return self.ancora

    def adicionaObjeto(self, objeto):
        self.objetos.append(objeto)

    def move(self, dx, dy):
        self.ancora.move(dx, dy)
        for obj in self.objetos:
            obj.move(dx, dy)

    def desenha(self, canvas):
        for obj in self.objetos:
            obj.desenha(canvas)

    def apaga(self, canvas):
        for obj in self.objetos:
            if obj.id:
                canvas.delete(obj.id)
        self.objetos.clear()


def main():

    janela = tk.Tk()
    janela.title("Grupo Gráfico - Cara com olhos")

    largura, altura = 400, 400
    canvas = tk.Canvas(janela, width=largura, height=altura, bg="white")
    canvas.pack()

  
    ancora = Ponto(200, 200)
    cara = GrupoGrafico(ancora)

   
    olho_esq = Circulo(Ponto(180, 180), 10, "blue")
    olho_dir = Circulo(Ponto(220, 180), 10, "blue")
    cabeca = Circulo(Ponto(200, 200), 50, "yellow")

   
    cara.adicionaObjeto(cabeca)
    cara.adicionaObjeto(olho_esq)
    cara.adicionaObjeto(olho_dir)

    
    cara.desenha(canvas)

    
    def mover_para(event):
        dx = event.x - cara.retornaAncora().x
        dy = event.y - cara.retornaAncora().y
        canvas.delete("all")  
        cara.move(dx, dy)
        cara.desenha(canvas)

    
    canvas.bind("<Button-1>", mover_para)

    
    janela.mainloop()



main()



