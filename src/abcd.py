import random
import math

def iniciar_populacao(abelhas, num_cidades):
    populacao = []

    for _ in range(abelhas):
        solucao = list(range(num_cidades))
        random.shuffle(solucao)
        populacao.append(solucao)
    
    return populacao
    
def calcular_distancia(solucao, cidades):
    distancia = 0

    for i in range(len(solucao) - 1):
        cidade_atual = cidades[solucao[i]]
        proxima_cidade = cidades[solucao[i + 1]]
        # Formula da Distancia Euclidiana é d = raiz((x2 - x1)² + (y2 - y1)²)
        distancia += math.sqrt((cidade_atual[0] - proxima_cidade[0])**2 + (cidade_atual[1] - proxima_cidade[1])**2)
    # Agora adiciona a cidade inicial e a final
    cidade_inicial = cidades[solucao[0]]
    cidade_final = cidades[solucao[-1]]
    distancia += math.sqrt((cidade_final[0] - cidade_inicial[0])**2 + (cidade_final[1] - cidade_inicial[1])**2)
    
    return distancia
    
def gerar_solucao_candidata(solucao):
    print("gerar_solucao_candidata") # utilizar equação de modificação?
    
def escolher_melhor_solucao(solucao, solucao_candidata):
    print("escolher_melhor_solucao")
    
def calcular_probabilidades(fitness):
    print("calcular_probabilidade")

def abc(cidades, abelhas, ciclos, limite, seed=2024):

    if seed is not None:
        random.seed(seed)

    num_cidades = len(cidades)
    populacao = iniciar_populacao(abelhas, num_cidades)
    fitness = [calcular_distancia(solucao, cidades) for solucao in populacao]
    tentativas = [0] * abelhas
    
    i = fitness.index(min(fitness))
    melhor_solucao = populacao[i]
    melhor_fitness = fitness[i]
    
    for ciclo in range(ciclos):
        for i in range(abelhas):
            solucao_candidata = gerar_solucao_candidata(populacao[i])
            populacao[i] = escolher_melhor_solucao(populacao[i], solucao_candidata)
            fitness[i] =  calcular_distancia(populacao[i], cidades)
            
        probabilidades = calcular_probabilidades(fitness)
        for i in range(abelhas):
            j =  # abelha observadora escolhe uma solução baseado nas probabilidades
            solucao_candidata = gerar_solucao_candidata(populacao[j])
            populacao[j] = escolher_melhor_solucao(populacao[j], solucao_candidata)
            fitness[j] =  calcular_distancia(populacao[j], cidades)
            
        for i in range(abelhas):
            if tentativas[i] > limite:
                populacao[i] = # nova solução é gerada aleatóriamente
                fitness[i] = calcular_distancia(populacao[i], cidades)
                tentativas[i] = 0
        
        i = fitness.index(min(fitness))
        melhor_solucao = populacao[i]
        melhor_fitness = fitness[i]
        
    return melhor_solucao, melhor_fitness
