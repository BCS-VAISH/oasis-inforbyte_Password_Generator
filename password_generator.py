import random as r
import string as str


def generate_password(length, uppercase, digits, special_chars):

    lowercase_chars = str.ascii_lowercase
    uppercase_chars = str.ascii_uppercase if uppercase else ''
    digit_chars = str.digits if digits else ''
    special_chars = str.punctuation if special_chars else ''


    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    if not all_chars:
        print("At least one character type must be selected")

    pwd= ''.join(r.choice(all_chars) for _ in range(length))
    return pwd


def main():
    print("Password Generator....!!!\n")

    try:
        length = int(input("Enter  length of password (positive integer): "))
        if length <= 0:
            print("Length must be a positive integer")

        uppercase = input("uppercase letters? (y/n): ").strip().lower() == 'y'
        digits = input("digits? (y/n): ").strip().lower() == 'y'
        special_chars = input("special characters? (y/n): ").strip().lower() == 'y'


        pwd = generate_password(length,uppercase,digits,special_chars)
        print(f"Generated Password: {pwd}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
