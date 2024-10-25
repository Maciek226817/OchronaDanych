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

# Przykład jak to działa
text_to_encrypt = "MaciejSobiecki"
key = 8

# Szyfrowanie
encrypted_text = Szyfr_Cezara(text_to_encrypt, key, mode='encrypt')
print(f"Zaszyfrowany tekst: {encrypted_text}")

# Odszyfrowanie
decrypted_text = Szyfr_Cezara(encrypted_text, key, mode='decrypt')
print(f"Odszyfrowany tekst: {decrypted_text}")