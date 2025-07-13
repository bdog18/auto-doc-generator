import math
import random
from collections import Counter
from typing import Dict, List, Tuple


def reverse_string(s: str) -> str:
    return s[::-1]


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def word_frequency(text: str) -> Dict[str, int]:
    words = text.lower().split()
    return dict(Counter(words))


def generate_password(length: int = 12) -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))


def find_anagrams(word: str, word_list: List[str]) -> List[str]:
    sorted_word = sorted(word)
    return [w for w in word_list if sorted(w) == sorted_word]


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def simulate_stock_price(
    initial_price: float, days: int, volatility: float = 0.02
) -> List[float]:
    prices = [initial_price]
    for _ in range(days):
        change_percent = random.uniform(-volatility, volatility)
        new_price = prices[-1] * (1 + change_percent)
        prices.append(round(new_price, 2))
    return prices


def linear_regression(x: List[float], y: List[float]) -> Tuple[float, float]:
    n = len(x)
    if n != len(y) or n == 0:
        raise ValueError("x and y must be the same length and not empty")
    mean_x, mean_y = sum(x) / n, sum(y) / n
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den = sum((xi - mean_x) ** 2 for xi in x)
    m = num / den
    b = mean_y - m * mean_x
    return m, b


def matrix_multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in A must equal number of rows in B")
    result = [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]
    return result
