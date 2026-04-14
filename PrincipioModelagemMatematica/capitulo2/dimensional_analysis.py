"""
Análise Dimensional - Implementação

Ferramentas para validar e analisar equações dimensionalmente.
"""

from typing import Dict, List, Tuple
from itertools import permutations
import numpy as np
from fractions import Fraction


class Dimension:
    """Representa as dimensões de uma quantidade física."""

    def __init__(self, mass=0, length=0, time=0, temperature=0):
        """
        Inicializa uma dimensão.

        Args:
            mass: Expoente de massa (M)
            length: Expoente de comprimento (L)
            time: Expoente de tempo (T)
            temperature: Expoente de temperatura (Θ)
        """
        self.M = mass
        self.L = length
        self.T = time
        self.Theta = temperature

    def __mul__(self, other):
        """Multiplicação de dimensões."""
        if isinstance(other, (int, float)):
            return self
        return Dimension(
            self.M + other.M,
            self.L + other.L,
            self.T + other.T,
            self.Theta + other.Theta
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divisão de dimensões."""
        return Dimension(
            self.M - other.M,
            self.L - other.L,
            self.T - other.T,
            self.Theta - other.Theta
        )

    def __pow__(self, exponent):
        """Potência de dimensão."""
        return Dimension(
            self.M * exponent,
            self.L * exponent,
            self.T * exponent,
            self.Theta * exponent
        )

    def __eq__(self, other):
        """Igualdade de dimensões."""
        return (self.M == other.M and
                self.L == other.L and
                self.T == other.T and
                self.Theta == other.Theta)

    def is_dimensionless(self):
        """Verifica se a dimensão é adimensional."""
        return self.M == 0 and self.L == 0 and self.T == 0 and self.Theta == 0

    def to_vector(self):
        """Retorna a dimensão como vetor [M, L, T, Θ]."""
        return np.array([self.M, self.L, self.T, self.Theta])

    def __repr__(self):
        """Representação em string."""
        parts = []
        if self.M != 0:
            parts.append(f"M^{self.M}" if self.M != 1 else "M")
        if self.L != 0:
            parts.append(f"L^{self.L}" if self.L != 1 else "L")
        if self.T != 0:
            parts.append(f"T^{self.T}" if self.T != 1 else "T")
        if self.Theta != 0:
            parts.append(f"Θ^{self.Theta}" if self.Theta != 1 else "Θ")

        if not parts:
            return "[1]"
        return "[" + "·".join(parts) + "]"


class DimensionalAnalysis:
    """Ferramenta para análise dimensional usando o Teorema de Buckingham Pi."""

    def __init__(self, variables: Dict[str, Dimension]):
        """
        Inicializa a análise dimensional.

        Args:
            variables: Dicionário {nome_variável: Dimension}
        """
        self.variables = variables
        self.n_variables = len(variables)
        self.dimensions_matrix = self._build_dimension_matrix()
        self.n_fundamental_dimensions = np.linalg.matrix_rank(
            self.dimensions_matrix
        )
        self.n_dimensionless_groups = self.n_variables - self.n_fundamental_dimensions

    def _build_dimension_matrix(self):
        """Constrói a matriz de dimensões (m x n)."""
        var_names = list(self.variables.keys())
        dimensions = [self.variables[name].to_vector()
                      for name in var_names]
        return np.array(dimensions).T  # Transpõe para ter dimensões como linhas

    def check_dimensional_consistency(self, equation_terms: List[Dimension]) -> bool:
        """
        Verifica se todos os termos de uma equação têm as mesmas dimensões.

        Args:
            equation_terms: Lista de dimensões dos termos da equação

        Returns:
            True se todas têm a mesma dimensão, False caso contrário
        """
        if not equation_terms:
            return False

        first_dim = equation_terms[0]
        return all(dim == first_dim for dim in equation_terms)

    def get_pi_groups_count(self):
        """Retorna o número de grupos dimensionless (Π)."""
        return self.n_dimensionless_groups

    def analyze(self):
        """Analisa o sistema e reporta informações dimensionais."""
        print(f"{'='*60}")
        print(f"ANÁLISE DIMENSIONAL")
        print(f"{'='*60}\n")

        print(f"Variáveis: {', '.join(self.variables.keys())}\n")

        print("Dimensões:")
        for name, dim in self.variables.items():
            print(f"  {name:20s} {dim}")

        print(f"\nNúmero total de variáveis (n): {self.n_variables}")
        print(f"Dimensões fundamentais (m): {self.n_fundamental_dimensions}")
        print(f"Grupos dimensionless (n-m): {self.n_dimensionless_groups}")
        print(f"\nMatriz de dimensões:")
        print(self.dimensions_matrix)
        print()


def pendulum_analysis():
    """Exemplo: Análise dimensional do pêndulo simples."""
    print("\n" + "="*60)
    print("EXEMPLO 1: PERÍODO DO PÊNDULO SIMPLES")
    print("="*60)

    # Variáveis do pêndulo
    variables = {
        'l': Dimension(length=1),           # comprimento
        'g': Dimension(length=1, time=-2),  # aceleração
        'm': Dimension(mass=1),              # massa
        'T0': Dimension(time=1),            # período
    }

    analysis = DimensionalAnalysis(variables)
    analysis.analyze()

    # Verificar alguns grupos dimensionless
    print("Grupos Dimensionless Propostos:")

    # Π₁ = T₀ / √(l/g)
    pi1 = variables['T0'] / (variables['l'] / variables['g']) ** 0.5
    print(f"  Π₁ = T₀ / √(l/g) = {pi1}")
    print(f"  Adimensional? {pi1.is_dimensionless()}\n")

    # Π₂ = m
    pi2 = variables['m']
    print(f"  Π₂ = m = {pi2}")
    print(f"  Adimensional? {pi2.is_dimensionless()}\n")


def falling_body_analysis():
    """Exemplo: Análise dimensional de corpo em queda."""
    print("\n" + "="*60)
    print("EXEMPLO 2: VELOCIDADE DE CORPO EM QUEDA")
    print("="*60)

    variables = {
        'V': Dimension(length=1, time=-1),   # velocidade
        'g': Dimension(length=1, time=-2),   # aceleração
        'h': Dimension(length=1),            # altura
        'm': Dimension(mass=1),              # massa
    }

    analysis = DimensionalAnalysis(variables)
    analysis.analyze()

    # Teste: V deve ser proporcional a √(gh)
    expected = (variables['g'] * variables['h']) ** 0.5
    actual = variables['V']

    print(f"V tem dimensão: {actual}")
    print(f"√(gh) tem dimensão: {expected}")
    print(f"Dimensionalmente consistente? {actual == expected}")


def peanut_butter_mixer_analysis():
    """Exemplo: Análise dimensional do misturador de amendoim."""
    print("\n" + "="*60)
    print("EXEMPLO 3: FORÇA DE ARRASTO EM MISTURADOR")
    print("="*60)

    variables = {
        'FD': Dimension(mass=1, length=1, time=-2),  # força arrasto
        'V': Dimension(length=1, time=-1),           # velocidade
        'd': Dimension(length=1),                    # largura lâmina
        'rho': Dimension(mass=1, length=-3),         # densidade
        'mu': Dimension(mass=1, length=-1, time=-1), # viscosidade
    }

    analysis = DimensionalAnalysis(variables)
    analysis.analyze()

    # Dois grupos dimensionless
    print("Grupos Dimensionless:")

    # Π₁ = μ / (ρ V d) - adimensional com viscosidade
    pi1 = variables['mu'] / (variables['rho'] * variables['V'] * variables['d'])
    print(f"  Π₁ = μ / (ρ V d) = {pi1}")
    print(f"  Adimensional? {pi1.is_dimensionless()}\n")

    # Π₂ = FD / (ρ V² d²)
    pi2 = variables['FD'] / (variables['rho'] * variables['V']**2 * variables['d']**2)
    print(f"  Π₂ = FD / (ρ V² d²) = {pi2}")
    print(f"  Adimensional? {pi2.is_dimensionless()}\n")


def unit_conversion_example():
    """Exemplo: Conversão de unidades."""
    print("\n" + "="*60)
    print("EXEMPLO 4: CONVERSÃO DE UNIDADES")
    print("="*60)

    # Converter 65 mph para m/s
    velocity_mph = 65

    # Fatores de conversão
    ft_per_mile = 5280
    m_per_ft = 0.3048
    s_per_hour = 3600

    velocity_ms = velocity_mph * ft_per_mile * m_per_ft / s_per_hour

    print(f"Velocidade original: {velocity_mph} mi/hr")
    print(f"\nCálculo:")
    print(f"  {velocity_mph} mi/hr × (5280 ft/mi) × (0.3048 m/ft) ÷ (3600 s/hr)")
    print(f"  = {velocity_mph * ft_per_mile} ft/hr")
    print(f"  = {velocity_mph * ft_per_mile * m_per_ft} m/hr")
    print(f"  = {velocity_ms:.2f} m/s")


if __name__ == "__main__":
    # Executar todos os exemplos
    pendulum_analysis()
    falling_body_analysis()
    peanut_butter_mixer_analysis()
    unit_conversion_example()

    print("\n" + "="*60)
    print("Análise dimensional concluída!")
    print("="*60)
