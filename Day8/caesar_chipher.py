alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
the_text = input("Type your message:\n").lower()
the_shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted = ""

    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]

        encrypted += new_letter
    print(f"The encoded text is {encrypted}")


def decrypt(text, shift):
    decrypted = ""

    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decrypted += new_letter
    print(f"The encoded text is {decrypted}")


if direction == "encode":
    encrypt(the_text, the_shift)

elif direction == "decode":
    decrypt(the_text, the_shift)

else:
    print("Invalid Entry!")
