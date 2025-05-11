alphabets = [ chr(i) for i in range(ord('a'),ord('z')+1)]



print(alphabets)

def encrypt(text, shift):
    result = ""
    for i in text:
        if i not in alphabets:
            result+=i
        else:
            index = alphabets.index(i)
            if (index+shift) >= 26:
                 m =  (index+shift)%26
                 result += alphabets[m]
            else:
                result += alphabets[(index+shift)]
    return result

def decrypt(text,shift):
    result = ""
    for i in text:
        if i not in alphabets:
            result+=i
        else:
            index = alphabets.index(i)
            if index-shift < 0:
                m =  (index - shift) % 26
                result += alphabets[m ]
            else:
                result += alphabets[index-shift]
    return result

continue_game = 'yes'


while continue_game == 'yes':
    cipher = input("Type 'encode' to encrypt or 'decode' to decrypt : ").lower()
    while cipher == 'encode' or  cipher == 'decode':
        user_message = input("Type your message : ")
        shift_number = int(input("Type your shift number : "))

        if cipher == 'encode':
            result = encrypt(user_message,shift_number)
            print(f"Here is encrypted message {result}")
        else:
            result = decrypt(user_message,shift_number)
            print(f"Here is decrypted message {result}")

        continue_game = input("Type 'yes' if you want to go again or 'No' to stop : ")

