import random

from abcd import abcd

from grafico import mostrar_percurso

def main():
    # Seed definida para garantir integridade dos teste com diferentes conjuntos de parâmetros
    random.seed(2024)
    
    # Parâmetros do problema e do algoritmo
    num_cidades = 10  # Número de cidades
    num_abelhas = 20  # Número de abelhas na população
    ciclos = 100      # Número de ciclos
    limite = 10       # Limite para abelhas exploradoras
    
    # Gera coordenadas aleatórias para as cidades
    cidades = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cidades)]
    
    # Exibe as coordenadas das cidades geradas
    print("Coordenadas das cidades:")
    for i, coord in enumerate(cidades):
        print(f"Cidade {i}: {coord}")
    
    # Executa o algoritmo ABC
    melhor_solucao, melhor_fitness = abcd(cidades, num_abelhas, ciclos, limite)
    
    # Exibe a melhor solução encontrada
    print("\nMelhor solução encontrada:")
    print(f"Ordem das cidades: {melhor_solucao}")
    print(f"Distância total: {melhor_fitness:.2f}")

    mostrar_percurso(cidades, melhor_solucao)

if __name__ == "__main__":
    main()
