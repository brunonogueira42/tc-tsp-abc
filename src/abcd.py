import random
import math

def iniciar_populacao(num_abelhas, num_cidades):
    """
    Inicializa uma população de abelhas com soluções aleatórias.

    Args:
        num_abelhas (int): Número de abelhas na população.
        num_cidades (int): Número de cidades a serem visitadas.

    Returns:
        list: Lista de soluções iniciais, onde cada solução é uma rota com os índices do percurso.
    """
    populacao = []

    for _ in range(num_abelhas):
        solucao = list(range(num_cidades))
        random.shuffle(solucao)
        populacao.append(solucao)
    
    return populacao
    
def calcular_distancia(solucao, cidades):
    """
    Calcula a distância total de uma solução com base na distância euclidiana entre as cidades.

    Args:
        solucao (list): Sequência de índices representando o percurso das cidades.
        cidades (list): Lista de coordenadas (x, y) das cidades.

    Returns:
        float: Distância total do percurso.
    """
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
    """
    Gera uma solução candidata trocando duas cidades de posição na solução atual.

    Args:
        solucao (list): Solução atual representada como uma lista de índices.

    Returns:
        list: Nova solução candidata após troca de duas cidades.
    """
    solucao_candidata = solucao[:]
    # Troca duas cidades de lugar aleatoriamente
    a, b = random.sample(range(len(solucao)), 2)
    solucao_candidata[a], solucao_candidata[b] = solucao_candidata[b], solucao_candidata[a]
    return solucao_candidata
    
def escolher_melhor_solucao(solucao, solucao_candidata, cidades):
    """
    Compara duas soluções e retorna a de menor distância.

    Args:
        solucao (list): Solução atual.
        solucao_candidata (list): Nova solução candidata.
        cidades (list): Lista de coordenadas (x, y) das cidades.

    Returns:
        list: A solução com a menor distância total.
    """
    distancia_atual = calcular_distancia(solucao, cidades)
    distancia_candidata = calcular_distancia(solucao_candidata, cidades)
    return solucao_candidata if distancia_candidata < distancia_atual else solucao
    
def calcular_probabilidades(fitness):
    """
    Calcula as probabilidades de escolha de cada solução baseada no fitness.

    Args:
        fitness (list): Lista de distâncias totais (fitness) de cada solução.

    Returns:
        list: Lista de probabilidades normalizadas para cada solução.
    """
    inverso_fitness = [1 / f for f in fitness]
    total = sum(inverso_fitness)
    return [f / total for f in inverso_fitness]

def abcd(cidades, num_abelhas, ciclos, limite):
    """
    Implementa o algoritmo de Colônia de Abelhas (ABC) para o Problema do Caixeiro Viajante (TSP).

    Args:
        cidades (list): Lista de coordenadas (x, y) das cidades.
        num_abelhas (int): Número de abelhas na população.
        ciclos (int): Número de ciclos de execução do algoritmo.
        limite (int): Limite de tentativas antes de uma abelha se tornar escoteira.

    Returns:
        tuple: Melhor solução encontrada e sua distância total.
    """
    populacao = iniciar_populacao(num_abelhas, len(cidades))
    fitness = [calcular_distancia(solucao, cidades) for solucao in populacao]
    tentativas = [0] * num_abelhas
    
    # Escolhe melhor solução inicial
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
                populacao[i] = list(range(len(cidades)))
                random.shuffle(populacao[i])
                fitness[i] = calcular_distancia(populacao[i], cidades)
                tentativas[i] = 0
        
        # Atualizar a melhor solução
        i = fitness.index(min(fitness))
        if fitness[i] < melhor_fitness:
            melhor_solucao = populacao[i]
            melhor_fitness = fitness[i]
        
    return melhor_solucao, melhor_fitness