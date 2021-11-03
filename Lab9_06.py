
#function to calculate number of vowels and consonants pass string as parameter
def checkVowel(content):
    #list of vowels
    vowels = ["a", "e", "i", "o", "u"]
    #initialize total variables
    totalVowels = 0
    totalConsonants = 0

    #loop through each character of the sentence
    for character in content:
        # in characrter is in vowels list increment number
        if character in vowels:
            totalVowels = totalVowels + 1
        #else if char is alpha, not dot or any other spcecial increment consonant total
        elif character.isalpha():
            totalConsonants = totalConsonants + 1

    #print total vowels and total consonants
    print("Num of vowels: ", totalVowels)
    print("Num of Consonants: ", totalConsonants)

userInput = input("Enter an English sentenc: ")
checkVowel(userInput)





