#Build a program that receives a full name and determines how many vowels and consonants it contains.
def VowelsConsonants(fName="Lestter Alphabeou Convowel"):
    vowels, consonants = 0,0
    for i in fName:
        if fName[fName.index(i)] in "aeiouAEIOU": vowels += 1
        else: consonants += 1
    return f'Your name has {vowels:\N{Sparkles}^10} vowels and {consonants:\N{Sparkles}^10}', vowels, consonants

print(VowelsConsonants()[0])