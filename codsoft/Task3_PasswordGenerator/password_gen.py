# Task3_PasswordGenerator: Secure & Customizable Password Generator
# File: password_gen.py

import string
import random

try:
    import pyperclip
    CLIPBOARD_ENABLED = True
except ImportError:
    CLIPBOARD_ENABLED = False

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if not any([use_upper, use_lower, use_digits, use_special]):
        raise ValueError("At least one character type must be selected.")

    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def password_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    strengths = {1: "Very Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
    return strengths.get(score, "Unknown")

def prompt_user():
    print("\n🔐 Password Generator")
    try:
        length = int(input("Enter desired password length (e.g. 12): "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        strength = password_strength(password)

        print(f"\n🧾 Generated Password: {password}")
        print(f"🔒 Strength: {strength}")

        if CLIPBOARD_ENABLED:
            pyperclip.copy(password)
            print("📋 Password copied to clipboard.")
        else:
            print("📋 Install 'pyperclip' to enable clipboard copy.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    while True:
        prompt_user()
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("👋 Exiting Password Generator.")
            break
