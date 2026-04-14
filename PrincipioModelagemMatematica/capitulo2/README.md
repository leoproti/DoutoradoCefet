# Capítulo 2: Análise Dimensional

## Resumo Executivo

A **Análise Dimensional** é uma ferramenta poderosa para o modelagem matemática que garante que as equações sejam dimensionalmente consistentes. Este capítulo apresenta métodos para:
- Validar modelos matemáticos antes de realizar cálculos
- Reduzir o número de variáveis em experimentos
- Entender as relações entre grandezas físicas

---

## 1. Conceitos Fundamentais (Seção 2.1-2.2)

### 1.1 Dimensões e Unidades

**Dimensão**: Representação de uma quantidade em termos de grandezas fundamentais (comprimento L, massa M, tempo T).

**Unidade**: Expressão numérica de uma dimensão em relação a um padrão (metros, quilogramas, segundos).

### Exemplo:
```
Velocidade: [V] = L/T
Força: [F] = M·L/T²
Densidade: [ρ] = M/L³
```

### 1.2 Homogeneidade Dimensional

Princípio fundamental: **Todos os termos em uma equação devem ter as mesmas dimensões.**

**Exemplo correto:**
```
Período de pêndulo: T₀ = 2π√(l/g)
- [T₀] = T
- [√(l/g)] = √(L/(L/T²)) = √(T²) = T ✓
```

**Exemplo incorreto:**
```
T₀ = 2π√(l/g) + 5 segundos  ← Inválido! Mistura √(l/g) com constante
```

---

## 2. Por Que Fazer Análise Dimensional? (Seção 2.3)

### Motivação Prática

1. **Redução de Experimentos**: Em lugar de fazer 9 gráficos (3³), podemos fazer 2 dimensionless groups
2. **Validação de Modelos**: Detecta erros antes de computações custosas
3. **Compreensão Física**: Revela quais variáveis são realmente importantes

### Exemplo: Misturador de Manteiga de Amendoim

Para modelar força de arrasto (F_D) ao mexer uma lâmina:
- Sem análise dimensional: 5 variáveis × 3 valores cada = 125 experimentos
- Com análise dimensional: 2 grupos dimensionless = 9 experimentos

---

## 3. Como Fazer Análise Dimensional? (Seção 2.4)

### Método 1: Método Básico

**Passo a passo:**

a) Listar todas as variáveis e parâmetros com suas dimensões
b) Antecipar como cada variável afeta as quantidades de interesse  
c) Identificar uma variável dependente em relação às outras
d) Expressar essa dependência como equação funcional
e) Escolher e eliminar uma dimensão primária
f) Repetir até encontrar equação adimensional
g) Revisar se o comportamento faz sentido

**Exemplo: Velocidade de um Corpo em Queda**

Variáveis: V, g, h

```
[V] = L/T
[g] = L/T²
[h] = L

V = V(g, h)

Dimensões:
L/T = (L/T²)^a · L^b

Resolvendo:
L: 1 = a + b  →  b = 1 - a
T: -1 = -2a   →  a = 1/2

Logo: V ∝ √(gh)  →  V = constant × √(gh)
```

### Método 2: Teorema de Pi de Buckingham

**Enunciado**: Uma equação dimensionalmente homogênea com n variáveis e m dimensões fundamentais pode ser reduzida a (n-m) grupos adimensionais independentes.

**Teorema de Pi**:
```
Π₁ = Φ(Π₂, Π₃, ..., Πₙ₋ₘ)
ou
Φ(Π₁, Π₂, ..., Πₙ₋ₘ) = 0
```

**Formulação Geral**:
```
Πᵢ = A₁^(a₁) · A₂^(a₂) · ... · Aₙ^(aₙ)
```

**Exemplo: Pêndulo Simples**

6 variáveis: l, g, m, T₀, θ, T (tensão da corda)
3 dimensões fundamentais: M, L, T

Logo: 6 - 3 = 3 grupos adimensionais

**Escolher base**: l, g, m

Grupos:
```
Π₁ = T₀/√(l/g)
Π₂ = θ  (adimensional)
Π₃ = T/(mg)
```

---

## 4. Sistemas de Unidades (Seção 2.5)

### Sistema Britânico vs SI

| Grandeza | Sistema Britânico | SI (Sistema Internacional) |
|----------|------------------|--------------------------|
| Comprimento | pé (ft) | metro (m) |
| Massa | slug | quilograma (kg) |
| Tempo | segundo (s) | segundo (s) |
| Força | libra-força (lbf) | newton (N) |

### Conversão de Unidades

```
65 mi/hr × (5280 ft/mi) × (1 hr/3600 s) × (0.3048 m/ft) = 29.06 m/s
```

### Prefixos SI Comuns

| Fator | Prefixo | Símbolo |
|-------|---------|---------|
| 10⁻³ | mili | m |
| 10⁻⁶ | micro | μ |
| 10³ | quilo | k |
| 10⁶ | mega | M |
| 10⁹ | giga | G |

---

## 5. Exemplos Resolvidos

### Exemplo 1: Período do Pêndulo

**Dado**: O período depende de l (comprimento) e g (aceleração da gravidade)

**Solução usando Método Básico**:
```
T₀ = T₀(l, g)

[T₀] = T
[l] = L
[g] = L/T²

T = (L)^a · (L/T²)^b
T = L^(a+b) · T^(-2b)

Exponentes:
L: 0 = a + b  →  a = -b
T: 1 = -2b   →  b = -1/2

Logo: T₀ = constant × √(l/g)
Fisicamente: T₀ = 2π√(l/g)  ✓
```

### Exemplo 2: Velocidade do Som

**Dado**: Velocidade c depende de pressão p e densidade ρ

**Solução**:
```
c = c(p, ρ)

[c] = L/T
[p] = M/(L·T²)
[ρ] = M/L³

L/T = [M/(L·T²)]^a · [M/L³]^b
L/T = M^(a+b) · L^(-a-3b) · T^(-2a)

Resolvendo:
M: 0 = a + b
L: 1 = -a - 3b
T: -1 = -2a

De T: a = 1/2
De M: b = -1/2

Logo: c ∝ √(p/ρ)
```

---

## 6. Implementação em Python

Ver arquivo `dimensional_analysis.py` para classes e funções reutilizáveis.

Ver arquivo `examples.py` para exemplos práticos executáveis.

---

## 7. Checklist de Aplicação

Ao aplicar análise dimensional:

- [ ] Listar todas as variáveis e suas dimensões
- [ ] Identificar quantas dimensões fundamentais existem
- [ ] Escolher variáveis base (contendo todas as dimensões)
- [ ] Formar grupos dimensionless permutando variáveis restantes
- [ ] Verificar se cada grupo é realmente adimensional
- [ ] Validar que o resultado físico faz sentido
- [ ] Documentar as suposições feitas

---

## Referências

Dym, C. L. (2004). *Principles of Mathematical Modeling*. 2nd Edition. Academic Press.

Langhaar, H. L. (1951). *Dimensional Analysis and Theory of Models*. John Wiley.

Taylor, E. S. (1974). *Dimensional Analysis for Engineers*. Oxford University Press.
