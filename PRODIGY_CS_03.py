import re

def password_strength(password):
    # Criteria check
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_character_criteria = bool(re.search(r'[\W_]', password))

    # Password strength check
    strength_score = sum([length_criteria,
                          uppercase_criteria,
                          lowercase_criteria,
                          number_criteria,
                          special_character_criteria
                          ])

    # Determine strength
    if strength_score == 5:
        strength = "The password is Very Strong"
    elif strength_score == 4:
        strength = "The password is Strong"
    elif strength_score == 3:
        strength = "The password is Moderate"
    elif strength_score == 2:
        strength = "The password is Weak"
    else:
        strength = "The password is Very Weak"

    feedback = {
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "number_criteria": number_criteria,
        "special_character_criteria": special_character_criteria,
        "strength": strength
    }
    return feedback

def provide_feedback(feedback):
    print("Password Strength:", feedback['strength'])

    missing_criteria = []

    if not feedback['length_criteria']:
        missing_criteria.append("Increase the length of your password to at least 8 characters.")
    if not feedback['uppercase_criteria']:
        missing_criteria.append("Include at least one uppercase letter.")
    if not feedback['number_criteria']:
        missing_criteria.append("Include some numbers.")
    if not feedback['special_character_criteria']:
        missing_criteria.append("Include some special characters (e.g., !, @, #, $, etc.).")

    if missing_criteria:
        print("\nSuggestions to improve your password:")
        for suggestion in missing_criteria:
            print(" -", suggestion)
    else:
        print("\nYour password meets all the necessary criteria.")

# Example usage
password = input("Enter a password: ")
feedback = password_strength(password)
provide_feedback(feedback)
