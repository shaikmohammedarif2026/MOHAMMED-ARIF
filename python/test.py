
# class Book:
#     total_books = 0
#     def __init__(self,name,author):
#         self.name = name
#         self.author = author
#         Book.total_books +=1
# book1 = Book("var","Don")
# book2 = Book("python","Jhon")
# book3 = Book("ML","Arif")
# book4 = Book("Java","Sam")
# book5 = Book("Data","Lisa")
# print("Total books created:",
# Book.total_books)

class Bank:
    bank_name = "SBI"
    def __init__(self,acc_no,pin):
        self.acc_no = acc_no
        self.pin = pin
a1 = Bank(213,111)
a2 = Bank(123,231)
a3= Bank(213,1213)
print(Bank.bank_name, a1.acc_no,a1.pin)
print(Bank.bank_name, a2.acc_no,a2.pin)
print(Bank.bank_name, a3.acc_no,a3.pin)