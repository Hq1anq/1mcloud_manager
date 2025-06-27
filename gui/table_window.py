from PySide6.QtWidgets import QMainWindow, QSizeGrip, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence, QGuiApplication

import json

from gui.ui_table import Ui_MainWindow
from gui.window_control import WindowController

class TableWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
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
        
        header = self.ui.table.horizontalHeader()
        header.setStretchLastSection(True)
        # header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Set all columns to stretch by default
        for i in range(1, self.ui.table.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        
        # Set the first column (status) to fixed width, others stretch
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.ui.table.setColumnWidth(0, 10)  # Adjust 40 to your preferred width

        self.deleted_rows = []
        undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        undo_shortcut.activated.connect(self.undoDelete)
        
        self.importData()
        
        self.show()
    
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.window_controller.handle_mouse_press(event)
        
    def resizeEvent(self, event):
        # Update Size Grips
        self.window_controller.update_grips_geometry()

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
    
    def importData(self):
        with open("servers_filtered.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            servers: list[dict] = data.get("servers", [])
        self.ui.table.setRowCount(len(servers))  # Set number of rows
        for row, server in enumerate(servers):
            self.ui.table.setItem(row, 1, QTableWidgetItem(str(server.get("server_id", ""))))
            self.ui.table.setItem(row, 2, QTableWidgetItem(server.get("ip_port", "")))
            self.ui.table.setItem(row, 3, QTableWidgetItem(server.get("country", "")))
            self.ui.table.setItem(row, 4, QTableWidgetItem(server.get("plan_number", "")))
            self.ui.table.setItem(row, 5, QTableWidgetItem(server.get("ngay_mua", "")))
            self.ui.table.setItem(row, 6, QTableWidgetItem(server.get("het_han", "")))
            self.ui.table.setItem(row, 7, QTableWidgetItem(server.get("trang_thai", "")))
            self.ui.table.setItem(row, 8, QTableWidgetItem(str(server.get("changed_ip", ""))))
            self.ui.table.setItem(row, 9, QTableWidgetItem(server.get("note", "")))