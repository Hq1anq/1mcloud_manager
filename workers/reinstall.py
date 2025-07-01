import server_api
import pyperclip

from PySide6.QtCore import QRunnable, Signal, QObject
from PySide6.QtWidgets import QTableWidget

class Reinstall(QRunnable):
    
    class Signals(QObject):
        change_table = Signal(int, bool)  # row, success
        
    def __init__(self, rows, table):
        super().__init__()
        self.rows = rows
        self.table: QTableWidget = table
        self.signals = self.Signals()

    def run(self):
        str_for_copy = ""
        for row in self.rows:
            item = self.table.item(row, 1)
            if not item:
                self.signals.change_table.emit(row, False)
                continue
            proxy_info = server_api.reinstall(item.text())
            if proxy_info is not None:
                print(proxy_info)
                str_for_copy += proxy_info + "\n"
                self.signals.change_table.emit(row, True)
            else:
                print(f"❌{self.table.item(row, 2).text()}")
                self.signals.change_table.emit(row, False)
        pyperclip.copy(str_for_copy)