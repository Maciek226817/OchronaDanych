def Szyfr_Cezara(text, key, mode='encrypt'):
    result = []
    if mode == 'decrypt':
        key = -key
    # Sprawdzenie każdego znaku, małe i wielke litery
    for char in text:
        if char.isupper():
            shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result.append(shifted_char)
        elif char.islower():
            shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result.append(shifted_char)
        else:
            result.append(char)

    return ''.join(result)

text = input("Podaj tekst do zaszyfrowania lub odszyfrowania: ")
key = int(input("Podaj klucz (liczbę całkowitą): "))
mode = input("Wybierz tryb (encrypt/decrypt): ").strip().lower()

if mode not in ['encrypt', 'decrypt']:
    print("Nieprawidłowy tryb. Wybierz 'encrypt' lub 'decrypt'.")
else:
    result_text = Szyfr_Cezara(text, key, mode)
    print(f"Wynik: {result_text}")

