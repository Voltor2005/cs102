def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key_index = 0
    for c in plaintext:
        if 'a' <= c <= 'z':
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            ciphertext += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        elif 'A' <= c <= 'Z':
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            ciphertext += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            ciphertext += c
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key_index = 0
    for c in ciphertext:
        if 'a' <= c <= 'z':
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            plaintext += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        elif 'A' <= c <= 'Z':
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            plaintext += c
    return plaintext