"""
Coleção de funções utilitárias simples para demonstração de testes automatizados.
"""

from __future__ import annotations

from typing import Iterable, Sequence


def factorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro não negativo.
    """
    if not isinstance(n, int):
        raise TypeError("O valor precisa ser um inteiro.")
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    resultado = 1
    for fator in range(2, n + 1):
        resultado *= fator
    return resultado


def fibonacci(n: int) -> int:
    """
    Retorna o n-ésimo número da sequência de Fibonacci.
    """
    if not isinstance(n, int):
        raise TypeError("O valor precisa ser um inteiro.")
    if n < 0:
        raise ValueError("A posição na sequência não pode ser negativa.")
    if n in (0, 1):
        return n
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        anterior, atual = atual, anterior + atual
    return atual


def is_palindrome(texto: str) -> bool:
    """
    Verifica se um texto é palíndromo desconsiderando espaços e caixa.
    """
    if not isinstance(texto, str):
        raise TypeError("O valor precisa ser uma string.")
    normalizado = "".join(caractere.lower() for caractere in texto if caractere.isalnum())
    return normalizado == normalizado[::-1]


def sum_even_numbers(numeros: Iterable[int]) -> int:
    """
    Soma apenas os números pares de uma sequência de inteiros.
    """
    if numeros is None:
        raise ValueError("A sequência de números não pode ser nula.")
    soma = 0
    for numero in numeros:
        if not isinstance(numero, int):
            raise TypeError("Todos os elementos precisam ser inteiros.")
        if numero % 2 == 0:
            soma += numero
    return soma


def normalize(values: Sequence[float]) -> list[float]:
    """
    Normaliza um vetor de valores numéricos para o intervalo [0, 1].
    """
    if values is None or len(values) == 0:
        raise ValueError("A sequência não pode ser vazia.")
    minimo = min(values)
    maximo = max(values)
    if minimo == maximo:
        raise ValueError("Não é possível normalizar uma sequência com todos os valores iguais.")
    intervalo = maximo - minimo
    return [(valor - minimo) / intervalo for valor in values]




