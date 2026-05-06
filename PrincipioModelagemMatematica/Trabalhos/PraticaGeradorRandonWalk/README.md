# Prática: Gerador de Random Walk e Monte Carlo

## Objetivo

Assimilar o conceito de caminhadas aleatórias e implementar o método de Monte Carlo.

## Roteiro

### 1. Gerador congruencial e simulação do Random Walk em 1+1 dimensões

Utilizando o gerador de números aleatórios congruencial, crie um algoritmo para simular o random walk em 1 + 1 dimensões (posição x e tempo).

- Implemente o **Gerador Linear Congruencial (LCG)** pela recorrência:
  `x_{n+1} = (a * x_n + c) mod m`
  com parâmetros que satisfaçam as condições de Hull-Dobell para período máximo (ex: `a=1664525`, `c=1013904223`, `m=2^32`).
- Normalize os valores gerados para o intervalo [0, 1): `u_n = x_n / m`.
- Converta cada número uniforme em um passo do caminhante:
  - se `u_n < 0.5` → passo `+1` (direita)
  - se `u_n >= 0.5` → passo `-1` (esquerda)
- Acumule os passos para obter a posição `x(t) = sum dos passos até o instante t`.

---

### 2. Execução de 10 caminhadas e gráfico conjunto

Execute pelo menos 10 caminhadas com pelo menos 10000 passos cada uma, e exiba um gráfico com as 10 caminhadas juntas.

- Para cada caminhada `i = 1, ..., 10`, use uma semente diferente para o LCG (ex: `seed_i = i * 12345`).
- Gere `N = 10000` passos por caminhada, armazenando a trajetória completa `x_i(t)` para `t = 0, 1, ..., N`.
- Plote todas as 10 trajetórias no mesmo gráfico:
  - Eixo horizontal: tempo `t` (número de passos)
  - Eixo vertical: posição `x(t)`
  - Use cores distintas para cada caminhada.

---

### 3. Desvio quadrático médio e ajuste log-log

Calcule o desvio quadrático médio (`<R^2>`) para as 10 amostras e represente graficamente em escala log-log — log `<R^2>` x log `t`. Ajuste a curva encontrada com uma lei de potência (alométrica).

- Para cada instante `t`, calcule:
  `<R^2>(t) = (1/10) * sum_{i=1}^{10} x_i(t)^2`
- Plote `log(<R^2>)` no eixo y versus `log(t)` no eixo x (escala log-log).
- Realize uma **regressão linear** sobre os dados transformados:
  `log(<R^2>) = alpha * log(t) + log(C)`
  para obter o expoente `alpha` e a constante `C`.
- Sobreponha a reta ajustada ao gráfico e exiba os valores de `alpha` e `C`.
- O valor teórico esperado para random walk clássico é `alpha = 1` (`<R^2> ~ t`).

---

### 4. Teste de hipótese sobre o expoente da lei de potência

Faça um teste de hipóteses com o valor obtido para o expoente da lei de potência e verifique a hipótese de que o caminhante execute um verdadeiro random walk (expoente igual a 1).

- Formule as hipóteses:
  - **H₀** (hipótese nula): `alpha = 1` (random walk verdadeiro)
  - **H₁** (hipótese alternativa): `alpha ≠ 1`
- Estime o erro padrão do expoente a partir da regressão linear (use a matriz de covariância do ajuste por mínimos quadrados).
- Calcule a estatística de teste:
  `t_stat = (alpha_estimado - 1) / erro_padrao`
- Compare com o valor crítico da distribuição t de Student com `n - 2` graus de liberdade (onde `n` é o número de pontos usados no ajuste).
- Conclua: se `|t_stat| < t_critico` para `alpha = 0.05`, não rejeite H₀ — o dado é compatível com random walk verdadeiro.

---

### 5. Verificação do Teorema Central do Limite

Verifique o Teorema Central do Limite para a simulação realizada.

- Realize um grande número de caminhadas independentes (ex: 1000 ou mais), cada uma com `N = 10000` passos.
- Colete os deslocamentos finais `x_i(N)` de cada caminhada.
- O TCL prevê que, para `N` grande:
  `x(N) / sqrt(N) → N(0, 1)`
  ou seja, `x(N) ~ N(0, N)` com média 0 e variância `N`.
- Plote o histograma normalizado dos deslocamentos finais.
- Sobreponha a curva gaussiana teórica `N(0, N)`.
- Compare visualmente e, opcionalmente, aplique um teste de normalidade (ex: Shapiro-Wilk ou Kolmogorov-Smirnov) para confirmar a convergência.
