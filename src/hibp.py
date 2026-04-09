import hashlib
import requests

def check_hibp(password):
    try:
        # Step 1 - Hash the password using SHA1
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        
        # Step 2 - Split into first 5 chars and the rest
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]
        
        # Step 3 - Send only the first 5 chars to the API
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=5)
        
        # Step 4 - Check if our suffix exists in the response
        hashes = response.text.splitlines()
        
        for line in hashes:
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return False, f"❌ This password was found in {int(count):,} data breaches!\n   Change it immediately!"
        
        return True, "✅ This password was NOT found in any known data breach!"
    
    except requests.exceptions.ConnectionError:
        return False, "⚠️  No internet connection - breach check skipped"
    
    except requests.exceptions.Timeout:
        return False, "⚠️  Request timed out - breach check skipped"
    
    except Exception as e:
        return False, f"⚠️  Breach check failed: {str(e)}"