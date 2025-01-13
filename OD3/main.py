import random
import math

# Funkcja obliczająca NWD za pomocą algorytmu Euklidesa
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    iterations = 1000000  # Liczba iteracji
    coprime_count = 0  # Liczba par względnie pierwszych

    # Pętla generująca losowe liczby
    for _ in range(iterations):
        x = random.randint(1, 10000)  # Zakres mniejszych liczb
        y = random.randint(1, 10000)  # Zakres mniejszych liczb

        # Sprawdzanie, czy liczby są względnie pierwsze
        if gcd(x, y) == 1:
            coprime_count += 1

    # Obliczanie prawdopodobieństwa i przybliżenia pi
    probability = coprime_count / iterations
    pi_approximation = math.sqrt(6.0 / probability)

    # Wyświetlanie wyników
    print(f"Liczba iteracji: {iterations}")
    print(f"Liczba par wzajemnie pierwszych: {coprime_count}")
    print(f"Przybliżona wartość pi: {pi_approximation}")

if __name__ == "__main__":
    main()

# WYJAŚNIENIE


# Wartość π jest bliska rzeczywistej wartości 3.1415... Im więcej iteracji tym przybliżenie jest dokładniejsze
# Teoria Cesaro opiera się na analizie liczby par liczb całkowitych, które są wzajemnie pierwsze. Prawdopodobieństwo to jest związane z wartością π,
# które można zaobserwować, w miarę jak liczba iteracji rośnie, przybliżenie staje się coraz bardziej dokładne, ponieważ rozkład liczb wzajemnie pierwszych wśród liczb całkowitych
# jest ściśle powiązany z funkcją związaną z liczbą π.
# W kodzie użyto generatora liczb pseudolosowych random.randint(). Nie jest on odpowiedni do zastosowań kryptograficznych.
# W przypadku wymagań kryptograficznych należy zastosować bezpieczny generator liczb losowych, np. moduł secrets dostępny w bibliotece standardowej Pythona.