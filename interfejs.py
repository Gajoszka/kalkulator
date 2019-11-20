#obsluga m.in polskich znaków
from __future__ import unicode_literals
# podstawowa klasa wszystkich elementów interfejsu graficznego
from PyQt5.QtWidgets import QApplication, QWidget
# importy do tworzenia widżetów
from PyQt5.QtGui import QIcon
# QLabel - tworzenie etykiet
# QGridLayout - rozmieszczanie etykiet w układzie tabelarycznym
from PyQt5.QtWidgets import QLabel, QGridLayout
# QLineEdit - 1 liniowe pole edycyjne
# QPushButton - przycisk
# QHBoxLayout - układ horyzontalny
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout


# kalkulator - wygląd okna aplikacji
class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    # tworzenie GUI
    def interfejs(self):

        etykieta1 = QLabel("Liczba 1: ", self)
        etykieta2 = QLabel("Liczba 2: ", self)
        etykieta3 = QLabel("Wynik: ", self)

        układT = QGridLayout()
        układT.addWidget(etykieta1, 0, 0)
        układT.addWidget(etykieta2, 0, 1)
        układT.addWidget(etykieta3, 0, 2)

        self.liczba1Edit = QLineEdit()
        self.liczba2Edit = QLineEdit()
        self.wynikEdit = QLineEdit()

        self.wynikEdit.readonly = True # readonly - tylko odczyt
        self.wynikEdit.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...') # setToolTip - ustawia podpowiedź

        układT.addWidget(self.liczba1Edit, 1, 0)
        układT.addWidget(self.liczba1Edit, 1, 1)
        układT.addWidget(self.liczba1Edit, 1, 2)

        # przyciski
        dodajP = QPushButton("Dodaj", self)
        odejmijP = QPushButton("Odejmij", self)
        pomnóżP = QPushButton("Pomnóż", self)
        podzielP = QPushButton("Podziel", self)
        koniecP = QPushButton("Zakończ", self)
        koniecP.resize(koniecP.sizeHint()) # podpowiada rozmiar obiektu

        # układ horyzontalny
        układH = QHBoxLayout()
        układH.addWidget(dodajP)
        układH.addWidget(odejmijP)
        układH.addWidget(pomnóżP)
        układH.addWidget(podzielP)
        układH.addWidget(koniecP)

        # liczby kolejno - wiersz, kolumna (tj. komórka do której wstawiamy obiekt i ilość wierszy i kolumn, które chcemy wykorzystać
        układT.addLayout(układH, 2, 0, 1, 3)
        układT.addWidget(koniecP, 3, 0, 1, 3)

        # przypisanie ukladu do okna
        self.setLayout(układT)


        self.setGeometry(20, 20, 300, 100) # szerokość, wysokość okna
        self.setWindowIcon(QIcon('kalkulator.png')) # tytuł w pasku tytułowym
        self.setWindowTitle("Prosty kalkulator") # tytuł
        self.show() # wyśwwietlenie okna


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv) # obiekt reprezentujący aplikację
    okno = Kalkulator() # obiekt reprezentujący okno aplikacji
    sys.exit(app.exec_()) # rozpoczęcie obsługi zdarzeń