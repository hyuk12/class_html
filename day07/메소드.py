class Book():
    def information(self, bookName, author, company, price, pages):
        self.bookName = bookName
        self.author = author
        self.company = company
        self.price = price
        self.pages = pages

    def bookInfo(self, information):
        self.information
        return print(information)


book_name = Book()
book1 = book_name.information("모모", "미하엘 엔데", "나무", "8500원", "367 페이지")
print(book1)
