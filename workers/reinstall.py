import server_api
import pyperclip, time

from PySide6.QtCore import QRunnable, Signal, QObject
from PySide6.QtWidgets import QTableWidget

class Reinstall(QRunnable):
    
    class Signals(QObject):
        change_table = Signal(int, bool, str, str)  # row, success
        finished_log = Signal(str)
        
    def __init__(self, rows, custom_info: str, table):
        super().__init__()
        self.rows = rows
        self.custom_info = custom_info
        self.table: QTableWidget = table
        self.signals = self.Signals()

    def run(self):
        str_for_copy = ""
        for row in self.rows:
            item = self.table.item(row, 1)
            if not item:
                self.signals.change_table.emit(row, False, None, None)
                continue
            if self.custom_info:
                proxy_info = server_api.reinstall(sid=item.text(), custom_info=self.custom_info)
            else:
                proxy_info = server_api.reinstall(sid=item.text())
            if proxy_info:
                proxy_str = f"{proxy_info[0]}:{proxy_info[1]}:{proxy_info[2]}:{proxy_info[3]}"
                print(proxy_str)
                str_for_copy += proxy_str + "\n"
                self.signals.change_table.emit(row, True, None, f"{proxy_info[0]}:{proxy_info[1]}")
            else:
                print(f"❌{self.table.item(row, 2).text()}")
                self.signals.change_table.emit(row, False, None, None)
            time.sleep(2)
        pyperclip.copy(str_for_copy)
        self.signals.finished_log("Reinstall - DONE!")