# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_main.ui'
#
# Created: Sat Dec 31 20:31:03 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Base(object):
    def setupUi(self, Base):
        Base.setObjectName("Base")
        Base.resize(650, 600)
        Base.setWindowTitle("KoHighlights")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/stuff/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Base.setWindowIcon(icon)
        Base.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        Base.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(Base)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.file_table = DropTableWidget(self.splitter)
        self.file_table.setFrameShape(QtGui.QFrame.WinPanel)
        self.file_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.file_table.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.file_table.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.file_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.file_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.file_table.setCornerButtonEnabled(False)
        self.file_table.setColumnCount(3)
        self.file_table.setObjectName("file_table")
        self.file_table.setColumnCount(3)
        self.file_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.file_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.file_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.file_table.setHorizontalHeaderItem(2, item)
        self.file_table.horizontalHeader().setHighlightSections(False)
        self.file_table.horizontalHeader().setMinimumSectionSize(22)
        self.file_table.horizontalHeader().setSortIndicatorShown(True)
        self.file_table.verticalHeader().setDefaultSectionSize(22)
        self.file_table.verticalHeader().setHighlightSections(True)
        self.file_table.verticalHeader().setMinimumSectionSize(22)
        self.text_box = QtGui.QPlainTextEdit(self.splitter)
        self.text_box.setFrameShape(QtGui.QFrame.WinPanel)
        self.text_box.setReadOnly(True)
        self.text_box.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.text_box.setObjectName("text_box")
        self.verticalLayout.addWidget(self.splitter)
        Base.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Base)
        self.statusbar.setObjectName("statusbar")
        Base.setStatusBar(self.statusbar)
        self.tool_bar = QtGui.QToolBar(Base)
        self.tool_bar.setWindowTitle("toolBar")
        self.tool_bar.setMovable(True)
        self.tool_bar.setAllowedAreas(QtCore.Qt.BottomToolBarArea|QtCore.Qt.TopToolBarArea)
        self.tool_bar.setIconSize(QtCore.QSize(32, 32))
        self.tool_bar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tool_bar.setObjectName("tool_bar")
        Base.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_bar)
        self.act_english = QtGui.QAction(Base)
        self.act_english.setCheckable(True)
        self.act_english.setChecked(False)
        self.act_english.setObjectName("act_english")
        self.act_greek = QtGui.QAction(Base)
        self.act_greek.setCheckable(True)
        self.act_greek.setChecked(False)
        self.act_greek.setObjectName("act_greek")

        self.retranslateUi(Base)
        QtCore.QMetaObject.connectSlotsByName(Base)

    def retranslateUi(self, Base):
        self.file_table.setSortingEnabled(True)
        self.file_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Base", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.file_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Base", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.file_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Base", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.act_english.setText(QtGui.QApplication.translate("Base", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.act_greek.setText(QtGui.QApplication.translate("Base", "Greek", None, QtGui.QApplication.UnicodeUTF8))

from main import DropTableWidget
import images_rc
