class Book:
    def __init__(self,title = None, author = None, availability = None, price = None):
        self.title = title
        self.author = author
        
        self.availability = availability
        self.price =price


    def royxat(self):
        a = [self.title, self.author, self.availability, self.price]
        if "" in a:
            return 1
        else:
            return 0

muallif = input("Iltimos kitobning muallifini kiriting!\n>>> ")
kitob = input("Iltimos kitobning nomini kiriting!\n>>> ")
# isb = input("Iltimos kitobning isbn raqamini kiriting!\n>>> ")
dona = input("Iltimos nechta kitobligini kiriting!\n>>> ")
narx = input("Iltimos kitobning narxini kiriting!\n>>> ")

book = Book(muallif,kitob,dona,narx)



if book.royxat() == 1:
    book.royxat()
    print("Iltimos ro'yxatni to'ldiring!")
    

elif book.royxat() == 0:
    a = open("royxat.csv","a")
    a.write(f"\n{muallif}, {kitob}, {dona}dona,  {narx}ming so'm")
    
