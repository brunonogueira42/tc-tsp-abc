import random
import math

def iniciar_populacao(num_abelhas, num_cidades):
    populacao = []

    for _ in range(num_abelhas):
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
    solucao_candidata = solucao[:]
    # Troca duas cidades de lugar aleatoriamente
    a, b = random.sample(range(len(solucao)), 2)
    solucao_candidata[a], solucao_candidata[b] = solucao_candidata[b], solucao_candidata[a]
    return solucao_candidata
    
def escolher_melhor_solucao(solucao, solucao_candidata, cidades):
    distancia_atual = calcular_distancia(solucao, cidades)
    distancia_candidata = calcular_distancia(solucao_candidata, cidades)
    return solucao_candidata if distancia_candidata < distancia_atual else solucao
    
def calcular_probabilidades(fitness):
    inverso_fitness = [1 / f for f in fitness]
    total = sum(inverso_fitness)
    return [f / total for f in inverso_fitness]

def abc(cidades, num_abelhas, ciclos, limite, seed=2024):
    if seed is not None:
        random.seed(seed)

    num_cidades = len(cidades)
    populacao = iniciar_populacao(num_abelhas, num_cidades)
    fitness = [calcular_distancia(solucao, cidades) for solucao in populacao]
    tentativas = [0] * num_abelhas
    
    i = fitness.index(min(fitness))
    melhor_solucao = populacao[i]
    melhor_fitness = fitness[i]
    
    for _ in range(ciclos):
        # Fase das abelhas empregadas
        for i in range(num_abelhas):
            solucao_candidata = gerar_solucao_candidata(populacao[i])
            nova_solucao = escolher_melhor_solucao(populacao[i], solucao_candidata, cidades)
            if nova_solucao == populacao[i]:
                tentativas[i] += 1
            else:
                tentativas[i] = 0
            populacao[i] = nova_solucao
            fitness[i] = calcular_distancia(populacao[i], cidades)
        
        # Fase das abelhas observadoras
        probabilidades = calcular_probabilidades(fitness)
        for _ in range(num_abelhas):
            i = random.choices(range(num_abelhas), probabilidades)[0]
            solucao_candidata = gerar_solucao_candidata(populacao[i])
            nova_solucao = escolher_melhor_solucao(populacao[i], solucao_candidata, cidades)
            if nova_solucao == populacao[i]:
                tentativas[i] += 1
            else:
                tentativas[i] = 0
            populacao[i] = nova_solucao
            fitness[i] = calcular_distancia(populacao[i], cidades)
        
        # Fase das abelhas escoteiras
        for i in range(num_abelhas):
            if tentativas[i] > limite:
                populacao[i] = list(range(num_cidades))
                random.shuffle(populacao[i])
                fitness[i] = calcular_distancia(populacao[i], cidades)
                tentativas[i] = 0
        
        # Atualizar a melhor solução global
        i = fitness.index(min(fitness))
        if fitness[i] < melhor_fitness:
            melhor_solucao = populacao[i]
            melhor_fitness = fitness[i]
        
    return melhor_solucao, melhor_fitness