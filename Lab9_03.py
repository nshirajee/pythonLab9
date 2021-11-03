
def _encrypt(content):
    ans = ""
    #unicode of character a
    a2 = ord('a')
    #loop through each character in sentence
    for character in content:
        #convert to unicode
        a1 = ord(character)
        # create new unicode
        b1 = a1 + 4;
        ans = ans + chr(b1)

    return ans

def _decrypt(content):
    ans = ""
    a2 = ord('a')
    for character in content:
        a1 = ord(character)
        b1 = a1 - 4;
        ans = ans + chr(b1)
    return ans


userInput = input("Enter text to encrypt:")

encryptedText = _encrypt(userInput)
print(encryptedText)
decryp = _decrypt(encryptedText)
print(decryp)
