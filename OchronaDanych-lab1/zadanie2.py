def extend_key(text, key):
    # Jeśli długość klucza jest krótsza niż długość tekstu, funkcja powtarza klucz, aby miał on tę samą długość co tekst.
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

# Szyfruje podany tekst za pomocą szyfru Vigenère'a. Dla każdej litery tekstu przelicza jej nową pozycję w alfabecie,
# uwzględniając wartość odpowiadającej jej litery z klucza.
# Duże litery są szyfrowane jako duże, a małe jako małe. Znaki inne niż litery (np. cyfry, spacje) nie są szyfrowane.
def szyfruj_vigenere(text, key):
    encrypted_text = []
    key = extend_key(text, key)

    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                shift = (ord(text[i]) + ord(key[i].upper()) - 2 * ord('A')) % 26
                encrypted_text.append(chr(shift + ord('A')))
            else:
                shift = (ord(text[i]) + ord(key[i].lower()) - 2 * ord('a')) % 26
                encrypted_text.append(chr(shift + ord('a')))
        else:
            encrypted_text.append(text[i])

    return ''.join(encrypted_text)
# Odszyfrowuje zaszyfrowany tekst przy użyciu tego samego klucza, cofając przesunięcia liter, które zostały zastosowane w procesie szyfrowania.
def deszyfruj_vigenere(text, key):
    decrypted_text = []
    key = extend_key(text, key)

    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                shift = (ord(text[i]) - ord(key[i].upper()) + 26) % 26
                decrypted_text.append(chr(shift + ord('A')))
            else:
                shift = (ord(text[i]) - ord(key[i].lower()) + 26) % 26
                decrypted_text.append(chr(shift + ord('a')))
        else:
            decrypted_text.append(text[i])

    return ''.join(decrypted_text)


# Przykład
plaintext = "MaciejSobiecki"
key = "KEY"
# Szyfrowanie
encrypted_text = szyfruj_vigenere(plaintext, key)
print(f"Encrypted text: {encrypted_text}")
# Deszyfrowanie
decrypted_text = deszyfruj_vigenere(encrypted_text, key)
print(f"Decrypted text: {decrypted_text}")