"""Funciones estadísticas básicas: media, mediana y moda.

Uso:
-----
from estadistica_basica import media, mediana, moda
"""

from collections import Counter
from typing import Iterable, List, Union, Optional

Numero = Union[int, float]

def media(valores: Iterable[Numero]) -> float:
    """Calcula la media aritmética.
    
    Parámetros
    ----------
    valores : Iterable[Numero]
        Secuencia de números (no vacía).
    
    Retorna
    -------
    float
        Promedio de los valores.
    """
    vals = list(valores)
    if not vals:
        raise ValueError("'valores' no puede estar vacío")
    return sum(vals) / len(vals)

def mediana(valores: Iterable[Numero]) -> float:
    """Calcula la mediana (valor central).
    
    Si hay cantidad par, retorna el promedio de los dos centrales.
    """
    vals = sorted(list(valores))
    n = len(vals)
    if n == 0:
        raise ValueError("'valores' no puede estar vacío")
    mitad = n // 2
    if n % 2 == 1:
        return float(vals[mitad])
    else:
        return (vals[mitad - 1] + vals[mitad]) / 2

def moda(valores: Iterable[Numero]) -> Numero:
    """Calcula la moda (valor más frecuente).
    
    Si hay empate, retorna cualquiera de las modas.
    """
    vals = list(valores)
    if not vals:
        raise ValueError("'valores' no puede estar vacío")
    c = Counter(vals)
    valor, _ = c.most_common(1)[0]
    return valor
