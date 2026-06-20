import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password length should be at least 4.")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

            choice = input("\nGenerate another password? (y/n): ")

            if choice.lower() != 'y':
                print("\nThank you for using Password Generator!")
                break

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
