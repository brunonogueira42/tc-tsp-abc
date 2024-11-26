import matplotlib.pyplot as plt

def mostrar_percurso(cidades, melhor_solucao):
    # Ordena as cidades conforme a solução e retorna ao ponto inicial
    percurso = [cidades[i] for i in melhor_solucao] + [cidades[melhor_solucao[0]]]
    x, y = zip(*percurso)  # Extrai as coordenadas X e Y
    
    # Configura o gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(*zip(*cidades), color='red', label='Cidades', zorder=2)  # Marca as cidades
    plt.plot(x, y, color='black', linestyle='-', linewidth=1.5, label='Percurso', zorder=1)  # Traça o percurso
    
    # Adiciona rótulos para as cidades
    for i, coord in enumerate(cidades):
        plt.text(coord[0], coord[1], f"{i}", fontsize=10, ha='right', color='black')
    
    plt.title("Melhor Solução Encontrada")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.legend()
    plt.grid()
    plt.show()