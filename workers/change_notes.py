import server_api

from PySide6.QtCore import QRunnable, Signal, QObject
from PySide6.QtWidgets import QTableWidget

class ChangeNotes(QRunnable):
    
    class Signals(QObject):
        change_table = Signal(int, bool, str)  # row, success, note
        
    def __init__(self, rows, note, replace, table):
        super().__init__()
        self.rows = rows
        self.note: str = note
        self.replace = replace
        self.table: QTableWidget = table
        self.signals = self.Signals()

    def run(self):
        for row in self.rows:
            item = self.table.item(row, 1)
            if not item:
                self.signals.change_table.emit(row, False, self.note)
                continue
            if self.replace:
                note_to_send = self.note.strip()
            else:
                # Remove the first word and space from note
                parts = self.table.item(row, 9).text().strip().split(maxsplit=1)
                suffix = parts[1] if len(parts) > 1 else ""
                note_to_send = self.note + suffix
            status_code = server_api.change_note(item.text(), note_to_send)
            self.signals.change_table.emit(row, status_code == 200, note_to_send)