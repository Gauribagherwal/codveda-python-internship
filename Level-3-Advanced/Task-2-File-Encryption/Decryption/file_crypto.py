from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken


KEY_FILE = Path("secret.key")


def generate_key():
    """Generate and save a new encryption key."""
    if not KEY_FILE.exists():
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        print("New encryption key created: secret.key")
    else:
        print("Encryption key already exists: secret.key")


def load_key():
    """Load the existing encryption key."""
    if not KEY_FILE.exists():
        print("Error: secret.key not found.")
        print("Please run the program once to create the key.")
        return None

    return KEY_FILE.read_bytes()


def encrypt_file(filename):
    """Encrypt the selected file."""
    key = load_key()

    if key is None:
        return

    input_file = Path(filename)

    if not input_file.exists():
        print("Error: File not found.")
        return

    encrypted_file = Path(str(input_file) + ".encrypted")

    try:
        fernet = Fernet(key)

        data = input_file.read_bytes()
        encrypted_data = fernet.encrypt(data)

        encrypted_file.write_bytes(encrypted_data)

        print("File encrypted successfully.")
        print(f"Encrypted file: {encrypted_file}")

    except Exception as error:
        print("Encryption error:", error)


def decrypt_file(filename):
    """Decrypt the selected encrypted file."""
    key = load_key()

    if key is None:
        return

    encrypted_file = Path(filename)

    if not encrypted_file.exists():
        print("Error: Encrypted file not found.")
        return

    if encrypted_file.suffix != ".encrypted":
        print("Error: Please select a .encrypted file.")
        return

    original_file = Path(str(encrypted_file)[:-10])

    try:
        fernet = Fernet(key)

        encrypted_data = encrypted_file.read_bytes()
        decrypted_data = fernet.decrypt(encrypted_data)

        original_file.write_bytes(decrypted_data)

        print("File decrypted successfully.")
        print(f"Decrypted file: {original_file}")

    except InvalidToken:
        print("Error: Invalid encryption key or corrupted file.")

    except Exception as error:
        print("Decryption error:", error)


def main():
    print("==============================")
    print("   FILE ENCRYPTION TOOL")
    print("==============================")

    generate_key()

    print("\n1. Encrypt file")
    print("2. Decrypt file")

    choice = input("Enter your choice (1/2): ").strip()

    filename = input("Enter file name: ").strip()

    if choice == "1":
        encrypt_file(filename)

    elif choice == "2":
        decrypt_file(filename)

    else:
        print("Error: Please enter 1 or 2.")


if __name__ == "__main__":
    main()