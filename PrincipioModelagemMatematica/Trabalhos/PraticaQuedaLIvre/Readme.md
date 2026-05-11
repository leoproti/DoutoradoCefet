objetivo:

Implementar computacionalmente um modelo de queda livre.
## Objetivo

Implementar computacionalmente um modelo de queda livre.

## Roteiro

1. A partir do apresentado em sala de aula, implemente computacionalmente um modelo para calcular o movimento de queda livre de uma partícula nas imediações da Terra, dada a altura inicial H e velocidade v0.

2. Apresente os gráficos para a posição, velocidade e aceleração da partícula em função do tempo.

3. Discuta as implicações e possíveis alterações na modelagem se fosse considerado um corpo rígido em queda livre nas mesmas condições.

4. Implemente a resistência do ar (**2 pontos extras**).

5. Estude a acurácia do resultado em função do tamanho do passo de tempo (**2 pontos extras**).

**Valor:** 3 pts

## Formato de entrega

- Arquivo devidamente identificado em formato **PDF**.

# Modelo Computacional de Queda Livre


## Repositório
O código-fonte completo deste projeto está disponível em: [https://github.com/LeonardoVieiraGuimaraes/DoutoradoCefet/tree/main/PrincipioModelagemMatematica/PraticaQuedaLIvre](https://github.com/LeonardoVieiraGuimaraes/DoutoradoCefet/tree/main/PrincipioModelagemMatematica/PraticaQuedaLIvre)

Este projeto implementa, em Python, um modelo computacional para simular a queda livre de um objeto, conforme roteiro detalhado da disciplina de Princípios de Modelagem Matemática.

## Objetivo
Transformar a teoria da queda livre em um programa real, utilizando o método de Euler para simulação passo a passo, e analisar os limites do modelo.

## Roteiro e Funcionalidades
1. **Implementação Básica:**
	- Simulação da queda livre usando laço de repetição (método de Euler), calculando posição e velocidade até o objeto atingir o solo.
2. **Gráficos:**
	- Geração dos gráficos de posição x tempo, velocidade x tempo e aceleração x tempo.
3. **Discussão Teórica:**
	- Análise das suposições do modelo (partícula vs. corpo rígido).
4. **Resistência do Ar (Bônus):**
	- Implementação opcional da resistência do ar proporcional à velocidade.
5. **Estudo do Passo de Tempo (Bônus):**
	- Comparação da precisão do modelo variando o tamanho do passo de tempo ($\Delta t$).

## Como Executar
1. Abra o arquivo `src/QuedaLivre.ipynb` no Jupyter Notebook ou Google Colab.
2. Execute as células em ordem. Os gráficos serão gerados automaticamente.
3. Modifique os parâmetros (altura, velocidade inicial, gravidade, passo de tempo) para explorar diferentes cenários.

## Exemplos de Gráficos Gerados
Os principais gráficos produzidos são:
- **Posição x Tempo:** Mostra a trajetória da queda até o solo.
- **Velocidade x Tempo:** Mostra a aceleração constante (ou com resistência do ar, a velocidade terminal).
- **Aceleração x Tempo:** Linha constante igual à gravidade (ou variável, se houver resistência do ar).

## Estrutura do Código
- O notebook está dividido em seções:
  1. Importação de bibliotecas
  2. Definição dos parâmetros e funções
  3. Implementação do modelo discreto (método de Euler)
  4. Geração dos gráficos
  5. Discussão teórica e análise de precisão

## Entrega
- Gere um PDF do notebook com os gráficos e respostas teóricas para submissão.

---
**Autor:** [Seu Nome]
**Disciplina:** Princípios de Modelagem Matemática