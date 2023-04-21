'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def validateScore(vld_num):
    if 0 < vld_num <= 100:
        return True
    else:
        return False
        
def findValidScores(lst):
    lst2 = []
    for i in lst:
        if validateScore(i) == True:
            lst2.append(i)
    return lst2
        
n = int(input())
lst = []
for i in range(n):
    score = int(input())
    lst.append(score)
x = findValidScores(lst)
if x == []:
    print("No valid score found.")
else:
    print("Valid Scores =",x)