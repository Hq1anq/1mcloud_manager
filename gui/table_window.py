from PySide6.QtWidgets import QMainWindow, QSizeGrip, QTableWidgetItem, QHeaderView, QLineEdit
from PySide6.QtCore import Qt, QThreadPool
from PySide6.QtGui import QShortcut, QKeySequence, QGuiApplication, QColor, QKeyEvent

import json
import server_api
from workers import ChangeNotes, Reinstall, Pause, ChangeIP, Refund

from gui.ui_table import Ui_MainWindow
from gui.window_control import WindowController

DATA_PATH = "data.json"

class TableWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.data = None
        
        self.window_controller = WindowController(self)
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.sizegrip = QSizeGrip(self.ui.sizeGrip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # Minimize window
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        # Close window
        self.ui.closeBtn.clicked.connect(self.close)
        # Restore/Maximize window
        self.ui.changeWindowBtn.clicked.connect(self.window_controller.maximize_restore)

        self.deleted_rows = []
        
        self.setup_filter_row()
        
        # Remove style of item in table for not overwite when setting background
        self.ui.table.setStyleSheet(
            """QTableCornerButton::section { background-color: rgb(33, 37, 43) }
            QTableWidget {
                padding: 5px;
                gridline-color: rgb(44, 49, 58);
                border-bottom: 1px solid rgb(44, 49, 60); }
            QTableWidget::item:selected{
                background-color: rgb(189, 147, 249);
                color: rgb(40, 44, 52);
            }
            QHeaderView { qproperty-defaultAlignment: AlignCenter }
            QHeaderView::section {
                background-color: rgb(33, 37, 43);
                border: 1px solid rgb(44, 49, 60);
                font-size: 15px }
            QLineEdit {
                background-color: rgb(50, 54, 62); /* slightly lighter/darker variant for edit mode */
                selection-background-color: rgb(189, 147, 249); /* background when highlight */
                selection-color: rgb(40, 44, 52);; /* text color when selected */
            }
            """)
        
        self._highlighted_rows = set()
        
        self.ui.getData.clicked.connect(self.run_get_data)
        self.ui.changeNotes.clicked.connect(self.run_change_notes)
        self.ui.reInstall.clicked.connect(self.run_reinstall)
        self.ui.pause.clicked.connect(self.run_pause)
        self.ui.refund.clicked.connect(self.run_refund)
        self.ui.changeIP.clicked.connect(self.run_changeip)
        self.ui.reload.clicked.connect(self.reload)
        self.ui.copyIP.clicked.connect(self.copy_ip)
        
        self.ui.table.itemSelectionChanged.connect(self.highlight_selected_row)
        
        save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        save_shortcut.activated.connect(self.save_table_to_file)
        undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        undo_shortcut.activated.connect(self.undoDelete)
        
        self.show()
        
        self.reload()
        
    def run_get_data(self):
        ips = self.ui.txtIP.toPlainText()
        amount = self.ui.txtAmount.text()
        data = server_api.get_data(ips, amount)
        self.load_data2table(data)
        if data is None:
            self.ui.statusTable.setText("Get Data - FAILED!")
            return
        self.load_data2table(data)
        self.ui.statusTable.setText("Get Data - DONE!")
    
    def run_change_notes(self):
        selected_rows = set(item.row() for item in self.ui.table.selectedItems())
        note = self.ui.txtNote.text()
        if not note.strip():
            return

        worker = ChangeNotes(
            list(selected_rows), note, self.ui.replaceCheckbox.isChecked(), self.ui.table
        )
        worker.signals.change_table.connect(self.update_row)
        worker.signals.finished_log.connect(self.show_status)
        
        QThreadPool.globalInstance().start(worker)
        
    def run_reinstall(self):
        selected_rows = set(item.row() for item in self.ui.table.selectedItems())

        worker = Reinstall(list(selected_rows), self.ui.txtReinstall.text().strip(), self.ui.table)
        worker.signals.change_table.connect(self.update_row)
        worker.signals.finished_log.connect(self.show_status)
        
        QThreadPool.globalInstance().start(worker)
        
    def run_pause(self):
        selected_rows = set(item.row() for item in self.ui.table.selectedItems())
        
        worker = Pause(list(selected_rows), self.ui.table)
        worker.signals.change_table.connect(self.update_row)
        worker.signals.finished_log.connect(self.show_status)
        
        QThreadPool.globalInstance().start(worker)
    
    def run_refund(self):
        selected_rows = set(item.row() for item in self.ui.table.selectedItems())
        
        worker = Refund(list(selected_rows), self.ui.table)
        worker.signals.change_table.connect(self.update_row)
        worker.signals.finished_log.connect(self.show_status)
        
        QThreadPool.globalInstance().start(worker)
        
    def run_changeip(self):
        selected_rows = set(item.row() for item in self.ui.table.selectedItems())

        worker = ChangeIP(rows=list(selected_rows), custom_info=None, table=self.ui.table)
        worker.signals.change_table.connect(self.update_row)
        worker.signals.finished_log.connect(self.show_status)
        
        QThreadPool.globalInstance().start(worker)
        
    def reload(self):
        '''Load json file to table widget'''
        self.load_data(DATA_PATH)
        self.load_data2table(self.data)
        
    # Add this method to your class:
    def save_table_to_file(self):
        self.save_data(DATA_PATH)
        self.show_status("Saved data to: " + DATA_PATH)
    
    def copy_ip(self):
        selected_rows = set(idx.row() for idx in self.ui.table.selectedIndexes())
        ip_items = [self.ui.table.item(row, 2).text().split(":")[0] for row in selected_rows]
        
        if ip_items:
            copied_text = "\n".join(ip_items)
            QGuiApplication.clipboard().setText(copied_text)
        
        self.ui.statusTable.setText("Copied IPs to clipboard!")
        
    def update_row(self, row: int, success: bool, note: str = None, ip_port: str = None, status: str = None, change_ip: bool = None):
        if success:
            self.ui.table.setItem(row, 0, self.table_item("✔️"))
            if note:
                self.ui.table.setItem(row, 9, self.table_item(note))
            if ip_port:
                self.ui.table.setItem(row, 2, self.table_item(ip_port))
            if status:
                self.ui.table.setItem(row, 7, self.table_item(status))
            if change_ip:
                count_changeip = int(self.ui.table.item(row, 8).text()) + 1
                self.ui.table.setItem(row, 8, self.table_item(str(count_changeip)))
        else:
            self.ui.table.setItem(row, 0, self.table_item("❌"))
    
    def show_status(self, log: str):
        self.ui.statusTable.setText(log)
    
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.window_controller.handle_mouse_press(event)
        
    def resizeEvent(self, event):
        # Update Size Grips
        self.window_controller.update_grips_geometry()
        
    def adjust_column_width(self):
        # Temporarily hide filter row
        self.ui.table.setRowHidden(0, True)
        header = self.ui.table.horizontalHeader()

        # Set columns 0-8 to ResizeToContents (fixed, minimum size)
        for i in range(9):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)
            self.ui.table.resizeColumnToContents(i)
            self.ui.table.setColumnWidth(i, self.ui.table.columnWidth(i) + 10)  # Add extra width

        # Set last column (9) to Stretch (expand with parent)
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.Stretch)
        # Show filter row again
        self.ui.table.setRowHidden(0, False)
    
    def setup_filter_row(self):
        self.ui.table.setRowCount(1)  # Ensure at least one row for filters
        self.filter_edits = []
        for col in range(1, self.ui.table.columnCount()):
            edit = QLineEdit()
            edit.setPlaceholderText("Filter")
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter if col != 9 else Qt.AlignmentFlag.AlignLeft)
            edit.setStyleSheet("background-color: rgb(40, 44, 52);")
            edit.returnPressed.connect(self.filter_table)
            self.ui.table.setCellWidget(0, col, edit)
            self.filter_edits.append(edit)
    
    def filter_table(self):
        visible_index = 1
        header_labels = [""]  # For filter row
        for row in range(1, self.ui.table.rowCount()):  # Skip filter row
            show_row = True
            for col, edit in enumerate(self.filter_edits, start=1):
                filter_text = edit.text().lower()
                item = self.ui.table.item(row, col)
                if filter_text and (not item or filter_text not in item.text().lower()):
                    show_row = False
                    break
            
            # Show/hide row and update row counter
            if show_row:
                self.ui.table.setRowHidden(row, False)
                header_labels.append(str(visible_index))
                visible_index += 1
            else:
                self.ui.table.setRowHidden(row, True)
                header_labels.append("")
                
        self.ui.table.setVerticalHeaderLabels(header_labels)
        self.adjust_column_width()
                
    def highlight_selected_row(self):
        selected_rows = set(idx.row() for idx in self.ui.table.selectedIndexes() if idx.row() > 0)
        
        # Rows to clear: previously highlighted but not currently selected
        rows_to_clear = self._highlighted_rows - selected_rows
        for row in rows_to_clear:
            for col in range(self.ui.table.columnCount()):
                item = self.ui.table.item(row, col)
                if item:
                    item.setBackground(QColor(40, 44, 52))  # Default bg
        
        # Rows to highlight: currently selected but not previously highlighted
        for row in selected_rows:
            for col in range(self.ui.table.columnCount()):
                item = self.ui.table.item(row, col)
                if item:
                    item.setBackground(QColor("#313640"))  # Subtle highlight
                    
        # Update the cache
        self._highlighted_rows = selected_rows
        self.ui.countRows.setText(f"Rows: {len(selected_rows)}")

    def addRow(self):
        currentRow = self.ui.table.currentRow()
        self.ui.table.insertRow(currentRow + 1)
        
    def deleteRow(self):
        if self.ui.table.rowCount() > 0:
            selectedRows = sorted(set(index.row() for index in self.ui.table.selectedIndexes()), reverse=True)
            for currentRow in selectedRows:
                row_data = [self.ui.table.item(currentRow, col).text() if self.ui.table.item(currentRow, col)
                            else '' for col in range(self.ui.table.columnCount())]
                self.deleted_rows.append((currentRow, row_data))
                self.ui.table.removeRow(currentRow)
            if len(selectedRows) == 0:
                self.ui.table.setCurrentCell(0, 0)
            else:
                self.ui.table.setCurrentCell(currentRow, 0)

    def undoDelete(self):
        if self.deleted_rows:
            row_index, row_data = self.deleted_rows.pop()
            self.ui.table.insertRow(row_index)
            for col, data in enumerate(row_data):
                item = QTableWidgetItem(data)
                self.ui.table.setItem(row_index, col, item)
            self.ui.table.setCurrentCell(row_index, 0)
    
    def table_item(self, text: str):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        return item
            
    def keyPressEvent(self, event: QKeyEvent):
        if event.matches(QKeySequence.StandardKey.Copy):
            self.copy_selected_cells()
        else:
            super().keyPressEvent(event)

    def copy_selected_cells(self):
        selected_items = self.ui.table.selectedItems()
        if not selected_items:
            return
        # Sort by row and column
        selected_items.sort(key=lambda item: (item.row(), item.column()))
        copied_text = "\n".join(item.text() for item in selected_items)
        QGuiApplication.clipboard().setText(copied_text)
    
    def load_data(self, file_path: str):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
                return self.data
        except:
            return None
        
    def load_data2table(self, data: list[dict]):
        self.ui.table.setRowCount(len(data) + 1)  # Set number of rows
        for row, server in enumerate(data, start=1):
            items = [
                QTableWidgetItem(str(server.get("server_id", ""))),
                QTableWidgetItem(server.get("ip_port", "")),
                QTableWidgetItem(server.get("country", "")),
                QTableWidgetItem(server.get("plan_number", "")),
                QTableWidgetItem(server.get("ngay_mua", "")),
                QTableWidgetItem(server.get("het_han", "")),
                QTableWidgetItem(server.get("trang_thai", "")),
                QTableWidgetItem(str(server.get("changed_ip", ""))),
                QTableWidgetItem(server.get("note", "")),
            ]
            # Insert blank or icon for first column if needed
            items.insert(0, QTableWidgetItem(""))  # Adjust if you use icons

            for col, item in enumerate(items):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter if col != 9 else Qt.AlignmentFlag.AlignLeft)
                self.ui.table.setItem(row, col, item)
        
        # Show row numbers starting from 1 for data rows
        headers = [""] + [str(i) for i in range(1, len(data) + 1)]
        self.ui.table.setVerticalHeaderLabels(headers)
        self.adjust_column_width()
    
    def save_data(self, file_path: str):
        data = []
        # Start from row 1 to skip filter row
        for row in range(1, self.ui.table.rowCount()):
            row_dict = {
                "server_id": int(self.ui.table.item(row, 1).text()) if self.ui.table.item(row, 1) else "",
                "ip_port": self.ui.table.item(row, 2).text() if self.ui.table.item(row, 2) else "",
                "country": self.ui.table.item(row, 3).text() if self.ui.table.item(row, 3) else "",
                "plan_number": self.ui.table.item(row, 4).text() if self.ui.table.item(row, 4) else "",
                "ngay_mua": self.ui.table.item(row, 5).text() if self.ui.table.item(row, 5) else "",
                "het_han": self.ui.table.item(row, 6).text() if self.ui.table.item(row, 6) else "",
                "trang_thai": self.ui.table.item(row, 7).text() if self.ui.table.item(row, 7) else "",
                "changed_ip": int(self.ui.table.item(row, 8).text()) if self.ui.table.item(row, 8) else "",
                "note": self.ui.table.item(row, 9).text() if self.ui.table.item(row, 9) else "",
            }
            data.append(row_dict)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)