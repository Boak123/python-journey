# task: check if a password reach the minimum length of 8 characters

# def check_password_length(password):
#     if len(password) < 8:
#         return "Password is too short. It must be at least 8 characters long."
#     else:
#         return "Password is valid."
    
# print(check_password_length("mypassword"))  # Example usage

# #Task: check if a password as a valid pattern

# def is_valid_password(password):
#     if len(password) < 8:
#         return "Password is too short. It must be at least 8 characters long."
#     if not any(char.isupper() for char in password):
#         return "Password must contain at least one uppercase letter."
#     if not any(char.islower() for char in password):
#         return "Password must contain at least one lowercase letter."
#     if not any(char.isdigit() for char in password):
#         return "Password must contain at least one digit."
#     if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
#         return "Password must contain at least one special character."
    
#     return "Password is valid."

# print(is_valid_password("MyPassword123!"))  # Example usage

def is_valid_email(email):
    return"@" in email and "." in email 
