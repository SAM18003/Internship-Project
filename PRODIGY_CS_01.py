#Function to encrypt the string
def encrypt(text,shift):
    encrypted_text=""                                # Initialize an empty string to hold the encrypted text
    for char in text:
        if char.isalpha():
                shift_amount=65 if char.isupper() else 97               # Determine the ASCII offset for upper or lower case
                encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)  # Encrypt the character and add it to the result
        else:
            encrypted_text+=char
    return encrypted_text     
          
#Function to decrypt the string
def decrypt(text,shift):
    decrypt_text=""                             # Initialize an empty string to hold the decrypted text
    for char in text:                      
        if char.isalpha():
            shift_amount=65 if char.isupper() else 97
            decrypt_text+=chr((ord(char)-shift-shift_amount)%26+shift_amount)   # Decrypt the character and add it to the result
        else:
            decrypt_text+=char
    return decrypt_text

# Main function to execute the Caesar Cipher encryption and decryption.
def main():
    message=input("Enter your message:")
    option=input("Enter your choice Encrypt(E) or Decrypt(D):")
    shift=int(input("Enter the shift value:"))

    if option=='E':
        result=encrypt(message,shift)
        print("The Encrypted message is:",result)
    elif option=='D':
        result=decrypt(message,shift)
        print("The Decrypted message is",result)
    else:
        print("Invalid choice!Please select the given options")

if __name__=="__main__":
    main()