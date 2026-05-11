# Prática: Gerador de Random Walk e Monte Carlo

## Objetivo
Assimilar o conceito de caminhadas aleatórias e implementar o método de Monte Carlo para a simulação de um random walk simples em 1+1 dimensões (posição em $x$ e tempo).

## Metodologia
- Implementação de um gerador de números pseudoaleatórios congruencial linear (LCG) para produzir variáveis uniformes em $[0,1)$.
- Conversão das variáveis uniformes em passos binários $+1$ ou $-1$ para construir o random walk em 1D.
- Simulação de pelo menos 10 caminhadas independentes, cada uma com 10000 passos.
- Plotagem conjunta das 10 trajetórias para visualização do comportamento estocástico.
- Cálculo do desvio quadrático médio $\langle R^2 \rangle$ ao longo do tempo para as 10 amostras.
- Ajuste do comportamento observado em escala log-log, buscando uma lei de potência do tipo $\langle R^2 \rangle \propto t^{\alpha}$.
- Teste de hipótese sobre o expoente $\alpha$, verificando se é compatível com o valor teórico $\alpha = 1$ de um random walk simples clássico.
- Verificação do Teorema Central do Limite (TCL) por meio da distribuição dos deslocamentos finais e comparação com uma aproximação normal.

## Resultados concluídos
- As 10 caminhadas mostram oscilações típicas de um passeio aleatório e diferentes trajetórias partindo da origem.
- O desvio quadrático médio $\langle R^2 \rangle$ cresce de maneira aproximadamente linear com o tempo, como esperado para um random walk puro.
- No gráfico log-log de $\log \langle R^2 \rangle$ versus $\log t$, os dados ajustam-se bem a uma reta, indicando uma lei de potência com expoente próximo de 1.
- O teste de hipótese foi realizado considerando a hipótese nula $\alpha = 1$; os resultados são compatíveis com um random walk verdadeiro dentro da incerteza estatística dos dados simulados.
- O Teorema Central do Limite foi verificado pela comparação entre a distribuição empírica dos deslocamentos finais e a curva gaussiana esperada para muitas amostras de 10000 passos.

## Arquivos principais
- `src/gera_tabela_latex_copia_graficos.ipynb`: notebook usado para gerar as simulações, tabelas e gráficos.
- `relatorioCefet/meu-trabalho.pdf`: relatório completo em formato PDF com fundamentação teórica, metodologia, resultados e conclusões.

## Observações
- A prática integra conceitos de geração pseudoaleatória, simulação de Monte Carlo, ajuste de lei de potência e validação estatística de um modelo de random walk.
- A implementação segue a formulação clássica do random walk em 1D e permite estender o estudo para processos com viés, outras dimensões ou diferentes geradores de números aleatórios.
