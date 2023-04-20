'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def findsubstr(lst, target):
    c = 0
    for i in lst:
        c += i.lower().count(target.lower())
    return c
n = int (input())
lst = []
for i in range(n):
    s = input()
    lst.append(s)
target = input()
m = findsubstr(lst, target)
if m:
    print(m)
else:
    print("Target String not found")