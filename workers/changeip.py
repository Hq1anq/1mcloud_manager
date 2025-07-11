import server_api
import pyperclip, time

from PySide6.QtCore import QRunnable, Signal, QObject
from PySide6.QtWidgets import QTableWidget

class ChangeIP(QRunnable):
    
    class Signals(QObject):
        change_table = Signal(int, bool, str, str, str, bool)  # row, success, note, ip_port, status, change_ip
        finished_log = Signal(str)

    def __init__(self, rows, custom_info: str, table):
        super().__init__()
        self.rows = rows
        self.custom_info = custom_info
        self.table: QTableWidget = table
        self.signals = self.Signals()

    def set_row(self, row: int, success: bool, ip_port: str):
        if success:
            self.signals.change_table.emit(row, success, None, ip_port, "Running", True)
        else:
            self.signals.change_table.emit(row, success, None, ip_port, None, False)
        
    def run(self):
        str_for_copy = ""
        for row in self.rows:
            item = self.table.item(row, 2)
            if not item:
                self.set_row(row, False, None)
                continue
            if self.custom_info:
                proxy_info = server_api.changeip(ip=item.text().split(":")[0], custom_info=self.custom_info)
            else:
                proxy_info = server_api.changeip(ip=item.text().split(":")[0])
            if proxy_info:
                proxy_str = f"{proxy_info[0]}:{proxy_info[1]}:{proxy_info[2]}:{proxy_info[3]}"
                print(proxy_str)
                str_for_copy += proxy_str + "\n"
                self.set_row(row, True, f"{proxy_info[0]}:{proxy_info[1]}")
            else:
                print(f"❌{self.table.item(row, 2).text()}")
                self.set_row(row, False, None)
            time.sleep(2)
        pyperclip.copy(str_for_copy)
        self.signals.finished_log.emit("ChangeIP - DONE!")