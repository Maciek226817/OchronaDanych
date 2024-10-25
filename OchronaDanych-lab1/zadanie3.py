import string
from collections import Counter

# Częstotliwości liter w języku polskim
polish_frequencies = {
    'a': 0.097, 'b': 0.018, 'c': 0.038, 'd': 0.045, 'e': 0.085,
    'f': 0.021, 'g': 0.014, 'h': 0.029, 'i': 0.085, 'j': 0.020,
    'k': 0.034, 'l': 0.048, 'm': 0.032, 'n': 0.072, 'o': 0.079,
    'p': 0.033, 'r': 0.066, 's': 0.059, 't': 0.034, 'u': 0.036,
    'w': 0.042, 'y': 0.038, 'z': 0.031,
}


def caesar_decrypt(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted_text.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)


def score_text(text):
    letter_count = Counter(filter(str.isalpha, text.lower()))
    total_letters = sum(letter_count.values())
    score = 0
    for letter, freq in polish_frequencies.items():
        observed_freq = letter_count[letter] / total_letters if total_letters > 0 else 0
        score += (observed_freq - freq) ** 2
    return score


def analyze_decryptions(ciphertext, num_results=10):
    decryptions = [(shift, caesar_decrypt(ciphertext, shift), score_text(caesar_decrypt(ciphertext, shift))) for shift
                   in range(26)]
    decryptions.sort(key=lambda x: x[2])
    return decryptions[:num_results]


def main():
    ciphertext = input("Podaj zaszyfrowany tekst: ")
    num_results = min(int(input("Ile najbardziej prawdopodobnych odszyfrowań chcesz zobaczyć? (do 10): ")), 10)
    probable_texts = analyze_decryptions(ciphertext, num_results)

    print("\nNajbardziej prawdopodobne odszyfrowania:")
    for shift, text, _ in probable_texts:
        print(f"Przesunięcie {shift}: {text}")


if __name__ == "__main__":
    main()
