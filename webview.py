import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QWidget, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a tab widget to hold the web views
        self.tabs = QTabWidget()

        # Create a horizontal layout to hold the back, forward, and reload buttons
        button_layout = QHBoxLayout()
        self.back_button = QPushButton("Back")
        self.forward_button = QPushButton("Forward")
        self.reload_button = QPushButton("Reload")
        self.experimental_button = QPushButton("Experimental")
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.reload_button)
        button_layout.addWidget(self.experimental_button)

        # Create a search bar with a search button
        search_layout = QHBoxLayout()
        self.search_edit = QLineEdit()
        self.search_button = QPushButton("Search")
        search_layout.addWidget(self.search_edit)
        search_layout.addWidget(self.search_button)

        # Create a vertical layout to hold the top bar, search bar, and tab widget
        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(search_layout)  # Add the search bar layout
        main_layout.addWidget(self.tabs)

        # Create a central widget to hold the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect the back, forward, and reload buttons to their respective functions
        self.back_button.clicked.connect(self.go_back)
        self.forward_button.clicked.connect(self.go_forward)
        self.reload_button.clicked.connect(self.reload)
        self.experimental_button.clicked.connect(self.experimental)

        # Connect the search button to the search function
        self.search_button.clicked.connect(self.search)

        # Add a tab with the Google homepage
        self.add_tab("https://www.google.com")

    def add_tab(self, url):
        # Create a web view and a page to hold it
        view = QWebEngineView()
        page = QWebEnginePage(view)

        # Set the URL and load it
        view.setUrl(QUrl(url))

        # Add the view to the tab widget
        self.tabs.addTab(view, "Jake scrubbed the code!")

    def go_back(self):
        # Get the current tab and its web view
        tab = self.tabs.currentWidget()
        view = tab.page().view()

        # Go back in the history
        view.back()

    def go_forward(self):
        # Get the current tab and its web view
        tab = self.tabs.currentWidget()
        view = tab.page().view()

        # Go forward in the history
        view.forward()

    def reload(self):
        # Get the current tab and reload it
        current_tab = self.tabs.currentWidget()
        current_tab.reload()

    def search(self):
        # Get the search query from the search edit widget
        query = self.search_edit.text()

        # Construct the search URL
        url = "https://www.google.com/search?q=" + query

        # Get the current tab and load the search URL
        current_tab = self.tabs.currentWidget()
        current_tab.setUrl(QUrl(url))

    def experimental(self):
        # Get the current tab
        tab = self.tabs.currentWidget()

        # Set the URL of the current tab to experimental
        tab.setUrl(QUrl("http://localhost:7878"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("AIxRetr0")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
