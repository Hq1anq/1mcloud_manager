# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablepgVqhO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

import resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 603)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{ border: none }\n"
"#navigationBar { background-color: transparent }\n"
"#navigationBar .QPushButton {\n"
"	background-color: transparent; border: none }\n"
"#navigationBar .QPushButton:hover {\n"
"	background-color: rgb(44, 49, 57);\n"
"	border-style: solid; border-radius: 4px }\n"
"#navigationBar .QPushButton:pressed {\n"
"	background-color: rgb(23, 26, 30);\n"
"	border-style: solid;\n"
"	border-radius: 4px }\n"
"#contentTop { background-color: rgb(33, 37, 43) }\n"
"#contentTop .QLabel { background-color: transparent; font-size: 15px }\n"
"QWidget {\n"
"	background-color: rgb(40, 44, 52);\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10px \"Segoe UI\" }\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60) }\n"
"QCheckBox::indicator:hover { border: 3px solid rgb(58, 66, 81) }\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
""
                        "	background-image: url(:/icons/icons/check.svg) }\n"
"QTableCornerButton::section { background-color: rgb(33, 37, 43) }\n"
"QTableWidget {	\n"
"	padding: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	font-size: 10px }\n"
"QTableWidget::item{ border-color: rgb(44, 49, 60) }\n"
"QTableWidget::item:selected{ background-color: rgb(189, 147, 249) }\n"
"QHeaderView { qproperty-defaultAlignment: AlignCenter }\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	font-size: 15px }\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"	height: 8px;\n"
"	margin: 0px 21px 0 21px;\n"
"	border-radius: 0px }\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(189, 147, 249);\n"
"	min-width: 25px;\n"
"	border-radius: 4px }\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {\n"
"	background: rgb(208, 181, 249) }\n"
"QScrollBar::handle:horizontal:pressed, QScroll"
                        "Bar::handle:vertical:pressed {\n"
"	background: rgb(161, 103, 249) }\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin }\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin }\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none }\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px }\n"
""
                        "QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"	min-height: 25px;\n"
"	border-radius: 4px }\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin }\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgb(55, 63, 77);\n"
"	height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin }\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover {\n"
"	background: rgb(64, 69, 77) }\n"
"QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed,\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed {\n"
"	background: rgb(189, 147, 249) }")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 10):
            self.table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.table.setObjectName(u"table")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.horizontalHeader().setMinimumSectionSize(110)
        self.table.horizontalHeader().setDefaultSectionSize(200)

        self.gridLayout.addWidget(self.table, 7, 0, 1, 2)

        self.sizeGrip = QFrame(self.centralwidget)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setCursor(QCursor(Qt.CursorShape.SizeFDiagCursor))

        self.gridLayout.addWidget(self.sizeGrip, 8, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.contentTop = QFrame(self.centralwidget)
        self.contentTop.setObjectName(u"contentTop")
        self.contentTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTop)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon = QLabel(self.contentTop)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(40, 16777215))
        self.icon.setPixmap(QPixmap(u":/icons/icons/Logo.svg"))
        self.icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.icon)

        self.title = QLabel(self.contentTop)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"#title{font-size: 20px; font-weight: bold}")

        self.horizontalLayout.addWidget(self.title)

        self.navigationBar = QFrame(self.contentTop)
        self.navigationBar.setObjectName(u"navigationBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.navigationBar.sizePolicy().hasHeightForWidth())
        self.navigationBar.setSizePolicy(sizePolicy2)
        self.hboxLayout = QHBoxLayout(self.navigationBar)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.navigationBar)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(33, 33))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(False)
        font1.setItalic(False)
        self.minimizeBtn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon1)
        self.minimizeBtn.setIconSize(QSize(15, 15))

        self.hboxLayout.addWidget(self.minimizeBtn)

        self.changeWindowBtn = QPushButton(self.navigationBar)
        self.changeWindowBtn.setObjectName(u"changeWindowBtn")
        self.changeWindowBtn.setMinimumSize(QSize(33, 33))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/icons/restore.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.changeWindowBtn.setIcon(icon2)
        self.changeWindowBtn.setIconSize(QSize(15, 15))
        self.changeWindowBtn.setCheckable(True)

        self.hboxLayout.addWidget(self.changeWindowBtn)

        self.closeBtn = QPushButton(self.navigationBar)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(33, 33))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setIconSize(QSize(15, 15))

        self.hboxLayout.addWidget(self.closeBtn)


        self.horizontalLayout.addWidget(self.navigationBar, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.contentTop, 0, 0, 1, 2)

        self.statusTable = QLabel(self.centralwidget)
        self.statusTable.setObjectName(u"statusTable")
        self.statusTable.setStyleSheet(u"color: yellow")
        self.statusTable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.statusTable, 3, 0, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setStyleSheet(u"QPushButton {\n"
"	font: 20px;\n"
"	font-weight: bold;\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding: 10px }\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 3px solid rgb(61, 70, 86) }\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 3px solid rgb(43, 50, 61) }\n"
"QLabel { qproperty-alignment: AlignCenter }\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 3px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198) }\n"
"QLineEdit:hover, QTextEdit:hover, QPlainTextEdit:hover { border: 2px solid rgb(64, 71, 88) }\n"
"QLineEdit:focus,  QTextEdit:focus, QPlainTextEdit:hover { border: 2px solid rgb(91, 101, 124) }\n"
"QComboBox { background-color: rgb(33, 37, 43) }")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(20)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.changeNotes = QPushButton(self.frame)
        self.changeNotes.setObjectName(u"changeNotes")

        self.gridLayout_2.addWidget(self.changeNotes, 0, 1, 1, 1)

        self.getData = QPushButton(self.frame)
        self.getData.setObjectName(u"getData")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.getData.sizePolicy().hasHeightForWidth())
        self.getData.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.getData, 0, 0, 2, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)

        self.changeIP = QPushButton(self.frame)
        self.changeIP.setObjectName(u"changeIP")

        self.gridLayout_3.addWidget(self.changeIP, 1, 0, 1, 1)

        self.reInstall = QPushButton(self.frame)
        self.reInstall.setObjectName(u"reInstall")

        self.gridLayout_3.addWidget(self.reInstall, 1, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_3)


        self.gridLayout.addWidget(self.frame, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"SID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"IP:PORT", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"COUNTRY", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"FROM", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TO", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CHANGED_IP", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(9)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"NOTE", None));
        self.title.setText(QCoreApplication.translate("MainWindow", u"1MCLOUD", None))
        self.statusTable.setText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch ip, m\u1ed7i ip m\u1ed9t d\u00f2ng", None))
        self.changeNotes.setText(QCoreApplication.translate("MainWindow", u"CHANGE NOTES", None))
        self.getData.setText(QCoreApplication.translate("MainWindow", u"GET DATA", None))
        self.changeIP.setText(QCoreApplication.translate("MainWindow", u"CHANGE IP", None))
        self.reInstall.setText(QCoreApplication.translate("MainWindow", u"REINSTALL", None))
    # retranslateUi

