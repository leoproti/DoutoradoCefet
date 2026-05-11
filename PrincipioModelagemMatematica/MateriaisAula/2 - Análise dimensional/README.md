# Capítulo 2 — Análise Dimensional

**Livro:** *Principles of Mathematical Modeling* (2ª Edição)
**Autor:** Clive L. Dym
**Editora:** Academic Press, Burlington, 2004
**ISBN:** 978-0-12-226551-8

---

## Visão Geral do Capítulo

O Capítulo 2 apresenta a **análise dimensional** como uma poderosa ferramenta de modelagem matemática. A análise dimensional permite reduzir o número de variáveis independentes em um problema físico, identificar grupos adimensionais que governam o fenômeno e formular experimentos de forma mais eficiente. O capítulo é estruturado em torno de dois métodos principais: o **Método Básico** e o **Teorema de Buckingham Pi**.

---

## Conteúdo do Capítulo

### 2.1 Introdução

O capítulo parte de um exemplo motivador: a força de arrasto $F_D$ exercida por um fluido sobre uma lâmina plana depende de diversas variáveis — a velocidade do escoamento $V$, a largura da lâmina $d$, a densidade do fluido $\rho$ e a viscosidade do fluido $\mu$. Sem análise dimensional, seria necessário traçar **9 gráficos distintos, cada um com 3 curvas**, para representar completamente essa dependência. Com a análise dimensional, toda essa informação pode ser condensada em **um único gráfico** de grupos adimensionais.

A ideia central é que as **leis físicas são independentes do sistema de unidades** utilizado. Portanto, as equações que descrevem fenômenos naturais devem ser **dimensionalmente homogêneas** — cada termo deve ter as mesmas dimensões.

---

### 2.2 Método Básico de Análise Dimensional

O Método Básico consiste em:

1. **Identificar as variáveis** relevantes do problema (ex.: $F_D$, $V$, $d$, $\rho$, $\mu$).
2. **Escrever a equação funcional** na forma $f(F_D, V, d, \rho, \mu) = 0$.
3. **Expressar cada variável em termos das dimensões fundamentais** (comprimento $L$, massa $M$, tempo $T$).
4. **Assumir uma forma de lei de potências** para a variável dependente em função das demais.
5. **Igualar os expoentes** das dimensões dos dois lados da equação, resolvendo o sistema linear resultante.
6. **Identificar o(s) grupo(s) adimensional(is)** (números $\Pi$).

**Exemplo — Período do pêndulo:**

As variáveis relevantes são o período $\tau$, o comprimento $l$, a massa $m$ e a aceleração da gravidade $g$. Aplicando o método básico:

$$\tau = C \sqrt{\frac{l}{g}}$$

onde $C$ é uma constante adimensional (experimentalmente, $C = 2\pi$). Notavelmente, a massa $m$ não aparece — o período de um pêndulo não depende de sua massa.

---

### 2.3 Teorema de Buckingham Pi (Π)

O **Teorema de Buckingham Pi** fornece um procedimento sistemático e geral para encontrar todos os grupos adimensionais de um problema.

**Enunciado:** Se um problema físico envolve $n$ variáveis com $k$ dimensões fundamentais independentes, então o problema pode ser descrito por $(n - k)$ grupos adimensionais independentes $\Pi_1, \Pi_2, \ldots, \Pi_{n-k}$.

**Passos do Teorema de Buckingham Pi:**

1. Identificar as $n$ variáveis e listar suas dimensões.
2. Determinar o número $k$ de dimensões fundamentais independentes presentes.
3. Selecionar $k$ **variáveis de repetição** (que, juntas, devem conter todas as $k$ dimensões fundamentais).
4. Construir cada grupo $\Pi_i$ combinando as $k$ variáveis de repetição com uma das $(n - k)$ variáveis restantes, de modo que o grupo resultante seja adimensional.
5. Expressar o resultado na forma $\Pi_1 = f(\Pi_2, \Pi_3, \ldots, \Pi_{n-k})$.

**Exemplo — Pêndulo (formulação revisada):**

Variáveis: $\tau$ (período), $l$ (comprimento), $m$ (massa), $g$ (aceleração gravitacional). Dimensões: $L$, $M$, $T$. Temos $n = 4$, $k = 3$, logo $n - k = 1$ grupo adimensional:

$$\Pi_1 = \frac{\tau^2 g}{l} = \text{constante}$$

que equivale ao resultado obtido pelo método básico.

---

### 2.4 Aplicações

O capítulo apresenta diversas aplicações do método básico e do Teorema de Buckingham Pi:

#### 2.4.1 Força de Arrasto (Drag)

Para uma lâmina plana em um escoamento viscoso, com variáveis $F_D$, $V$, $d$, $\rho$, $\mu$ ($n = 5$, $k = 3$, $n-k = 2$):

$$\frac{F_D}{\rho V^2 d^2} = f\!\left(\frac{\rho V d}{\mu}\right)$$

O segundo grupo adimensional é o **número de Reynolds** $Re = \rho V d / \mu$, fundamental em mecânica dos fluidos.

#### 2.4.2 Problema de Dois Corpos (Gravitação)

Para o período $\tau$ de revolução de dois corpos de massas $m_1$ e $m_2$ separados por uma distância $r$, com a constante gravitacional $G$:

$$\tau^2 = C \frac{r^3}{G(m_1 + m_2)}$$

Esta é essencialmente a **Terceira Lei de Kepler** obtida por análise dimensional.

#### 2.4.3 Misturador

Para o torque $T$ em um misturador com hélice de diâmetro $d$ girando a velocidade angular $\omega$ em um fluido de densidade $\rho$ e viscosidade $\mu$:

$$\frac{T}{\rho \omega^2 d^5} = f\!\left(\frac{\rho \omega d^2}{\mu}\right)$$

#### 2.4.4 Escoamento em Tubos (Lei de Hagen-Poiseuille)

Para o fluxo volumétrico $Q$ em um tubo de diâmetro $d$ com queda de pressão $\Delta p / l$ e viscosidade $\mu$:

$$Q = C \frac{d^4}{\mu} \frac{\Delta p}{l}$$

Esta é a **Lei de Hagen-Poiseuille** (com $C = \pi/128$), válida para escoamento laminar.

#### 2.4.5 Velocidade do Som

A velocidade do som $c$ em um gás depende da pressão $p$ e da densidade $\rho$:

$$c = C \sqrt{\frac{p}{\rho}}$$

#### 2.4.6 Flexibilidade de uma Viga

Para uma viga de seção quadrada $d \times d$ e comprimento $l$, com módulo de elasticidade $E$, a flexibilidade (complacência) $C_{\rm flex}$ satisfaz:

$$C_{\rm flex} E d = F\!\left(\frac{l}{d}\right)$$

Dados experimentais mostram que $F(l/d) \propto (l/d)^3$, o que leva à fórmula clássica de deflexão de viga:

$$\delta = \frac{P l^3}{48 E I}, \quad I = \frac{d^4}{12}$$

---

## Conceitos-Chave

| Conceito | Descrição |
|---|---|
| **Homogeneidade dimensional** | Toda equação física válida deve ser dimensionalmente homogênea |
| **Grupo adimensional (Π)** | Combinação de variáveis sem dimensões, que resume o comportamento físico |
| **Método Básico** | Abordagem por lei de potências para encontrar grupos adimensionais |
| **Teorema de Buckingham Pi** | Procedimento geral: $n$ variáveis, $k$ dimensões → $(n-k)$ grupos |
| **Número de Reynolds** | $Re = \rho V l / \mu$ — razão entre forças inerciais e viscosas |
| **Semelhança dinâmica** | Dois sistemas são dinamicamente similares se seus grupos adimensionais forem iguais |
| **Redução de variáveis** | A análise dimensional reduz o número de parâmetros independentes de $n$ para $n-k$ |

---

## Dimensões Fundamentais Utilizadas

| Símbolo | Dimensão |
|---|---|
| $M$ | Massa |
| $L$ | Comprimento |
| $T$ | Tempo |
| $\Theta$ | Temperatura (quando necessário) |

**Exemplos de dimensões derivadas:**

- Velocidade: $[V] = L T^{-1}$
- Força: $[F] = M L T^{-2}$
- Pressão: $[p] = M L^{-1} T^{-2}$
- Viscosidade dinâmica: $[\mu] = M L^{-1} T^{-1}$
- Densidade: $[\rho] = M L^{-3}$

---

## Problemas do Capítulo (2.1 a 2.23)

Os problemas do capítulo 2 cobrem a aplicação do método básico e do Teorema de Buckingham Pi a uma variedade de contextos físicos e de engenharia:

- **Problemas 2.1–2.6:** Método Básico (força de arrasto, pêndulo, queda livre, problema de dois corpos)
- **Problemas 2.7–2.12:** Teorema de Buckingham Pi (misturador, pêndulo, dois corpos no espaço)
- **Problemas 2.13–2.19:** Aplicações (tensão em corda, velocidade do som, número de Weber, pêndulo viscoso, escoamento em tubo)
- **Problemas 2.20–2.23:** Aplicações avançadas (tubos rugosos, velocidade do som no aço, flexibilidade de viga)

As resoluções detalhadas desses problemas encontram-se em:
`PrincipioModelagemMatematica/Problemas/Problemas2/`

---

## Referências

- DYM, Clive L. *Principles of Mathematical Modeling*. 2. ed. Burlington: Academic Press, 2004. ISBN 978-0-12-226551-8. DOI: [10.1016/B978-012226551-8/50000-4](https://doi.org/10.1016/B978-012226551-8/50000-4)
