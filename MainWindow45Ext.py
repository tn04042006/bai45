import functools

from PyQt6.QtWidgets import QPushButton

from Baitap45.ui.MainWindow45 import Ui_MainWindow


class MainWindow45Ext(Ui_MainWindow):
    def __init__(self):
        self.books=[]
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
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
        book={"isbn":self.lineEditISBN.text(),
              "title":self.lineEditTitle.text(),
              "author":self.lineEditAuthor.text(),
              "year":self.lineEditYear.text(),
              "publisher":self.lineEditPublisher.text()}
        self.books.append(book)
        self.hienthi_sach_len_giaodien()

    def hienthi_sach_len_giaodien(self):
        #xoa toan bo sach trong layout di de nap lai
        self.clearLayout(self.verticalBook)
        for i in range(len(self.books)):
            book=self.books[i]
            book_button=QPushButton(text=book["title"])
            self.verticalBook.addWidget(book_button)
            book_button.clicked.connect(functools.partial(self.xem_chitiet,i))

    def xem_chitiet(self,i):
        book=self.books[i]
        self.lineEditISBN.setText(book,["isbn"])
        self.lineEditPublisher.setText(book,["publiser"])
        self.lineEditYear.setText(book,["year"])
        self.lineEditAuthor.setText(book,["author"])
        self.lineEditTitle.setText(book,["year"])
    def xuly_loaibo(self):

    def loc_theo_nam(self):

    def tim_tieude(self):

    def tim_isbn(self):

    def loc_publiser(self):

