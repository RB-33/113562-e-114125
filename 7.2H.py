def criar_ficheiro_dados():
    dados = """1000
1200 10
1450 12
1800 14
"""
    with open("dados.txt", "w") as f:
        f.write(dados)

criar_ficheiro_dados()
print("Ficheiro 'dados.txt' criado com sucesso.")

def ler_dados(ficheiro):
    with open(ficheiro, "r") as f:
        linhas = f.readlines()
    
    odometro_inicial = int(linhas[0])
    trajetos = []

    for linha in linhas[1:]:
        partes = linha.strip().split()
        if len(partes) == 2:
            odometro_final = int(partes[0])
            litros = float(partes[1])
            trajetos.append((odometro_final, litros))
    
    return odometro_inicial, trajetos

def calcular_consumos(odometro_inicial, trajetos):
    consumos = []
    total_km = 0
    total_litros = 0

    for odometro_final, litros in trajetos:
        distancia = odometro_final - odometro_inicial
        consumo_medio = (litros / distancia) * 100
        consumos.append(consumo_medio)
        
        total_km += distancia
        total_litros += litros
        odometro_inicial = odometro_final  # preparar para o próximo trajeto
    
    consumo_total = (total_litros / total_km) * 100 if total_km != 0 else 0
    return consumos, consumo_total

def main():
    nome_ficheiro = "dados.txt"
    odometro_inicial, trajetos = ler_dados(nome_ficheiro)
    consumos, consumo_total = calcular_consumos(odometro_inicial, trajetos)

    for i, c in enumerate(consumos, 1):
        print(f"Consumo médio no trajeto {i}: {c:.2f} L/100km")
    
    print(f"\nConsumo médio total da viagem: {consumo_total:.2f} L/100km")

main()

