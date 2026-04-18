fruits = [
    (150, "apple"),
    (170, "apple"),
    (130, "apple"),
    (50, "grape"),
    (60, "grape"),
    (45, "grape"),
    (200, "orange"),
    (220, "orange"),
    (180, "orange"),
]


def classify(weight):
    closest = min(fruits, key=lambda item: abs(item[0] - weight))
    return closest[1]


if __name__ == "__main__":
    for test in [55, 160, 210, 100]:
        print(f"A fruit weighing {test}g is probably a(n) {classify(test)}.")
