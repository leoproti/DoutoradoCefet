# Capítulo 2: Análise Dimensional 📚

## Índice de Conteúdo

### 📖 Arquivos Principais

1. **README.md** - Guia completo do capítulo
   - Resumo executivo
   - Conceitos fundamentais (Dimensões e Unidades)
   - Homogeneidade Dimensional
   - Motivação para Análise Dimensional
   - Métodos (Básico e Buckingham Pi)
   - Sistemas de Unidades
   - Exemplos resolvidos
   - Checklist de aplicação

2. **EXERCICIOS.md** - Lista completa de exercícios
   - 9 exercícios resolvidos (3 níveis de dificuldade)
   - 3 exercícios para resolver
   - Gabarito resumido
   - Dicas importantes

3. **dimensional_analysis.py** - Implementação em Python
   - Classe `Dimension` para manipular dimensões
   - Classe `DimensionalAnalysis` para análise
   - Exemplos de código

4. **examples.py** - 5 exemplos práticos completos
   - Período do pêndulo
   - Queda de corpos
   - Misturador de amendoim
   - Número de Reynolds
   - Conversão de unidades

---

## 🎯 Guia Rápido de Uso

### Para Aprender a Teoria
1. Leia **README.md** na sequência (2-3 horas)
2. Focando em:
   - Seção 1: Conceitos fundamentais
   - Seção 2: Métodos de resolução
   - Seção 3: Exemplos resolvidos

### Para Praticar
1. Resolva os exercícios em **EXERCICIOS.md**
2. Comece com Nível 1 (Básico)
3. Progresse para Nível 2 e 3
4. Confira soluções no gabarito

### Para Implementar
1. Estude as classes em **dimensional_analysis.py**
2. Execute **examples.py** para ver aplicações práticas
3. Adapte o código para seus problemas

---

## 🔑 Conceitos-Chave

### 1. Definição
**Análise Dimensional**: Método para validar modelos matemáticos e reduzir variáveis em experimentos usando a consistência dimensional das equações.

### 2. Princípio Fundamental
> "Todos os termos em uma equação devem ter as mesmas dimensões"

### 3. Dois Métodos Principais

#### Método Básico
- Informal e intuitivo
- Bom para problemas simples
- Passo a passo:
  1. Listar variáveis
  2. Antecipar efeitos
  3. Formar equação funcional
  4. Eliminar dimensões
  5. Revisar resultado

#### Teorema de Buckingham Pi
- Formal e sistemático
- Para problemas complexos
- Resultado: (n - m) grupos adimensionless
  - n = número de variáveis
  - m = número de dimensões fundamentais

### 4. Benefícios
✓ Reduz drasticamente experimentos necessários  
✓ Detecta erros de modelagem  
✓ Organiza conhecimento de forma clara  
✓ Encontra relações entre variáveis  

---

## 📊 Exemplos Inclusos

### Exemplo 1: Pêndulo Simples
```
Problema: T₀ = f(l, g, m)
Análise: T₀ = 2π√(l/g)  [m é irrelevante!]
Lição: Nem todas as variáveis afetam o resultado
```

### Exemplo 2: Queda de Corpo
```
Problema: V = f(g, h, m)
Análise: V = √(2gh)  [velocidade independente de m]
Lição: Galileu estava certo!
```

### Exemplo 3: Misturador
```
Problema: 5 variáveis para 243 experimentos
Análise: 2 grupos dimensionless para 9 experimentos
Lição: Redução drástica de trabalho experimental
```

### Exemplo 4: Reynolds
```
Usar: Re = ρVl/μ
Aplicar: Classificar regimes de fluxo
Importância: Número adimensional mais importante em mecânica dos fluidos
```

### Exemplo 5: Conversão
```
Atenção: NASA perdeu $327.6 milhões por erro de unidades!
Lição: Conversão correta é CRÍTICA
```

---

## 🧮 Dimensões Fundamentais

| Grandeza | Símbolo | Exemplo |
|----------|---------|---------|
| Comprimento | L | metro (m) |
| Massa | M | quilograma (kg) |
| Tempo | T | segundo (s) |
| Temperatura | Θ | kelvin (K) |
| Corrente | A | ampère (A) |

### Dimensões Derivadas

| Quantidade | Símbolo | Dimensão |
|-----------|---------|----------|
| Velocidade | v | L/T |
| Aceleração | a | L/T² |
| Força | F | M·L/T² |
| Energia | E | M·L²/T² |
| Potência | P | M·L²/T³ |
| Pressão | p | M/(L·T²) |
| Viscosidade | μ | M/(L·T) |

---

## 📐 Algoritmo Geral

```
ENTRADA: Lista de variáveis e dimensões
PROCESSO:
  1. Construir matriz de dimensões
  2. Encontrar rank da matriz (= m)
  3. Calcular n - m grupos dimensionless
  4. Escolher base de m variáveis
  5. Construir grupos permutando variáveis restantes
  6. Resolver sistema linear para expoentes
SAÍDA: Grupos dimensionless e relações entre variáveis
```

---

## 🛠️ Como Executar os Códigos

### Pré-requisitos
```bash
pip install numpy matplotlib
```

### Executar análise dimensional
```bash
python dimensional_analysis.py
```

### Executar exemplos práticos
```bash
python examples.py
```

### Saída esperada
- Matriz de dimensões
- Grupos dimensionless identificados
- Valores numéricos calculados
- Gráficos (se aplicável)

---

## 📝 Checklist de Aprendizado

Após estudar este capítulo, você deve ser capaz de:

- [ ] Explicar o princípio de homogeneidade dimensional
- [ ] Identificar dimensões de qualquer quantidade física
- [ ] Aplicar o Método Básico em problemas simples
- [ ] Usar o Teorema de Buckingham Pi em problemas complexos
- [ ] Calcular grupos dimensionless corretamente
- [ ] Validar resultados com conhecimento físico
- [ ] Converter entre sistemas de unidades
- [ ] Implementar análise dimensional em código
- [ ] Resolver todos os exercícios propostos

---

## 🔗 Relação com Outros Tópicos

**Capítulo 1**: Modelagem matemática (motivação geral)  
↓  
**Capítulo 2**: Análise dimensional (validação de modelos) ⬅️ VOCÊ ESTÁ AQUI  
↓  
**Capítulo 3**: Escala (abstração e proporção)  
↓  
**Capítulos 4+**: Aplicações específicas (pêndulo, fluxo, etc.)

---

## 📚 Leitura Adicional

1. **Livro**: Dym, C. L. (2004). *Principles of Mathematical Modeling*. 2nd Ed.
2. **Artigo**: Buckingham, E. (1914). On Physically Similar Systems. Physical Review.
3. **Guia**: Taylor, E. S. (1974). *Dimensional Analysis for Engineers*.
4. **Software**: SYMPY para análise simbólica de dimensões.

---

## ⚠️ Erros Comuns

❌ **Erro 1**: Confundir dimensão com unidade
✓ Correto: Dimensão é [L], unidade é metro

❌ **Erro 2**: Adicionar termos com dimensões diferentes
✓ Correto: V + 5 segundos é INVÁLIDO

❌ **Erro 3**: Usar fórmulas em unidades incorretas
✓ Correto: Sempre verificar sistema de unidades

❌ **Erro 4**: Esquecer que grupos podem ter formas diferentes
✓ Correto: Π₁ = T₀²g/l é equivalente a T₀/√(l/g)

---

## 🎓 Próximos Passos

1. ✅ Estudar teoria em README.md
2. ✅ Executar exemplos em examples.py
3. ✅ Resolver exercícios em EXERCICIOS.md
4. ✅ Implementar seus próprios problemas
5. ✅ Progredir para Capítulo 3 (Escala)

---

## 📞 Notas

- Última atualização: 2026-04-14
- Baseado em: Dym, C. L. (2004), 2nd Edition
- Nível: Engenheiros e cientistas
- Pré-requisitos: Cálculo, Física Básica

---

**Bom estudo!** 🚀
