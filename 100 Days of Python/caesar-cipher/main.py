alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decode:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

'''
Create a function called 'encrypt' that shifts each letter of 'text'
forwards in the alphabet by the shift amount and print the encrypted text.
'''

def caesar(direction, text, shift):
    message = list(text.strip())
    new_message = []
    # based on letter location create message with shifted values
    for letter in message:
        position = int(alphabet.index(letter))
        if direction == 'encode':
            new_position = position + shift
        elif direction == 'decode':
            new_position = position - shift
        new_message.append(alphabet[new_position])
    print(new_message)

caesar(direction, text, shift)