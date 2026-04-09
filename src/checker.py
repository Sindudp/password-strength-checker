def check_length(password):
    if len(password) < 8:
        return False, "❌ Too short - it must be at least 8 characters"
    elif len(password) < 12:
        return True, "⚠️  Length is okay but create a 12+ characters it's stronger"
    else:
        return True, "✅ Your password is a good length"


def check_uppercase(password):
    if any(c.isupper() for c in password):
        return True, "✅ Contains uppercase letter"
    return False, "❌ Missing uppercase letter (A-Z)"


def check_lowercase(password):
    if any(c.islower() for c in password):
        return True, "✅ Contains lowercase letter"
    return False, "❌ Missing lowercase letter (a-z)"


def check_numbers(password):
    if any(c.isdigit() for c in password):
        return True, "✅ Contains number"
    return False, "❌ Missing number (0-9)"


def check_symbols(password):
    symbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    if any(c in symbols for c in password):
        return True, "✅ Contains special character"
    return False, "❌ Missing special character (!@#$ etc.)"