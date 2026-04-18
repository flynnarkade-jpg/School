def check(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add a number.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Add a symbol (like ! @ #).")

    strength = ["Very Weak", "Weak", "Okay", "Good", "Strong", "Very Strong"][score]
    return strength, feedback


if __name__ == "__main__":
    pw = input("Enter a password to check: ")
    strength, tips = check(pw)
    print(f"Strength: {strength}")
    for tip in tips:
        print(f" - {tip}")
