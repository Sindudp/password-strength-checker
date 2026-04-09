from src.checker import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_numbers,
    check_symbols
)
from src.common_check import check_common_password
from src.entropy import check_entropy
from src.hibp import check_hibp
from src.utils import (
    print_header,
    print_success,
    print_warning,
    print_error,
    print_info,
    colored_message
)

def run_basic_checks(password):
    print_header("\n--- Password Analysis ---\n")

    checks = [
        check_common_password(password),
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_numbers(password),
        check_symbols(password),
    ]

    passed = 0
    for status, message in checks:
        colored_message(status, message)
        if status:
            passed += 1

    print()
    score_msg = f"{passed}/{len(checks)} checks passed"

    if passed == len(checks):
        print_success(score_msg)
        print_success("💪 Basic structure looks strong!")
    elif passed >= 4:
        print_warning(score_msg)
        print_warning("⚠️  Moderate - improve the missing checks above")
    else:
        print_error(score_msg)
        print_error("🔴 Weak password - fix the issues above")

    # Entropy check
    print_header("\n--- Entropy Analysis ---")
    _, entropy_message = check_entropy(password)

    if "Very Weak" in entropy_message or "Weak" in entropy_message:
        print_error(entropy_message)
    elif "Fair" in entropy_message:
        print_warning(entropy_message)
    else:
        print_success(entropy_message)

    # Breach check
    print_header("\n--- Breach Database Check ---")
    print_info("🔍 Checking breach database...")
    _, hibp_message = check_hibp(password)

    if hibp_message.startswith("✅"):
        print_success(hibp_message)
    elif hibp_message.startswith("⚠️"):
        print_warning(hibp_message)
    else:
        print_error(hibp_message)


if __name__ == "__main__":
    print_header("=== Password Strength Checker ===")
    password = input("\nEnter a password to check: ")
    run_basic_checks(password)