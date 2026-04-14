# Exercícios Propostos - Capítulo 2: Análise Dimensional

## Nível 1: Básico

### Exercício 1.1: Velocidade do Som

**Problema**: A velocidade do som em um gás, $c$, depende da:
- Pressão do gás: $p$ [M/(L·T²)]
- Densidade do gás: $ρ$ [M/L³]

Usando análise dimensional, determine como $c$ depende de $p$ e $ρ$.

**Solução**:
```
c = c(p, ρ)
[c] = L/T
[p] = M/(L·T²)
[ρ] = M/L³

c = C · p^a · ρ^b
L/T = [M/(L·T²)]^a · [M/L³]^b
L/T = M^(a+b) · L^(-a-3b) · T^(-2a)

Igualando expoentes:
M: 0 = a + b         →  b = -a
L: 1 = -a - 3b = -a + 3a = 2a  →  a = 1/2
T: -1 = -2a         →  a = 1/2 ✓

Resultado: c = C · √(p/ρ)
Fisicamente: c = √(γp/ρ) onde γ é o índice adiabático
```

### Exercício 1.2: Período de Oscilação

**Problema**: Um objeto oscila devido a uma mola com constante $k$. Seu período $T$ depende de:
- Massa: $m$ [M]
- Constante da mola: $k$ [M/T²]

Encontre como $T$ depende de $m$ e $k$.

**Solução**:
```
T = T(m, k)
[T] = T
[m] = M
[k] = M/T²

T = C · m^a · k^b
T = (M)^a · (M/T²)^b
T = M^(a+b) · T^(-2b)

Igualando:
M: 0 = a + b       →  a = -b
T: 1 = -2b         →  b = -1/2, a = 1/2

Resultado: T = C · √(m/k)
Fisicamente: T = 2π√(m/k)
```

---

## Nível 2: Intermediário

### Exercício 2.1: Força em Condutor Elétrico

**Problema**: A força $F$ em um condutor imerso em um campo magnético depende de:
- Comprimento do condutor: $L$ [L]
- Intensidade de corrente: $I$ [A] (dimensão fundamental própria)
- Força do campo magnético: $B$ [M/(A·T²)]

Determine a relação entre $F$, $L$, $I$ e $B$.

**Solução**:
```
Usando análise dimensional:
[F] = M·L/T²
[L] = L
[I] = A
[B] = M/(A·T²)

F = C · L^a · I^b · B^c
M·L/T² = L^a · A^b · [M/(A·T²)]^c

Igualando expoentes:
M: 1 = c
A: 0 = b - c  →  b = c = 1
L: 1 = a      →  a = 1
T: -2 = -2c   →  c = 1 ✓

Resultado: F = C · L·I·B
Fisicamente: F = B·I·L (Lei de Ampère-Lorentz)
```

### Exercício 2.2: Fluido em Tubo

**Problema**: O fluxo volumétrico $Q$ através de um tubo depende de:
- Diâmetro do tubo: $d$ [L]
- Queda de pressão por unidade de comprimento: $∇P$ [M/(L²·T²)]
- Viscosidade do fluido: $μ$ [M/(L·T)]

Use o Teorema de Buckingham Pi para encontrar a relação.

**Solução**:
```
Variáveis: n = 4 (Q, d, ∇P, μ)
Dimensões fundamentais: m = 3 (M, L, T)
Grupos dimensionless: n - m = 1

Matriz de dimensões:
        Q    d    ∇P   μ
L:      3    1   -2    -1
M:      0    0    1     1
T:     -1    0   -2    -1

Escolher base: d, ∇P, μ
Grupo dimensionless:

Π = Q · d^a · (∇P)^b · μ^c

Para que seja adimensional:
L: 3 + a - 2b - c = 0
M: 0 + b + c = 0   →  c = -b
T: -1 - 2b - c = 0  →  -1 - 2b + b = 0  →  b = -1, c = 1

Logo: 3 + a + 2 + 1 = 0  →  a = -4

Π = Q/(d^4 · ∇P/μ) = constant

Resultado: Q = C · d⁴ · (∇P)/μ
Lei de Hagen-Poiseuille: Q = (π/128) · d⁴ · (∇P)/μ
```

---

## Nível 3: Avançado

### Exercício 3.1: Resistência do Ar em Queda

**Problema**: Um objeto em queda sofre resistência do ar que depende de:
- Velocidade: $V$ [L/T]
- Densidade do ar: $ρ$ [M/L³]
- Área de seção transversal: $A$ [L²]
- Coeficiente de forma: $C_D$ [adimensional]

Encontre a força de arrasto $F_D$.

**Solução**:
```
Variáveis: n = 5 (F_D, V, ρ, A, C_D)
Dimensões: m = 3
Grupos: n - m = 2

F_D = F_D(V, ρ, A, C_D)
[F_D] = M·L/T²
[V] = L/T
[ρ] = M/L³
[A] = L²
[C_D] = 1

Grupo 1 (adimensional óbvio):
Π₁ = C_D

Grupo 2 (contém F_D):
Π₂ = F_D/(ρ·V²·A)

Relação funcional:
F_D/(ρ·V²·A) = f(C_D)

Se f(C_D) = C_D:
F_D = (1/2)·ρ·V²·A·C_D

Resultado: Equação clássica da força de arrasto
```

### Exercício 3.2: Transferência de Calor

**Problema**: A taxa de transferência de calor $Q̇$ através de uma parede depende de:
- Área da parede: $A$ [L²]
- Diferença de temperatura: $ΔT$ [Θ]
- Espessura da parede: $x$ [L]
- Condutividade térmica: $k$ [M·L/(T³·Θ)]

Encontre a relação usando análise dimensional.

**Solução**:
```
[Q̇] = M·L²/T³ (poder/energia por tempo)
[A] = L²
[ΔT] = Θ
[x] = L
[k] = M·L/(T³·Θ)

Q̇ = C · A^a · (ΔT)^b · x^c · k^d
M·L²/T³ = (L²)^a · (Θ)^b · (L)^c · [M·L/(T³·Θ)]^d

Igualando:
M: 1 = d
L: 2 = 2a + c + d   →  2 = 2a + c + 1  →  c = 1 - 2a
Θ: 0 = b - d = b - 1  →  b = 1
T: -3 = -3d = -3  ✓

Escolhendo a = 1:
c = 1 - 2 = -1

Resultado: Q̇ = C · A · ΔT · k/x
Lei de Fourier: Q̇ = k·A·ΔT/x
```

---

## Exercícios para Resolver

### E1: Força Centrípeta

A força centrípeta necessária para manter um objeto em movimento circular depende de:
- Massa: $m$ [M]
- Velocidade: $v$ [L/T]
- Raio da trajetória: $r$ [L]

Encontre como $F_c$ depende dessas variáveis.

**Resposta esperada**: $F_c = m v^2 / r$

---

### E2: Frequência de Vibração

A frequência natural de vibração $f$ de uma viga cantilever depende de:
- Comprimento: $L$ [L]
- Módulo de elasticidade: $E$ [M/(L·T²)]
- Densidade: $ρ$ [M/L³]

Determine a relação funcional.

**Resposta esperada**: $f ∝ (1/L²)·\sqrt{E/ρ}$

---

### E3: Projeto de Aerofólio

A força de sustentação $F_L$ de um aerofólio depende de:
- Velocidade do ar: $V$ [L/T]
- Densidade do ar: $ρ$ [M/L³]
- Área do aerofólio: $A$ [L²]
- Ângulo de ataque: $α$ [adimensional]

Usando Buckingham Pi, encontre a relação.

**Resposta esperada**: $F_L = \frac{1}{2}ρ V^2 A C_L(α)$

---

## Checklist de Resolução

Ao resolver exercícios de análise dimensional:

- [ ] Listar todas as variáveis com suas dimensões
- [ ] Contar número de variáveis (n) e dimensões (m)
- [ ] Calcular número de grupos dimensionless (n - m)
- [ ] Aplicar Método Básico OU Teorema de Buckingham Pi
- [ ] Verificar que cada grupo é realmente adimensional
- [ ] Validar resultado com conhecimento físico
- [ ] Comparar com fórmulas conhecidas

---

## Gabarito Resumido

| Exercício | Resultado |
|-----------|-----------|
| 1.1 | $c = C\sqrt{p/ρ}$ |
| 1.2 | $T = C\sqrt{m/k}$ |
| 2.1 | $F = BIL$ |
| 2.2 | $Q = C·d^4·∇P/μ$ |
| 3.1 | $F_D = \frac{1}{2}ρV^2AC_D$ |
| 3.2 | $\dot{Q} = kAΔT/x$ |
| E1 | $F_c = mv^2/r$ |
| E2 | $f ∝ (1/L^2)\sqrt{E/ρ}$ |
| E3 | $F_L = \frac{1}{2}ρV^2AC_L$ |

---

## Dicas Importantes

1. **Sempre verificar dimensões**: Mesmo que a álgebra esteja correta
2. **Usar constantes físicas quando disponível**: $g = 9.81$ m/s², $π = 3.14159$
3. **Considerar simetrias**: Algumas variáveis podem ser eliminadas por simetria
4. **Validar com casos limites**: Ex: Quando $μ → 0$, o que acontece?
5. **Comparar com literatura**: Fórmulas conhecidas confirmam a análise

---

## Referências

- Dym, C. L. (2004). Principles of Mathematical Modeling. Cap. 2.
- Buckingham, E. (1914). On Physically Similar Systems. Physical Review.
- Taylor, E. S. (1974). Dimensional Analysis for Engineers.
