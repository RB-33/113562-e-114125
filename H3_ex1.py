
#Programa faz uma tabela de conver~sao de graus Celsius para Fahrenheit
#Rodrig Barradas V1
def tabela():
 print("|  Celsius\t|\tFahrenheit  |")
 print("----------------------------")
 for celsius in range(0, 101, 10):
        fahrenheit = 9 / 5 * celsius + 32
        print(f"|\t{celsius:>3}\t\t|{int(fahrenheit):9}      |")
tabela()