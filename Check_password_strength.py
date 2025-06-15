import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Lowercase and Uppercase check
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 1
    else:
        remarks += "Use both uppercase and lowercase letters.\n"

    # Digits check
    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks += "Include at least one digit.\n"

    # Special character check
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "Include at least one special character (!@#$%^&* etc.).\n"

    # Strength output
    if strength == 4:
        return "Strong password!"
    elif strength == 3:
        return "Moderate password. Consider improving:\n" + remarks
    else:
        return "Weak password. Suggestions:\n" + remarks

# Take input from user
user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print("\nResult:", result)