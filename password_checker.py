import re
import getpass

# List of common weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "111111", "iloveyou", "admin", "welcome",
    "monkey", "dragon", "master", "sunshine", "princess",
    "letmein", "football", "shadow", "superman", "michael"
]

def check_password_strength(password):
    score = 0
    feedback = []

    # ── Length Check ──────────────────────────────────────────
    length = len(password)
    if length < 6:
        feedback.append("❌ Too short — use at least 8 characters.")
    elif length < 8:
        feedback.append("⚠️  Short — aim for 12+ characters for better security.")
        score += 1
    elif length < 12:
        feedback.append("✅ Decent length (8–11 chars). 12+ is even better.")
        score += 2
    else:
        feedback.append("✅ Great length (12+ characters).")
        score += 3

    # ── Character Type Checks ─────────────────────────────────
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Contains lowercase letters.")
    else:
        feedback.append("❌ Add lowercase letters (a-z).")

    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Contains uppercase letters.")
    else:
        feedback.append("❌ Add uppercase letters (A-Z).")

    if re.search(r'\d', password):
        score += 1
        feedback.append("✅ Contains numbers.")
    else:
        feedback.append("❌ Add numbers (0-9).")

    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 2
        feedback.append("✅ Contains special characters — nice!")
    else:
        feedback.append("❌ Add special characters (!@#$%^&* etc.).")

    # ── Common Password Check ─────────────────────────────────
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("🚨 This is a very common password — change it immediately!")

    # ── Repeated Characters Check ─────────────────────────────
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("⚠️  Avoid repeating characters (e.g. 'aaa', '111').")

    # ── Sequential Characters Check ───────────────────────────
    sequences = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "qwertyuiop", "asdfghjkl"]
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password.lower():
                score -= 1
                feedback.append("⚠️  Avoid sequential patterns (e.g. 'abc', '123', 'qwerty').")
                break

    # ── Strength Rating ───────────────────────────────────────
    score = max(0, score)  # No negative scores

    if score <= 2:
        strength = "🔴 WEAK"
        color = "\033[91m"  # Red
    elif score <= 4:
        strength = "🟠 FAIR"
        color = "\033[93m"  # Yellow
    elif score <= 6:
        strength = "🟡 MODERATE"
        color = "\033[93m"  # Yellow
    elif score <= 7:
        strength = "🟢 STRONG"
        color = "\033[92m"  # Green
    else:
        strength = "💪 VERY STRONG"
        color = "\033[92m"  # Green

    reset = "\033[0m"

    return score, strength, feedback, color, reset


def display_result(password):
    score, strength, feedback, color, reset = check_password_strength(password)

    print("\n" + "="*45)
    print(f"  PASSWORD STRENGTH: {color}{strength}{reset}")
    print(f"  SCORE: {score}/8")
    print("="*45)
    print("\n📋 Feedback:")
    for tip in feedback:
        print(f"   {tip}")

    # Visual strength bar
    bar_filled = min(score, 8)
    bar = "█" * bar_filled + "░" * (8 - bar_filled)
    print(f"\n  Strength Bar: [{color}{bar}{reset}]")
    print()


def main():
    print("\n" + "="*45)
    print("   🔐 PASSWORD STRENGTH CHECKER")
    print("="*45)
    print("  Built for learning cybersecurity basics!")
    print("="*45)

    while True:
        print("\nOptions:")
        print("  [1] Check a password")
        print("  [2] Check password (hidden input)")
        print("  [3] Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            password = input("Enter password to check: ")
            display_result(password)

        elif choice == "2":
            password = getpass.getpass("Enter password (hidden): ")
            display_result(password)

        elif choice == "3":
            print("\n👋 Goodbye! Keep your passwords strong!\n")
            break

        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")

        again = input("Check another password? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Goodbye! Keep your passwords strong!\n")
            break


if __name__ == "__main__":
    main()