'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class Book:
    def __init__(self, pages, price, author, idd, title):
        self.pages = pages
        self.price = price
        self.author = author
        self.idd = idd
        self.title = title
    
class BookStore:
    def __init__(self, bookStoreName, BookList):
        self.bookStoreName = bookStoreName
        self.BookList = BookList
    
    def findMinimumBookByid(self):
        lst2 = []
        for i in BookList:
            lst2.append(i.idd)
        if lst2 == None:
            print("none")
        else:
            for i in BookList:
                if i.idd == min(lst2):
                    print(i.pages)
                    print(i.price)
                    print(i.author)
                    print(i.idd)
                    print(i.title)
        
    def sortBookByid(self):
        lst = []
        for i in BookList:
            lst.append(i.idd)
        if lst == []:
            print("none")
        else:
            lst.sort()
            for i in lst:
                print(i)

n = int(input())
BookList = []
for i in range(n):
    pages = int(input())
    price = int(input())
    author = input()
    idd = int(input())
    title = input()
    BookList.append(Book(pages, price, author, idd, title))
    
a = BookStore("x", BookList)
a.findMinimumBookByid()
a.sortBookByid()