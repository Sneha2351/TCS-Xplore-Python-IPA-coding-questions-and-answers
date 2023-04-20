'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
s = input()
space = 0
character = 0
for i in s:
    if i == " ":
        space += 1
    else:
        character += 1
print("No of spaces :",space ,"and characters :",character)