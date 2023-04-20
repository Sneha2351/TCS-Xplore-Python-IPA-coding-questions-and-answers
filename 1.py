'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def func(lst, v):
    for i in lst:
        if i == v:
            a = lst.index(i)
    return a
n = int(input())
lst = []
for i in range(n):
    s = input()
    lst.append(s)
v = input()
m = func(lst, v)
if m == None:
    print("No Record Found")
else:
    print(m)