# Problema do Caixeiro Viajante (TSP) + Colônia de Abelhas (ABC)

O Algoritmo Colônia de Abelhas (ABC) é utilizado para resolver o Problema do Caixeiro Viajante (TSP). O objetivo é encontrar o menor caminho para visitar todas as cidades e retornar à cidade inicial.

## Requisitos

- Python: versão 3.12.6 ou superior.
- Bibliotecas `math` e `random` (nativas do Python).
- Biblioteca `matplotlib`.

## Estrutura do Projeto

- `abcd.py`: Implementação do Algoritmo Colônia de Abelhas (ABC).
- `grafico.py`: Função para exibir o gráfico do percurso da melhor solução encontrada.
- `main.py`: Script principal para executar o algoritmo e exibir os resultados.

## Como Executar o Código

1. Certifique-se de que você possui Python 3.12.6 ou superior instalado.

2. Instale a biblioteca `matplotlib` se ainda não estiver instalada:

```bash
pip install matplotlib
```

3. No terminal ou prompt de comando, navegue até o diretório onde os arquivos estão salvos (`/src`).

4. Execute o seguinte comando para iniciar o programa:

```bash
python main.py
```

## Parâmetros

No arquivo `main.py`, é possível configurar os seguintes parâmetros:

- Número de cidades: `num_cidades`
- Número de abelhas na população: `num_abelhas`
- Número de ciclos: `ciclos`
- Limite de tentativas antes de uma abelha se tornar escoteira: `limite`

## Exemplo de Saída

Após a execução do programa, a saída será semelhante à seguinte:

```bash
Coordenadas das cidades:
Cidade 0: (60, 23)
Cidade 1: (93, 74)
Cidade 2: (38, 25)
Cidade 3: (92, 52)
Cidade 4: (96, 91)
Cidade 5: (97, 33)
Cidade 6: (68, 31)
Cidade 7: (81, 94)
Cidade 8: (63, 45)
Cidade 9: (53, 67)

Melhor solução encontrada:
Ordem das cidades: [9, 7, 4, 1, 3, 5, 6, 0, 2, 8]
Distância total: 231.78
```
