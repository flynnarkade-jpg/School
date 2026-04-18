def encode(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decode(text, shift):
    return encode(text, -shift)


if __name__ == "__main__":
    message = "Hello, School!"
    secret = encode(message, 3)
    print(f"Original: {message}")
    print(f"Encoded:  {secret}")
    print(f"Decoded:  {decode(secret, 3)}")
