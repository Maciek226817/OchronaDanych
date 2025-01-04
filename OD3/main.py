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


# Wynik będzie się różnił za każdym razem, ponieważ program generuje losowe liczby, ale z większą liczbą iteracji wynik będzie coraz bardziej zbliżony do rzeczywistej wartości pi

# def gcd(a, b): Ta funkcja oblicza największy wspólny dzielnik dwóch liczb a i b za pomocą algorytmu Euklidesa
# Funkcja Main:
# generuje 1000000 par liczb losowych w zakresie od 1 do 10000
# dla kazdej pary liczba sprawdza czy są względnie pierwsze NWD = 1
# na końcu oblicza przyblizenie liczby pi na podstawie wzoru
# Na koniec są wyświetlane wyniki