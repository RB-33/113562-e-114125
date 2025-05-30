from graphics import *
import random
import time

class Door:
    def __init__(self, win, center, width, height, label):
        self.win = win
        self.center = center
        self.width = width
        self.height = height
        self.label = label
        
        # Calcular os cantos para desenhar o retângulo
        x1 = center.getX() - width/2
        y1 = center.getY() - height/2
        x2 = center.getX() + width/2
        y2 = center.getY() + height/2
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill("sienna")
        self.rect.setOutline("black")
        self.rect.setWidth(2)
        
        # Criar o texto da porta
        self.text = Text(center, f"Porta {label}")
        self.text.setSize(18)
        self.text.setStyle("bold")
        
        # Desenhar os elementos
        self.rect.draw(win)
        self.text.draw(win)
        
    def contains(self, point):
        """Verifica se um ponto está dentro da porta"""
        x, y = point.getX(), point.getY()
        x1 = self.center.getX() - self.width/2
        x2 = self.center.getX() + self.width/2
        y1 = self.center.getY() - self.height/2
        y2 = self.center.getY() + self.height/2
        
        return x1 <= x <= x2 and y1 <= y <= y2
    
    def set_color(self, color):
        """Muda a cor da porta"""
        self.rect.setFill(color)
        
    def undraw(self):
        """Remove a porta da tela"""
        self.rect.undraw()
        self.text.undraw()

class Button:
    def __init__(self, win, center, width, height, label):
        self.win = win
        self.center = center
        self.width = width
        self.height = height
        self.label = label
        
        # Calcular os cantos para desenhar o retângulo
        x1 = center.getX() - width/2
        y1 = center.getY() - height/2
        x2 = center.getX() + width/2
        y2 = center.getY() + height/2
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill("lightgray")
        self.rect.setOutline("black")
        self.rect.setWidth(2)
        
        # Criar o texto do botão
        self.text = Text(center, label)
        self.text.setSize(14)
        self.text.setStyle("bold")
        
        # Desenhar os elementos
        self.rect.draw(win)
        self.text.draw(win)
        
    def contains(self, point):
        """Verifica se um ponto está dentro do botão"""
        x, y = point.getX(), point.getY()
        x1 = self.center.getX() - self.width/2
        x2 = self.center.getX() + self.width/2
        y1 = self.center.getY() - self.height/2
        y2 = self.center.getY() + self.height/2
        
        return x1 <= x <= x2 and y1 <= y <= y2
    
    def set_color(self, color):
        """Muda a cor do botão"""
        self.rect.setFill(color)
        
    def undraw(self):
        """Remove o botão da tela"""
        self.rect.undraw()
        self.text.undraw()

def main():
    # Configuração da janela
    win = GraphWin("Three Button Monte", 800, 600)
    win.setBackground("lightblue")
    
    # Título do jogo
    title = Text(Point(400, 50), "Jogo Monte - Encontre o Prêmio!")
    title.setSize(24)
    title.setStyle("bold")
    title.setTextColor("darkblue")
    title.draw(win)
    
    # Criar portas
    doors = [
        Door(win, Point(200, 300), 120, 200, 1),
        Door(win, Point(400, 300), 120, 200, 2),
        Door(win, Point(600, 300), 120, 200, 3)
    ]
    
    # Criar botão de saída
    quit_button = Button(win, Point(700, 550), 100, 40, "Sair")
    
    # Área de status
    status_bg = Rectangle(Point(50, 500), Point(350, 580))
    status_bg.setFill("white")
    status_bg.setOutline("gray")
    status_bg.setWidth(2)
    status_bg.draw(win)
    
    status_text = Text(Point(200, 530), "Bem-vindo! Escolha uma porta para começar.")
    status_text.setSize(11)
    status_text.draw(win)
    
    wins_text = Text(Point(100, 560), "Vitórias: 0")
    wins_text.setSize(11)
    wins_text.draw(win)
    
    losses_text = Text(Point(300, 560), "Derrotas: 0")
    losses_text.setSize(11)
    losses_text.draw(win)
    
    # Variáveis do jogo
    wins = 0
    losses = 0
    game_active = True
    
    # Loop principal do jogo
    while game_active:
        # Selecionar porta premiada aleatoriamente
        winning_door = random.choice([1, 2, 3])
        
        # Aguardar a escolha do jogador
        choice = None
        while choice is None and game_active:
            click = win.getMouse()
            
            # Verificar se clicou no botão de saída
            if quit_button.contains(click):
                game_active = False
                break
            
            # Verificar se clicou em alguma porta
            for door in doors:
                if door.contains(click):
                    choice = door.label
                    break
        
        if not game_active:
            break
        
        # Processar escolha do jogador
        if choice == winning_door:
            # Vitória!
            wins += 1
            status_text.setText("Parabéns! Você encontrou o prêmio! 🏆")
            doors[choice-1].set_color("gold")
        else:
            # Derrota
            losses += 1
            status_text.setText(f"Que pena! O prêmio estava na Porta {winning_door}. Tente novamente!")
            doors[choice-1].set_color("red")
            doors[winning_door-1].set_color("gold")
        
        # Atualizar contadores
        wins_text.setText(f"Vitórias: {wins}")
        losses_text.setText(f"Derrotas: {losses}")
        
        # Pausa para mostrar o resultado
        time.sleep(2)
        
        # Resetar as cores das portas
        for door in doors:
            door.set_color("sienna")
    
    # Fechar a janela ao sair
    win.close()

if __name__ == "__main__":
    main()