'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
s = input()
vowel = 0
consonant = 0
vwl = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in s:
    if i.isalpha() == True:
        if i in vwl:
            vowel += 1
        else:
            consonant += 1
print("Vowels count -",vowel)
print("Consonants count -",consonant)