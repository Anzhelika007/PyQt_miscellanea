# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self,QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"MainWindow")
        QMainWindow.resize(596, 601)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        QMainWindow.setFont(font)
        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_pushButton = QPushButton(self.centralwidget)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.verticalLayout.addWidget(self.add_pushButton)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 572, 380))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.coordWidget_layout = QVBoxLayout()
        self.coordWidget_layout.setSpacing(6)
        self.coordWidget_layout.setObjectName(u"coordWidget_layout")

        self.verticalLayout_3.addLayout(self.coordWidget_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.clear_pushButton = QPushButton(self.centralwidget)
        self.clear_pushButton.setObjectName(u"clear_pushButton")

        self.verticalLayout.addWidget(self.clear_pushButton)

        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 596, 47))
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)

        QMetaObject.connectSlotsByName(QMainWindow)
    # setupUi

    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0439\u0442\u0430\u043d \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.add_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.clear_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi


