from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QCompleter, QVBoxLayout, QWidget

class SearchBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Bar with Suggestions")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Type your search query...")
        layout.addWidget(self.search_input)

        # Create a list of suggestions (you can fetch this dynamically from a server or other sources)
        suggestion_list = ["apple", "banana", "cherry", "grape", "orange", "pear", "pineapple"]

        completer = QCompleter(suggestion_list, self.search_input)
        self.search_input.setCompleter(completer)

        self.central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = SearchBar()
    window.show()
    app.exec_()