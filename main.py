"""EasyCrypt Text Encryptor/Decryptor: Encrypt, decrypt and generate a key. 

Operation given by user. If encryption or decryption, text and key given.
If generating key, key length given.
"""


import random



def clean_string(text: str) -> str:
    """Return a cleaned string 'text' with all symbols and non-letter
    characters removed.
    
    ASCII characters that are letters are 'clean'
    
    >>> clean_string('Hello World!')
    'Hello World'
    >>> clean_string('@#Good day Mr. Cho*+')
    'Good day Mr Cho'
    """

    clean = ''

    for ch in text:
        if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            clean += ch

    return clean



def group_by_five(text: str) -> str:
    """Return the letters in string 'text' in groups of 5.

    >>> group_by_five("IMAGINEBEINGBAD")
    IMAGI NEBEI NGBAD
    >>> group_by_five("HITHEREMRCHO")
    HITHE REMRC HO
    """
    
    grouped_text = ""
    
    # Range is offset to index by 1 because “letter” is needed to check multiples of 5.
    for letter in range(1, len(text) + 1):
        grouped_text += text[letter - 1]
        # Ensuring a space does not proceed the last group of 5.
        if letter % GROUP == 0 and letter != len(text):
            grouped_text += " "
    
    return grouped_text



def generate_letters(text: str) -> str:
    """Return string 'text' with the same random letter added to the end.

    The number of letters generated will be the number of letters needed to
    make the length of text a multiple of 5.

    >>> generate_letters("SPAMANDEGGS")
    SPAMANDEGGSYYYY
    >>> generate_letters("HELLOTHERE")
    HELLOTHERE
    """

    if len(text) % GROUP != 0:
        # Getting 5 subtracted by the remainder to get needed number of letters.
        num_letters = GROUP - (len(text) % GROUP)
        rand_letter = ALPHABET[random.randint(0, 25)]
        for i in range(num_letters):
            text += rand_letter

    return text

  

def generate_key(key_num: int) -> str:
    """Return a randomly generated uppercase string 'key' using length key_num.

    >>> generate_key(9)
    RQYDTPHWV
    >>> generate_key(3)
    ABC
    """

    key = ""
    for i in range(key_num):
        letter = ALPHABET[random.randint(0, 25)]
        key += letter
    
    return key



def encrypt_decrypt(operation: str, text: str, key: str) -> str:
    """ Return encrypted text if operation is 1, return decrypted text 
    if operation is 2.

    Both encryption and decryption uses key to change text. 
    """
    
    # When sum or difference is out of range, shift by 64 in ASCII.
    # When sum or difference is out of range, where a shift of 64 
    #   will not be in range of ASCII letters, shift by 90
    SHIFT_LESS = 64
    SHIFT_MORE = 90
    # in operation 1: sum of 154 is highest it can be for SHIFT_LESS to 
    #keep in A-Z
    ENCRYPT_SWITCH = 154
    # in operation 2: difference of 0 is highest it can be for 
    #SHIFT_MORE to keep in A-Z
    DECRYPT_SWITCH = 0

    temporary = ""
    new_text = ""
    i = 0

    if operation == "1":
         
        while i < len(text):
            # Goes through key from start to end. Repeats this process
            # until text is done
            for j in range(len(key)):
                # Adding ASCII values of one letter of 'text' to matching 
                # letter of 'key' 
                temporary = ord(text[i]) + ord(key[j])
                
                if temporary <= ENCRYPT_SWITCH:
                    temporary -= SHIFT_LESS
                else:
                    temporary -= SHIFT_MORE
                    
                temporary = chr(temporary)
                new_text += temporary
          
                i += 1
                
                # Before looping again, check that i doesn't go over possible 
                #   index of 'text'
                if i == len(text):
                    break

    if operation == "2":
      
        while i < len(text):
          
            for j in range(len(key)):
                # Rearrange formula: encrypted text = plaintext + key 
                temporary = ord(text[i]) - ord(key[j])
                
                if temporary <= DECRYPT_SWITCH:
                  temporary += SHIFT_MORE
                else:
                  temporary += SHIFT_LESS
                  
                temporary = chr(temporary)
                new_text += temporary
                
                i += 1
                
                if i == len(text):
                    break
    
    new_text = group_by_five(new_text)
    
    return new_text



if __name__ == '__main__':
    """The main program."""

    print("""----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------""")

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    GROUP = 5

    while True:
        operation = input("""\nPlease choose from one of the following menu options:
1. Encrypt plaintext.
2. Decrypt ciphertext.
3. Generate key.
4. Exit

> """)
    
        print()           
        if operation == "1" or operation == "2":
            # Filler words in output vary based on operation used
            operation_type = "encrypt"
            plaintext_ciphertext = "plaintext"
            encryption_decryption = "encryption"
            text_status = "encrypted"
                
            if operation == "2":
                operation_type = "decrypt"
                plaintext_ciphertext = "ciphertext"
                encryption_decryption = "decryption"
                text_status = "decrypted"
            
            
            text = input("Please enter text to {}: ".format(operation_type))
            text = clean_string(text).upper()
            group_text = group_by_five(text)

            print("This is the {}:".format(plaintext_ciphertext), group_text, "\n")
            text = generate_letters(text)
            
            key = input("A key is any string of letters(1-1000 chars): ")
            key = clean_string(key).upper()
            
            while len(key) == 0 or len(key) > 1000:
                print("invalid input")
                key = input("A key is any string of letters(1-1000 chars): ")
                key = clean_string(key).upper()

            print("Using {} key:".format(encryption_decryption), key, "\n")
            
            changed_text = encrypt_decrypt(operation, text, key)
            print("Your message has been {}: \n{}".format(text_status, changed_text))

   
        elif operation == "3":
            print("Generate an encryption key comprised of random characters (max. 1000).")
            while True:
                try:
                    key_num = int(input("Enter the desired length of key (1-1000): "))
                    if 1 <= key_num <= 1000:
                        break
                    else:
                        print("invalid")
                except ValueError:
                    print("not an integer")

            key = generate_key(key_num)
            print("Your new encryption key:\n{}".format(key))

        elif operation == "4":
            print("Thank you for using EasyCrypt. Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")
            continue
