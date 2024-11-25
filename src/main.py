import random

from abcd import abcd

def main():
    random.seed(2024)
    
    num_cidades = 10  # Número de cidades
    num_abelhas = 20  # Número de abelhas na população
    ciclos = 100      # Número de ciclos
    limite = 10       # Limite para abelhas exploradoras
    
    cidades = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cidades)]
    
    print("Coordenadas das cidades:")
    for i, coord in enumerate(cidades):
        print(f"Cidade {i}: {coord}")
    
    melhor_solucao, melhor_fitness = abcd(cidades, num_abelhas, ciclos, limite)
    
    print("\nMelhor solução encontrada:")
    print(f"Ordem das cidades: {melhor_solucao}")
    print(f"Distância total: {melhor_fitness:.2f}")

if __name__ == "__main__":
    main()
