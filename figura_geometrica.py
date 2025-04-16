"""
Módulo de figuras geométricas.

Este módulo define clases para calcular áreas de diferentes figuras geométricas:
rectángulo, triángulo y círculo.
"""

# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""
        # No es necesario usar 'pass' ya que el docstring sirve como cuerpo de la función


class Rectangulo(FiguraGeometrica):
    """Clase para representar un rectángulo."""

    def __init__(self, base, altura):
        """Inicializa un rectángulo con base y altura."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    """Clase para representar un triángulo."""

    def __init__(self, base, altura):
        """Inicializa un triángulo con base y altura."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):
    """Clase para representar un círculo."""

    def __init__(self, radio):
        """Inicializa un círculo con su radio."""
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
