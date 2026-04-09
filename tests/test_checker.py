import sys
import os

# This allows test file to find src folder
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.checker import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_numbers,
    check_symbols
)
from src.common_check import check_common_password
from src.entropy import check_entropy

# ─────────────────────────────────────────
# Test Helper
# ─────────────────────────────────────────
passed_tests = 0
failed_tests = 0

def test(description, condition):
    global passed_tests, failed_tests
    if condition:
        print(f"  ✅ PASS: {description}")
        passed_tests += 1
    else:
        print(f"  ❌ FAIL: {description}")
        failed_tests += 1

# ─────────────────────────────────────────
# Test Basic Checks
# ─────────────────────────────────────────
print("\n=== Running Tests ===")
print("\n📋 Testing Basic Checks...")

# Length checks
status, _ = check_length("hi")
test("Short password detected correctly", status == False)

status, _ = check_length("Hello@123456")
test("Long password passes correctly", status == True)

# Uppercase checks
status, _ = check_uppercase("hello123")
test("Missing uppercase detected correctly", status == False)

status, _ = check_uppercase("Hello123")
test("Uppercase passes correctly", status == True)

# Lowercase checks
status, _ = check_lowercase("HELLO123")
test("Missing lowercase detected correctly", status == False)

status, _ = check_lowercase("Hello123")
test("Lowercase passes correctly", status == True)

# Number checks
status, _ = check_numbers("Hello@abc")
test("Missing number detected correctly", status == False)

status, _ = check_numbers("Hello123")
test("Number passes correctly", status == True)

# Symbol checks
status, _ = check_symbols("Hello123")
test("Missing symbol detected correctly", status == False)

status, _ = check_symbols("Hello@123")
test("Symbol passes correctly", status == True)

# ─────────────────────────────────────────
# Test Common Password Check
# ─────────────────────────────────────────
print("\n📋 Testing Common Password Check...")

status, _ = check_common_password("123456")
test("Common password '123456' detected", status == False)

status, _ = check_common_password("password")
test("Common password 'password' detected", status == False)

status, _ = check_common_password("X9#mK2@pLqR5")
test("Strong password passes common check", status == True)

# ─────────────────────────────────────────
# Test Entropy Check
# ─────────────────────────────────────────
print("\n📋 Testing Entropy Check...")

status, _ = check_entropy("123456")
test("Weak password scores low entropy", status == False)

status, _ = check_entropy("X9#mK2@pLqR5!99")
test("Strong password scores high entropy", status == True)

# ─────────────────────────────────────────
# Final Results
# ─────────────────────────────────────────
total = passed_tests + failed_tests
print(f"\n{'='*40}")
print(f"Total Tests  : {total}")
print(f"Passed       : {passed_tests} ✅")
print(f"Failed       : {failed_tests} ❌")
print(f"{'='*40}")

if failed_tests == 0:
    print("🎉 All tests passed! Your tool is working perfectly!")
else:
    print("⚠️  Some tests failed — check the issues above!")