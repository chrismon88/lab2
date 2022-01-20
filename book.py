class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
       
        if title in (self.books):
            print("Book already entered!")
        else:
            self.books.append(title)

    def __str__(self):
        if self.books:
            book_list = ", ".join(self.books)
        else:
            book_list = "No books published"
        return f"Name: {self.name} Books Published: {book_list}"

def main():
    sweigart = Author("Al Sweigart")
    sweigart.publish("Automate the boring stuff with python")
    sweigart.publish("Invent with python")

    print(sweigart)


    chris = Author("Chris")
    print(chris)

main()