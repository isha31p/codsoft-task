import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    characters = lowercase
    if use_uppercase:
        characters += uppercase
    if use_numbers:
        characters += digits
    if use_special_chars:
        characters += special_chars
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator App..")

    while True:
        try:
            length = int(input("Enter length of the password: "))
            if length < 6:  
                print("Password length should contain at least 6 character.")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Your generated password is: {password}")
          
if __name__ == "__main__":
    main()
