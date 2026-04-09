import os

def load_common_passwords():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    wordlist_path = os.path.join(base_dir, "wordlists", "most-common.txt")
    
    try:
        with open(wordlist_path, "r", encoding="utf-8") as f:
            common = set(line.strip().lower() for line in f if line.strip())
        return common
    except FileNotFoundError:
        print("⚠️  Wordlist file not found! Skipping common password check.")
        return set()


def check_common_password(password):
    common_passwords = load_common_passwords()
    
    if not common_passwords:
        return False, "⚠️  Common password check skipped (wordlist missing)"
    
    if password.lower() in common_passwords:
        return False, "❌ This is a very common password - hackers will guess this instantly!"
    
    return True, "✅ Not a commonly used password"