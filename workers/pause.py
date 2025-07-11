import server_api
import pyperclip, time

from PySide6.QtCore import QRunnable, Signal, QObject
from PySide6.QtWidgets import QTableWidget

class Pause(QRunnable):
    
    class Signals(QObject):
        change_table = Signal(int, bool, str, str, str, bool)  # row, success, note, ip_port, status, change_ip
        finished_log = Signal(str)
        
    def __init__(self, rows, table):
        super().__init__()
        self.rows = rows
        self.table: QTableWidget = table
        self.signals = self.Signals()
    
    def set_row(self, row: int, success: bool, status: str = None):
        self.signals.change_table.emit(row, success, None, None, status, False)
        
    def run(self):
        list_sids = []
        row_sid_map = {}
        for row in self.rows:
            item = self.table.item(row, 1)
            if not item:
                self.signals.change_table.emit(row, False, None, None)
                continue
            sid = item.text()
            list_sids.append(sid)
            row_sid_map[sid] = row  # <-- Map sid to row
        pause_status = server_api.pause(sids="\n".join(list_sids))
        if pause_status:
            success_sids = set(str(sid) for sid in pause_status["result"]["success"])
            for sid in list_sids:
                row = row_sid_map[sid]
                if sid in success_sids:
                    self.set_row(row, True, "Paused")
                else:
                    self.set_row(row, False, "Pause failed")
            self.signals.finished_log.emit("Pause - DONE!")
        else:
            self.signals.finished_log.emit("Pause - ERROR!")