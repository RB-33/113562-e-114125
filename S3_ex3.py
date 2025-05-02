def main():
    print()
    print("Este programa conta o número de palavras da frase que inserir.")
    frase = input("Introduza a frase: ")
    count = 0
    for i in frase.split():
        count = count + 1
    print()
    print(f"A frase tem {count} palavras")

main()

from graphics import*
