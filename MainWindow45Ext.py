import functools
from PyQt6.QtWidgets import QPushButton
from Baitap45.ui.MainWindow45 import Ui_MainWindow

class MainWindow45Ext(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.books = []
        self.previous_button = None
        self.selected_index = -1

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.xuly_luu_sach)
        self.pushButtonRemove.clicked.connect(self.xuly_loaibo)
        self.pushButtonFilterYear.clicked.connect(self.loc_theo_nam)
        self.pushButtonSearchTitle.clicked.connect(self.tim_tieude)
        self.pushButtonSearchISBN.clicked.connect(self.tim_isbn)
        self.pushButtonFilterPublisher.clicked.connect(self.loc_publiser)

    def xuly_luu_sach(self):
        if not self.lineEditISBN.text() or not self.lineEditTitle.text():
            # Add a message box here to notify the user
            print("ISBN and Title are required!")
            return

        book = {
            "isbn": self.lineEditISBN.text(),
            "title": self.lineEditTitle.text(),
            "author": self.lineEditAuthor.text(),
            "year": self.lineEditYear.text(),
            "publisher": self.lineEditPublisher.text()
        }
        self.books.append(book)
        self.hienthi_sach_len_giaodien()

    def hienthi_sach_len_giaodien(self, books=None):
        # Default to displaying all books if no custom list is provided
        books = books if books is not None else self.books

        self.clearLayout(self.verticalBook)
        for i, book in enumerate(books):
            # Display book details in a single button
            book_button = QPushButton(f"ISBN: {book['isbn']}, {book['title']}, {book['year']}, {book['publisher']}")
            self.verticalBook.addWidget(book_button)
            book_button.clicked.connect(functools.partial(self.xem_chitiet, i))

    def xem_chitiet(self, i):
        book = self.books[i]
        self.lineEditISBN.setText(book["isbn"])
        self.lineEditTitle.setText(book["title"])
        self.lineEditAuthor.setText(book["author"])
        self.lineEditYear.setText(book["year"])
        self.lineEditPublisher.setText(book["publisher"])
        self.selected_index = i

    def xuly_loaibo(self):
        if self.selected_index == -1:
            print("No book selected to remove.")
            return
        self.books.pop(self.selected_index)
        self.selected_index = -1
        self.previous_button = None
        self.hienthi_sach_len_giaodien()

    def loc_theo_nam(self):
        year = self.lineEditYear.text()
        if not year:
            print("Please enter a year to filter.")
            return
        filtered_books = [book for book in self.books if book["year"] == year]
        self.hienthi_sach_len_giaodien(filtered_books)

    def tim_tieude(self):
        title = self.lineEditTitle.text().lower()
        if not title:
            print("Please enter a title to search.")
            return
        matched_books = [book for book in self.books if title in book["title"].lower()]
        self.hienthi_sach_len_giaodien(matched_books)

    def tim_isbn(self):
        isbn = self.lineEditISBN.text()
        if not isbn:
            print("Please enter an ISBN to search.")
            return
        matched_books = [book for book in self.books if book["isbn"] == isbn]
        self.hienthi_sach_len_giaodien(matched_books)

    def loc_publiser(self):
        publisher = self.lineEditPublisher.text().lower()
        if not publisher:
            print("Please enter a publisher to filter.")
            return
        filtered_books = [book for book in self.books if publisher in book["publisher"].lower()]
        self.hienthi_sach_len_giaodien(filtered_books)
