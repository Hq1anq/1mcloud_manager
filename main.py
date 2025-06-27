import sys
from PySide6.QtWidgets import QApplication

from gui.table_window import TableWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWindow()
    sys.exit(app.exec())