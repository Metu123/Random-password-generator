import random
import string
import os

def generate_password():
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if length <= 0:
        print("Password length must be positive.")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}")

    dir_path = input("Enter the directory to save the password (e.g., /path/to/folder): ").strip()
    if not os.path.isdir(dir_path):
        print("Invalid directory path.")
        return

    output_path = os.path.join(dir_path, "generated_password.txt")
    with open(output_path, "w") as file:
        file.write(f"Generated Password: {password}\n")

    print(f"Password saved at: {output_path}")

if __name__ == "__main__":
    generate_password()