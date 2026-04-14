"""
Exemplos Práticos de Análise Dimensional

Aplicações do Capítulo 2 em problemas reais.
"""

import numpy as np
import matplotlib.pyplot as plt
from dimensional_analysis import Dimension


# ============================================================================
# EXEMPLO 1: PERÍODO DO PÊNDULO SIMPLES
# ============================================================================

def exemplo_1_pendulum():
    """
    Problema: Encontrar o período de um pêndulo simples.

    Variáveis envolvidas:
    - l: comprimento da corda [L]
    - g: aceleração da gravidade [L/T²]
    - m: massa da esfera [M]
    - T₀: período [T]

    Solução usando o Método Básico:
    1. Eliminar dimensão T usando g e T₀ em conjunto
    2. Eliminar dimensão M notando que não aparece em outras variáveis
    3. Encontrar relação adimensional entre l e g
    """

    print("\n" + "="*70)
    print("EXEMPLO 1: PERÍODO DO PÊNDULO SIMPLES")
    print("="*70)

    print("\n1. FORMULAÇÃO DO PROBLEMA")
    print("-" * 70)
    print("   T₀ = T₀(l, g, m)")
    print("   onde:")
    print("      l = comprimento da corda")
    print("      g = aceleração da gravidade")
    print("      m = massa da esfera")
    print("      T₀ = período (variável dependente)")

    print("\n2. DIMENSÕES DAS VARIÁVEIS")
    print("-" * 70)
    vars_pendulum = {
        'l': Dimension(length=1),
        'g': Dimension(length=1, time=-2),
        'm': Dimension(mass=1),
        'T0': Dimension(time=1),
    }

    for name, dim in vars_pendulum.items():
        print(f"   [{name:3s}] = {dim}")

    print("\n3. ANÁLISE DIMENSIONAL")
    print("-" * 70)
    print("   Sendo T₀ função de l, g, m:")
    print("   T₀ = C · l^a · g^b · m^c")
    print()
    print("   [T] = [L]^a · [L/T²]^b · [M]^c")
    print("   [T] = [M]^c · [L]^(a+b) · [T]^(-2b)")
    print()
    print("   Igualando expoentes:")
    print("      M:  0 = c           ⟹ c = 0   (m não aparece!)")
    print("      L:  0 = a + b       ⟹ a = -b")
    print("      T:  1 = -2b         ⟹ b = -1/2, a = 1/2")

    print("\n4. RESULTADO")
    print("-" * 70)
    print("   T₀ = C · √(l/g)")
    print()
    print("   Conhecimento de física: C = 2π")
    print("   Fórmula clássica: T₀ = 2π√(l/g)")

    print("\n5. VERIFICAÇÃO NUMÉRICA")
    print("-" * 70)
    g = 9.81  # m/s²
    lengths = np.array([0.25, 0.50, 1.00, 1.50, 2.00])  # metros
    periods = 2 * np.pi * np.sqrt(lengths / g)

    print(f"   {'Comprimento (m)':>18} | {'Período (s)':>15}")
    print("   " + "-" * 36)
    for l, T in zip(lengths, periods):
        print(f"   {l:18.2f} | {T:15.4f}")


# ============================================================================
# EXEMPLO 2: VELOCIDADE DE CORPO EM QUEDA
# ============================================================================

def exemplo_2_falling_body():
    """
    Problema: Encontrar a velocidade de um corpo em queda.

    Variáveis:
    - V: velocidade [L/T]
    - g: aceleração da gravidade [L/T²]
    - h: altura da queda [L]
    - m: massa (será eliminada)

    Este exemplo mostra que a massa não afeta a velocidade de queda!
    """

    print("\n" + "="*70)
    print("EXEMPLO 2: VELOCIDADE DE CORPO EM QUEDA")
    print("="*70)

    print("\n1. FORMULAÇÃO")
    print("-" * 70)
    print("   V = V(g, h, m)")
    print("   Encontrar como V depende de g, h, m")

    print("\n2. MÉTODO BÁSICO")
    print("-" * 70)
    print("   V = C · g^a · h^b · m^c")
    print()
    print("   [L/T] = [L/T²]^a · [L]^b · [M]^c")
    print("   [L/T] = [M]^c · [L]^(a+b) · [T]^(-2a)")
    print()
    print("   Igualando expoentes:")
    print("      M:  0 = c           ⟹ c = 0   (massa irrelevante!)")
    print("      L:  1 = a + b")
    print("      T: -1 = -2a         ⟹ a = 1/2")
    print()
    print("   From a = 1/2 and a + b = 1:")
    print("      b = 1/2")

    print("\n3. RESULTADO")
    print("-" * 70)
    print("   V = C · √(g · h)")
    print()
    print("   Física: V = √(2gh)  (com C = √2)")
    print()
    print("   INTERPRETAÇÃO: A velocidade é INDEPENDENTE da massa!")
    print("   (Galileu verificou isso empiricamente)")

    print("\n4. CÁLCULOS NUMÉRICOS")
    print("-" * 70)
    g = 9.81  # m/s²
    heights = np.array([1, 5, 10, 20, 50, 100])  # metros

    print(f"   {'Altura (m)':>15} | {'Velocidade (m/s)':>20}")
    print("   " + "-" * 38)

    for h in heights:
        V = np.sqrt(2 * g * h)
        print(f"   {h:15.1f} | {V:20.2f}")


# ============================================================================
# EXEMPLO 3: FORÇA DE ARRASTO NO MISTURADOR
# ============================================================================

def exemplo_3_mixer():
    """
    Problema: Encontrar a força de arrasto ao mexer em manteiga de amendoim.

    Variáveis:
    - FD: força de arrasto [M·L/T²]
    - V: velocidade da lâmina [L/T]
    - d: largura da lâmina [L]
    - ρ: densidade do fluido [M/L³]
    - μ: viscosidade dinâmica [M/(L·T)]

    Este exemplo mostra como reduzir 5 variáveis a 2 grupos dimensionless.
    """

    print("\n" + "="*70)
    print("EXEMPLO 3: FORÇA DE ARRASTO EM MISTURADOR DE MANTEIGA")
    print("="*70)

    print("\n1. PROBLEMA: Quantos experimentos são necessários?")
    print("-" * 70)
    print("   Variáveis: 5 (FD, V, d, ρ, μ)")
    print("   Se variarmos 3 valores para cada:")
    print("      Experimentos necessários = 3⁵ = 243")
    print()
    print("   Com análise dimensional:")
    print("      n = 5 (variáveis)")
    print("      m = 3 (dimensões: M, L, T)")
    print("      Grupos dimensionless = n - m = 2")
    print("      Experimentos necessários ≈ 3² = 9  ✓✓✓")

    print("\n2. APLICAR TEOREMA DE BUCKINGHAM PI")
    print("-" * 70)

    vars_mixer = {
        'FD': Dimension(mass=1, length=1, time=-2),
        'V': Dimension(length=1, time=-1),
        'd': Dimension(length=1),
        'rho': Dimension(mass=1, length=-3),
        'mu': Dimension(mass=1, length=-1, time=-1),
    }

    print("   Dimensões:")
    for name, dim in vars_mixer.items():
        print(f"      [{name:3s}] = {dim}")

    print("\n   Construindo grupos dimensionless:")
    print("   Escolher base: V, d, ρ (contêm M, L, T)")
    print()

    # Grupo 1
    print("   Π₁ = μ / (ρ · V · d)")
    pi1_dims = vars_mixer['mu'] / (vars_mixer['rho'] * vars_mixer['V'] * vars_mixer['d'])
    print(f"       Dimensão: {pi1_dims}")
    print(f"       Adimensional? {pi1_dims.is_dimensionless()} ✓")
    print()

    # Grupo 2
    print("   Π₂ = FD / (ρ · V² · d²)")
    pi2_dims = vars_mixer['FD'] / (vars_mixer['rho'] * vars_mixer['V']**2 * vars_mixer['d']**2)
    print(f"       Dimensão: {pi2_dims}")
    print(f"       Adimensional? {pi2_dims.is_dimensionless()} ✓")

    print("\n3. RELAÇÃO FUNCIONAL")
    print("-" * 70)
    print("   Π₂ = f(Π₁)")
    print()
    print("   FD/(ρV²d²) = f(μ/(ρVd))")
    print()
    print("   Isso significa:")
    print("   FD = ρ · V² · d² · f(μ/(ρVd))")

    print("\n4. INTERPRETAÇÃO FÍSICA")
    print("-" * 70)
    print("   A força de arrasto depende de:")
    print("   • ρV²d² (efeitos inerciais)")
    print("   • μ/(ρVd) = 1/Re (número de Reynolds)")
    print()
    print("   Em regimes diferentes de Reynolds:")
    print("      Re < 1:     FD ∝ μVd   (fluxo viscoso)")
    print("      Re > 10³:   FD ∝ ρV²d² (fluxo turbulento)")


# ============================================================================
# EXEMPLO 4: NÚMERO DE REYNOLDS
# ============================================================================

def exemplo_4_reynolds():
    """
    Exemplo: O Número de Reynolds é um grupo dimensionless importante.
    """

    print("\n" + "="*70)
    print("EXEMPLO 4: NÚMERO DE REYNOLDS (grupo dimensionless importante)")
    print("="*70)

    print("\n1. DEFINIÇÃO")
    print("-" * 70)
    print("   O Número de Reynolds quantifica a importância relativa")
    print("   de forças inerciais vs forças viscosas:")
    print()
    print("   Re = ρVl/μ = (ρVl)/μ")
    print()
    print("   onde:")
    print("      ρ = densidade do fluido")
    print("      V = velocidade característica")
    print("      l = comprimento característico")
    print("      μ = viscosidade dinâmica")

    print("\n2. VERIFICAÇÃO DIMENSIONAL")
    print("-" * 70)

    dims = {
        'rho': Dimension(mass=1, length=-3),
        'V': Dimension(length=1, time=-1),
        'l': Dimension(length=1),
        'mu': Dimension(mass=1, length=-1, time=-1),
    }

    Re_dim = (dims['rho'] * dims['V'] * dims['l']) / dims['mu']
    print(f"   [Re] = (M/L³) · (L/T) · (L) / (M/(LT))")
    print(f"        = {Re_dim}")
    print(f"   Adimensional? {Re_dim.is_dimensionless()} ✓")

    print("\n3. INTERPRETAÇÃO")
    print("-" * 70)
    print("   Re << 1:     Fluxo Stokes (viscoso dominante)")
    print("   Re ≈ 1-10:   Transição")
    print("   Re >> 1:     Fluxo turbulento (inércia dominante)")

    print("\n4. EXEMPLOS PRÁTICOS")
    print("-" * 70)

    # Casos típicos
    cases = [
        ("Espermatozoide em água", 1e-4, 1000, 1e-5, 0.001),
        ("Queda de chuva (1mm)", 0.01, 1000, 1e-5, 0.001),
        ("Esfera de 1cm caindo", 0.01, 1000, 1e-5, 0.01),
        ("Avião voando (v=100m/s)", 100, 1.2, 2e-5, 1),
        ("Navio (v=10m/s)", 10, 1000, 1e-3, 100),
    ]

    print(f"\n   {'Caso':30} | {'Re':>10}")
    print("   " + "-" * 43)

    for case, V, rho, mu, l in cases:
        Re = (rho * V * l) / mu
        print(f"   {case:30} | {Re:10.1e}")


# ============================================================================
# EXEMPLO 5: CONVERSÃO DE UNIDADES
# ============================================================================

def exemplo_5_units():
    """
    Exemplo: A importância de conversão correta de unidades.
    """

    print("\n" + "="*70)
    print("EXEMPLO 5: CONVERSÃO CORRETA DE UNIDADES")
    print("="*70)

    print("\n Problema Real: NASA - Mars Climate Orbiter (1998)")
    print("-" * 70)
    print(" A sonda foi destruída porque um dos times usou libras-força")
    print(" enquanto outro usava newtons nos cálculos de manobra.")
    print(" Custo: $327.6 milhões")

    print("\n1. CONVERSÃO: 65 mi/hr para m/s")
    print("-" * 70)

    velocity_mph = 65

    print(f"   Velocidade original: {velocity_mph} mi/hr")
    print()
    print("   Factores de conversão:")
    print("      1 mile = 5280 feet")
    print("      1 foot = 0.3048 meters")
    print("      1 hour = 3600 seconds")
    print()

    # Conversão passo a passo
    step1 = velocity_mph * 5280  # mi/hr → ft/hr
    print(f"   Passo 1: {velocity_mph} mi/hr × 5280 ft/mi = {step1} ft/hr")

    step2 = step1 * 0.3048  # ft/hr → m/hr
    print(f"   Passo 2: {step1} ft/hr × 0.3048 m/ft = {step2} m/hr")

    step3 = step2 / 3600  # m/hr → m/s
    print(f"   Passo 3: {step2} m/hr ÷ 3600 s/hr = {step3:.2f} m/s")

    print()
    print("   Forma compacta:")
    print(f"   65 mi/hr × (5280/3600) × 0.3048 = {velocity_mph * 5280/3600 * 0.3048:.2f} m/s")

    print("\n2. VERIFICAÇÃO DIMENSIONAL")
    print("-" * 70)
    print("   [mi/hr] × [ft/mi] × [m/ft] × [hr/s]")
    print("   = [mi/hr × ft/mi × m/ft × 1/s]")
    print("   = [m/s]  ✓")

    print("\n3. PREFIXOS SI")
    print("-" * 70)

    prefixes = {
        10**9: 'giga (G)',
        10**6: 'mega (M)',
        10**3: 'kilo (k)',
        1: '(base)',
        10**-3: 'mili (m)',
        10**-6: 'micro (μ)',
        10**-9: 'nano (n)',
    }

    for factor, name in sorted(prefixes.items(), reverse=True):
        print(f"   10^{np.log10(factor):>3.0f}: {name}")


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # Executar todos os exemplos
    exemplo_1_pendulum()
    exemplo_2_falling_body()
    exemplo_3_mixer()
    exemplo_4_reynolds()
    exemplo_5_units()

    print("\n" + "="*70)
    print("EXEMPLOS PRÁTICOS CONCLUÍDOS")
    print("="*70)
    print("\nPontos-chave:")
    print("  ✓ Análise dimensional elimina variáveis desnecessárias")
    print("  ✓ Reduz drasticamente o número de experimentos necessários")
    print("  ✓ Ajuda a validar fórmulas e modelos")
    print("  ✓ Conversão correta de unidades é CRÍTICA")
    print("="*70 + "\n")
