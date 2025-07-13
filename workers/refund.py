import server_api

from PySide6.QtCore import QRunnable, Signal, QObject
from PySide6.QtWidgets import QTableWidget

class Refund(QRunnable):
    
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
        list_ip = []
        list_sid = []
        row_ip_map = {}
        for row in self.rows:
            sid = self.table.item(row, 1).text().strip()
            ip = self.table.item(row, 2).text().split(":")[0].strip()
            if not sid or not ip:
                self.signals.change_table.emit(row, False, None, None)
                continue
            list_ip.append(ip)
            list_sid.append(sid)
            row_ip_map[ip] = row  # <-- Map sid to row
        refund_status = server_api.refund(sids="\n".join(list_sid))
        print(refund_status)
        if refund_status:
            success_ips = set(str(sid) for sid in refund_status["result"]["success"].keys())
            for sid in list_ip:
                row = row_ip_map[sid]
                if sid in success_ips:
                    self.set_row(row, True, "Refunded")
                else:
                    self.set_row(row, False, "Refund failed")
            self.signals.finished_log.emit("Refund - DONE!")
        else:
            self.signals.finished_log.emit("Refund - ERROR!")