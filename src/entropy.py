from zxcvbn import zxcvbn

def check_entropy(password):
    result = zxcvbn(password)
    
    score = result['score']  # score is 0 to 4
    
    # Get crack time
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']
    
    # Get feedback
    feedback_list = result['feedback']['suggestions']
    warning = result['feedback']['warning']
    
    # Score label
    score_labels = {
        0: "❌ Very Weak",
        1: "🔴 Weak", 
        2: "🟡 Fair",
        3: "🟢 Strong",
        4: "💪 Very Strong"
    }
    
    label = score_labels[score]
    
    # Build feedback message
    feedback = warning if warning else (feedback_list[0] if feedback_list else "No suggestions")
    
    message = (
        f"\n🔐 Entropy Score: {score}/4 — {label}"
        f"\n⏱️  Estimated crack time: {crack_time}"
        f"\n💬 Feedback: {feedback}"
    )
    
    # Pass if score is 3 or above
    passed = score >= 3
    
    return passed, message