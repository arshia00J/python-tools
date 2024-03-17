import random
import string
import datetime
from termcolor import colored


def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result


def binary_to_text(binary_str):
    binary_list = binary_str.split()
    text_result = ''.join(chr(int(binary, 2)) for binary in binary_list)
    return text_result


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def timestamp_to_real_time(timestamp):
    try:
        real_time = datetime.datetime.fromtimestamp(timestamp)
        formatted_time = real_time.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time
    except ValueError:
        return "Invalid timestamp"


def main():
    while True:
        print(colored("Tools Menu", 'blue'))
        print("1. " + colored("Text to Binary", 'green'))
        print("2. " + colored("Binary to Text", 'green'))
        print("3. " + colored("Password Generator", 'green'))
        print("4. " + colored("Timestamp to Real Time", 'green'))
        print("5. " + colored("Quit", 'red'))

        choice = input(colored("Enter your choice (1/2/3/4/5): ", 'yellow'))

        if choice == "1":
            text_input = input(
                "Enter the text you want to convert to binary: ")
            binary_output = text_to_binary(text_input)
            print("Binary representation:", colored(binary_output, 'cyan'))

        elif choice == "2":
            binary_input = input(
                "Enter the binary you want to convert to text (separate bytes with spaces): ")
            text_output = binary_to_text(binary_input)
            print("Text representation:", colored(text_output, 'cyan'))

        elif choice == "3":
            try:
                length = int(input("Enter the desired password length: "))
                if length < 1:
                    print("Please enter a positive integer greater than 0.")
                else:
                    password = generate_password(length)
                    print("Generated password:", colored(password, 'green'))
            except ValueError:
                print("Invalid input. Please enter a valid positive integer.")

        elif choice == "4":
            try:
                timestamp = int(input("Enter a Unix timestamp: "))
                real_time = timestamp_to_real_time(timestamp)
                print("Converted time:", colored(real_time, 'cyan'))
            except ValueError:
                print("Invalid input. Please enter a valid Unix timestamp.")

        elif choice == "5":
            print(colored("Goodbye!", 'red'))
            break

        else:
            print(colored("Invalid choice. Please enter 1, 2, 3, 4, or 5.", 'red'))


if __name__ == "__main__":
    main()
