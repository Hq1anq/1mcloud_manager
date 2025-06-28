from PySide6.QtWidgets import QMainWindow, QSizeGrip, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence, QGuiApplication

import json
import server_api

from gui.ui_table import Ui_MainWindow
from gui.window_control import WindowController

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
        # CUSTOM GRIPS

        # Minimize window
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        # Close window
        self.ui.closeBtn.clicked.connect(self.close)
        # Restore/Maximize window
        self.ui.changeWindowBtn.clicked.connect(self.window_controller.maximize_restore)

        self.deleted_rows = []
        
        self.ui.getData.clicked.connect(self.run_get_data)
        undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        undo_shortcut.activated.connect(self.undoDelete)
        
        self.show()
        
        self.load_data()
        self.load_data2table(self.data)
        
    def run_get_data(self):
        data = server_api.get_data_from_ip(self.ui.txtIP.toPlainText())
        self.load_data2table(data)
    
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.window_controller.handle_mouse_press(event)
        
    def resizeEvent(self, event):
        # Update Size Grips
        self.window_controller.update_grips_geometry()
        
    def adjust_column_width(self):
        header = self.ui.table.horizontalHeader()

        # Set columns 0-8 to ResizeToContents (fixed, minimum size)
        for i in range(9):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)
            self.ui.table.resizeColumnToContents(i)
            self.ui.table.setColumnWidth(i, self.ui.table.columnWidth(i) + 10)  # Add extra width

        # Set last column (9) to Stretch (expand with parent)
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.Stretch)

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
            
    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Copy):
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
    
    def load_data(self, file_path: str = "data.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
                return self.data
        except:
            return None
    def load_data2table(self, data: list[dict]):
        self.ui.table.setRowCount(len(data))  # Set number of rows
        for row, server in enumerate(data):
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
            items.insert(0, QTableWidgetItem("✔️"))  # Adjust if you use icons

            for col, item in enumerate(items):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if col == 0: # Change font of icon column
                    font = item.font()
                    font.setPointSize(15)
                    item.setFont(font)
                self.ui.table.setItem(row, col, item)
        self.adjust_column_width()