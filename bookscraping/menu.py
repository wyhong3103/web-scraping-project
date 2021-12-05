from requests.api import get
from app import get_books

def best_books(books):
    for i in sorted(books,key = lambda x:(x.rating*-1,x.price)):
        print(f"{i}\n")

def cheap_book(books):
    for i in sorted(books,key = lambda x:x.price):
        print(f"{i}\n")


function_dic = {
    "b" : best_books,
    "c" : cheap_book
}

def menu():
    page = 1
    options = input(f"\n--------Book Scraper 1.0--------\nCurrent Page: {page}/{get_books(page)[1]}\n\n-Enter b to view the books by its rating\n-Enter c to view the books by its price\n-Enter p to change page\n-Enter n to change to next page\n-Enter q to quit\n-->")
    while options != "q":
        if options == "p":
            page = int(input("To Page: "))
            if page > 50:
                print("You have reached the limit!")
                continue
        elif options == "n":
            if page == 50:
                print("You have reached the limit!")
            else:
                page += 1
        else:
            function_dic[options](get_books(page)[0])
        options = input(f"\n--------Book Scraper 1.0--------\nCurrent Page: {page}/{get_books(page)[1]}\n\n-Enter b to view the books by its rating\n-Enter c to view the books by its price\n-Enter p to change page\n-Enter n to change to next page\n-Enter q to quit\n")
menu()