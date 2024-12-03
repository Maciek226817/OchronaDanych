import numpy as np

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IPInverse = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

Key1 = []
Key2 = []

def permute(input_bits, table):
    return [input_bits[i - 1] for i in table]

def left_shift(bits, shifts):
    return np.roll(bits, -shifts).tolist()

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

def sbox(input_bits, sbox):
    row = int(f"{input_bits[0]}{input_bits[3]}", 2)
    col = int(f"{input_bits[1]}{input_bits[2]}", 2)
    value = sbox[row][col]
    return [value // 2, value % 2]

def combine(left, right):
    return left + right

def swap(input_bits):
    return input_bits[4:] + input_bits[:4]

def fk(input_bits, subkey):
    left = input_bits[:4]
    right = input_bits[4:]

    expanded = permute(right, EP)
    xor_result = xor(expanded, subkey)

    sbox_result = sbox(xor_result[:4], S0) + sbox(xor_result[4:], S1)
    permuted = permute(sbox_result, P4)

    return combine(xor(left, permuted), right)

def generate_keys(key):
    global Key1, Key2

    permuted_key = permute(key, P10)
    left = left_shift(permuted_key[:5], 1)
    right = left_shift(permuted_key[5:], 1)

    Key1 = permute(combine(left, right), P8)

    left = left_shift(left, 2)
    right = left_shift(right, 2)

    Key2 = permute(combine(left, right), P8)

def encrypt(plaintext):
    permuted = permute(plaintext, IP)
    fk1_result = fk(permuted, Key1)
    swapped = swap(fk1_result)
    fk2_result = fk(swapped, Key2)
    return permute(fk2_result, IPInverse)

def decrypt(ciphertext):
    permuted = permute(ciphertext, IP)
    fk2_result = fk(permuted, Key2)
    swapped = swap(fk2_result)
    fk1_result = fk(swapped, Key1)
    return permute(fk1_result, IPInverse)

if __name__ == "__main__":
    key_input = input("Podaj klucz (10 bitów): ")
    plaintext_input = input("Podaj tekst jawny (8 bitów): ")

    key = [int(bit) for bit in key_input.strip()]
    plaintext = [int(bit) for bit in plaintext_input.strip()]

    if len(key) != 10 or len(plaintext) != 8:
        print("Błąd: Klucz musi mieć 10 bitów, a tekst jawny 8 bitów.")
    else:
        generate_keys(key)

        print("Klucz 1:", "".join(map(str, Key1)))
        print("Klucz 2:", "".join(map(str, Key2)))

        ciphertext = encrypt(plaintext)
        print("Zaszyfrowany tekst:", "".join(map(str, ciphertext)))

        decrypted = decrypt(ciphertext)
        print("Odszyfrowany tekst:", "".join(map(str, decrypted)))