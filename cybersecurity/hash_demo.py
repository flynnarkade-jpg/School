import hashlib


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


if __name__ == "__main__":
    password = "hunter2"
    print(f"Password: {password}")
    print(f"SHA-256:  {sha256(password)}")

    print(f"\nSame input always gives the same hash:")
    print(sha256(password))
    print(sha256(password))

    print(f"\nA tiny change gives a completely different hash:")
    print(sha256("hunter2"))
    print(sha256("Hunter2"))
