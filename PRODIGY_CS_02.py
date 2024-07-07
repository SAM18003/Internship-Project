def encrypt_image(path, key):
    try:
        # Open the file for reading purpose
        with open(path, 'rb') as fin:
            # Storing image data in variable "image"
            image = fin.read()

        # Converting image into byte array to perform encryption easily on numeric data
        image = bytearray(image)

        # Performing XOR operation on each value of byte array
        for index, value in enumerate(image):
            image[index] = value ^ key

        # Opening file for writing purpose
        with open(path, 'wb') as fin:
            # Writing encrypted data in image
            fin.write(image)

        print('Encryption Done...')
    
    except Exception as e:
        print('Error caught during encryption: ', e.__class__.__name__)


def decrypt_image(path, key):
    try:
        # Open the file for reading purpose
        with open(path, 'rb') as fin:
            # Storing image data in variable "image"
            image = fin.read()

        # Converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)

        # Performing XOR operation on each value of byte array
        for index, value in enumerate(image):
            image[index] = value ^ key

        # Opening file for writing purpose
        with open(path, 'wb') as fin:
            # Writing decrypted data in image
            fin.write(image)

        print('Decryption Done...')
    
    except Exception as e:
        print('Error caught during decryption: ', e.__class__.__name__)


def main():
    action = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    path = input(r'Enter path of Image: ')
    key = int(input('Enter Key for encryption/decryption of Image: '))

    if action == 'e':
        encrypt_image(path, key)
    elif action == 'd':
        decrypt_image(path, key)
    else:
        print("Invalid action. Please enter 'e' to encrypt or 'd' to decrypt.")


if __name__ == "__main__":
    main()
