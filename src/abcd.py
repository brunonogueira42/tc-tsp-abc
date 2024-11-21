
def iniciar_populacao(abelhas, num_cidades):
    print("iniciar_populacao") # gerar soluções aleatórias
    
def calcular_distancia(solucao, cidades):
    print("calcular_distancia")
    
def gerar_solucao_candidata(solucao):
    print("gerar_solucao_candidata") # utilizar equação de modificação?
    
def escolher_melhor_solucao(solucao, solucao_candidata):
    print("escolher_melhor_solucao")
    
def calcular_probabilidades(fitness):
    print("calcular_probabilidade")

def abc(cidades, abelhas, ciclos, limite):
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
