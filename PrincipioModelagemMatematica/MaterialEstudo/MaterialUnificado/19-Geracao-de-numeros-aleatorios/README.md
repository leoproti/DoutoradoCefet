# Unidade 19 — Geração de Números Aleatórios

## Objetivo

Compreender como computadores geram números pseudo-aleatórios, estudar os principais algoritmos (LCG, Mersenne Twister, PCG64), métodos de transformação de distribuições e critérios de qualidade de um gerador. Aplicar ao Random Walk e à Deposição Aleatória.

---

## Conteúdo principal

### 1. Motivação
- Simulações de Monte Carlo, modelos estocásticos, Random Walk, deposição aleatória, criptografia.
- Números **verdadeiramente aleatórios** (fenômenos físicos) vs. **pseudo-aleatórios** (PRNG, determinísticos, dependem de semente).

### 2. Geradores Congruenciais Lineares (LCG)
- Recorrência: $X_{n+1} = (a X_n + c) \bmod m$; número uniforme: $U_n = X_n / m$.
- Variantes: multiplicativo ($c=0$), misto ($c \neq 0$).
- **Condições de Hull-Dobell** para período máximo $m$.
- Parâmetros dos slides CEFET: $A = 843314861$, $B = 453816693$, $M = 2^{30}$.
- **Limitações:** estrutura de grade, período curto, correlações nos bits menos significativos.

### 3. Geradores Modernos
- **Mersenne Twister (MT19937):** período $2^{19937}-1$; padrão histórico em Python/MATLAB.
- **PCG64:** LCG 128 bits + permutação; padrão atual do NumPy (`np.random.default_rng()`).
- **CSPRNGs:** ChaCha20, AES-CTR — para segurança criptográfica (`secrets` no Python).

### 4. Distribuição Gaussiana e TCL
- $f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$; FWHM $\approx 2{,}355\,\sigma$.
- **Teorema Central do Limite:** soma de $n$ v.a.\ i.i.d.\ converge para $\mathcal{N}(n\mu, n\sigma^2)$.

### 5. Random Walk (Caminhada Aleatória)
- $S_n = \sum_{i=1}^n X_i$, $X_i \in \{-1, +1\}$ com $p = 1/2$.
- Probabilidade teórica: $P_N(d) = \frac{1}{2^N}\binom{N}{(N+d)/2}$ (válida se $N+d$ par, $|d| \leq N$).
- Triângulo de Pascal: distribuição de probabilidades por número de passos.
- Propriedades: $\langle S_N \rangle = 0$, $\langle S_N^2 \rangle = N$, $\sigma_N = \sqrt{N}$.
- Movimento Browniano: limite contínuo do RW, $B(t) - B(s) \sim \mathcal{N}(0, t-s)$.

### 6. Deposição Aleatória
- **DA pura:** $w(L,t) \sim t^{1/2}$ (rugosidade cresce indefinidamente).
- **DARS / Edwards-Wilkinson:** $w(L,\infty) \sim L^{1/2}$; expoentes $\alpha=1/2$, $\beta_w=1/4$, $z=2$.
- **Lei de Family-Vicsek:** $w(L,t) \sim L^\alpha f(t/L^z)$; $z = \alpha/\beta_w$.
- **Expoente de Hurst:** $H = d - D$ (dimensão fractal de perfis auto-afins).

### 7. Transformação de Distribuições
- **Transformada Inversa:** $X = F^{-1}(U)$ — Exponencial: $X = -\ln(1-U)/\lambda$.
- **Box-Muller:** $Z = \sqrt{-2\ln U_1}\cos(2\pi U_2) \sim \mathcal{N}(0,1)$.
- **Método de Rejeição:** amostrar $f(x)$ via envelope $g(x)$.

### 8. Testes de Qualidade
- **Teste $\chi^2$:** uniformidade ($\chi^2 = \sum(O-E)^2/E$).
- **Kolmogorov-Smirnov:** $D_n = \sup|F_n(x) - F(x)|$.
- **Teste espectral:** estrutura de grade em dimensões múltiplas.
- **TestU01 BigCrush:** bateria moderna com 254 testes; PCG64 passa, LCG simples falha.

---

## Fórmulas-chave

| Conceito | Fórmula |
|---|---|
| LCG | $X_{n+1} = (aX_n + c) \bmod m$ |
| Transformada inversa | $X = F^{-1}(U)$ |
| Box-Muller | $Z = \sqrt{-2\ln U_1}\cos(2\pi U_2)$ |
| $P_N(d)$ do RW | $\binom{N}{(N+d)/2} / 2^N$ |
| Desvio padrão do RW | $\sigma_N = \sqrt{N}$ |
| Rugosidade DA | $w \sim t^{1/2}$ |
| Family-Vicsek | $z = \alpha / \beta_w$ |
| Teste $\chi^2$ | $\sum(O-E)^2/E \sim \chi^2(k-1)$ |

---

## Resumo rápido

- Computadores geram sequências **pseudo-aleatórias** — deterministicamente, via semente.
- **LCG** é simples e rápido, mas tem período curto e estrutura de grade.
- **PCG64** (NumPy moderno) e **MT19937** são os padrões práticos para ciência.
- Para converter $U \sim \mathcal{U}(0,1)$ em outra distribuição: **Transformada Inversa** ou **Box-Muller**.
- O **Random Walk** em 1D tem $P_N(d)$ exata via binomial e converge para Gaussiana pelo TCL.
- A **Deposição Aleatória** conecta PRNG à física de superfícies rugosas e fractais.

---

## Exercícios sugeridos

1. Gere 15 termos do LCG com $a=7$, $c=0$, $m=10$, $X_0=3$. Qual o período?
2. Aplique as condições de Hull-Dobell para $a=5$, $c=1$, $m=8$.
3. Use Box-Muller com $U_1=0{,}3$ e $U_2=0{,}7$ para gerar $Z_1$ e $Z_2$.
4. Calcule $P_6(0)$ e $P_6(2)$ pela fórmula teórica. Confirme no triângulo de Pascal.
5. Para $N=10^4$, estime a probabilidade gaussiana de $|S_N| > 300$.
6. Realize o teste $\chi^2$ para contagens $\{5,15,8,12,10,7,13,11,9,10\}$ em 10 bins com 100 amostras.
7. Explique por que a densidade gaussiana deve ser multiplicada por 2 ao comparar com $P_N(d)$.
8. Quando usar `secrets` em vez de `np.random` no Python?

---

## Referências

- **Knuth, D. E.** *The Art of Computer Programming*, Vol. 2. Addison-Wesley, 1998.
- **L'Ecuyer, P.** *Handbook of Simulation*. Wiley, 1998.
- **Matsumoto & Nishimura.** Mersenne Twister. *ACM TOMACS*, 8(1), 1998.
- **O'Neill, M. E.** PCG: A Family of Simple Fast RNG Algorithms. HMC, 2014.
- **Faria, A. A. P.** Aspectos Fractais em Sistemas Complexos. Tese UFMG, 2002.
- **Family & Vicsek.** *J. Phys. A*, 18, L75, 1985. (Lei de escala FV)
- **Edwards & Wilkinson.** *Proc. R. Soc. Lond. A*, 381, 1982. (Equação EW)
- Wikipedia: [Random number generation](https://en.wikipedia.org/wiki/Random_number_generation)
- Wikipedia: [Random walk](https://en.wikipedia.org/wiki/Random_walk)
- Slides da disciplina: `pmmat_aula07.pdf` e `numerosaleatorios.pdf`

