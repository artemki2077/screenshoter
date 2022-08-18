# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Screenshoter(object):
    def setupUi(self, Screenshoter):
        if not Screenshoter.objectName():
            Screenshoter.setObjectName(u"Screenshoter")
        Screenshoter.resize(957, 706)
        self.centralwidget = QWidget(Screenshoter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.select_net = QComboBox(self.centralwidget)
        self.select_net.setObjectName(u"select_net")
        self.select_net.setEnabled(True)
        self.select_net.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.select_net.setLayoutDirection(Qt.LeftToRight)
        self.select_net.setAutoFillBackground(False)
        self.select_net.setEditable(True)
        self.select_net.setDuplicatesEnabled(False)

        self.horizontalLayout_3.addWidget(self.select_net)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.x_net = QSpinBox(self.centralwidget)
        self.x_net.setObjectName(u"x_net")
        self.x_net.setMaximum(700)

        self.horizontalLayout_4.addWidget(self.x_net)

        self.y_net = QSpinBox(self.centralwidget)
        self.y_net.setObjectName(u"y_net")
        self.y_net.setMaximum(700)

        self.horizontalLayout_4.addWidget(self.y_net)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.input_name = QLineEdit(self.centralwidget)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_7.addWidget(self.input_name)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.x_name = QSpinBox(self.centralwidget)
        self.x_name.setObjectName(u"x_name")
        self.x_name.setMaximum(700)

        self.horizontalLayout_8.addWidget(self.x_name)

        self.y_name = QSpinBox(self.centralwidget)
        self.y_name.setObjectName(u"y_name")
        self.y_name.setMaximum(700)

        self.horizontalLayout_8.addWidget(self.y_name)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.input_full_name = QLineEdit(self.centralwidget)
        self.input_full_name.setObjectName(u"input_full_name")
        self.input_full_name.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_9.addWidget(self.input_full_name)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.x_full_name = QSpinBox(self.centralwidget)
        self.x_full_name.setObjectName(u"x_full_name")
        self.x_full_name.setMaximum(700)

        self.horizontalLayout_10.addWidget(self.x_full_name)

        self.y_full_name = QSpinBox(self.centralwidget)
        self.y_full_name.setObjectName(u"y_full_name")
        self.y_full_name.setMaximum(700)

        self.horizontalLayout_10.addWidget(self.y_full_name)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_21.addWidget(self.label_6)

        self.font_index = QDoubleSpinBox(self.centralwidget)
        self.font_index.setObjectName(u"font_index")
        font = QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.font_index.setFont(font)
        self.font_index.setSingleStep(0.100000000000000)
        self.font_index.setValue(1.000000000000000)

        self.horizontalLayout_21.addWidget(self.font_index)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_18.addWidget(self.label_7)

        self.input_id_api = QLineEdit(self.centralwidget)
        self.input_id_api.setObjectName(u"input_id_api")
        self.input_id_api.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_18.addWidget(self.input_id_api)

        self.get_price = QPushButton(self.centralwidget)
        self.get_price.setObjectName(u"get_price")

        self.horizontalLayout_18.addWidget(self.get_price)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_20.addWidget(self.label_9)

        self.input_link_img = QLineEdit(self.centralwidget)
        self.input_link_img.setObjectName(u"input_link_img")
        self.input_link_img.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_20.addWidget(self.input_link_img)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_13.addWidget(self.label)

        self.check_trust = QCheckBox(self.centralwidget)
        self.check_trust.setObjectName(u"check_trust")

        self.horizontalLayout_13.addWidget(self.check_trust)

        self.check_meta = QCheckBox(self.centralwidget)
        self.check_meta.setObjectName(u"check_meta")

        self.horizontalLayout_13.addWidget(self.check_meta)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.input_lost = QDoubleSpinBox(self.centralwidget)
        self.input_lost.setObjectName(u"input_lost")
        self.input_lost.setDecimals(16)
        self.input_lost.setMaximum(90000.990000000005239)

        self.horizontalLayout_11.addWidget(self.input_lost)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.x_lost = QSpinBox(self.centralwidget)
        self.x_lost.setObjectName(u"x_lost")
        self.x_lost.setMaximum(700)

        self.horizontalLayout_12.addWidget(self.x_lost)

        self.y_lost = QSpinBox(self.centralwidget)
        self.y_lost.setObjectName(u"y_lost")
        self.y_lost.setMaximum(700)

        self.horizontalLayout_12.addWidget(self.y_lost)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_15.addWidget(self.label_8)

        self.input_price = QDoubleSpinBox(self.centralwidget)
        self.input_price.setObjectName(u"input_price")
        self.input_price.setDecimals(16)
        self.input_price.setMaximum(90000.990000000005239)

        self.horizontalLayout_15.addWidget(self.input_price)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.x_price = QSpinBox(self.centralwidget)
        self.x_price.setObjectName(u"x_price")
        self.x_price.setMaximum(700)

        self.horizontalLayout_16.addWidget(self.x_price)

        self.y_price = QSpinBox(self.centralwidget)
        self.y_price.setObjectName(u"y_price")
        self.y_price.setMaximum(700)

        self.horizontalLayout_16.addWidget(self.y_price)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 340, 247))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")

        self.verticalLayout.addWidget(self.plus)

        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate.sizePolicy().hasHeightForWidth())
        self.generate.setSizePolicy(sizePolicy)
        self.generate.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.generate)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_state = QPushButton(self.centralwidget)
        self.btn_state.setObjectName(u"btn_state")

        self.verticalLayout_3.addWidget(self.btn_state)

        self.image = QLabel(self.centralwidget)
        self.image.setObjectName(u"image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy1)
        self.image.setMinimumSize(QSize(575, 601))
        self.image.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.image)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")

        self.horizontalLayout_17.addWidget(self.back)

        self.forward = QPushButton(self.centralwidget)
        self.forward.setObjectName(u"forward")

        self.horizontalLayout_17.addWidget(self.forward)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        Screenshoter.setCentralWidget(self.centralwidget)

        self.retranslateUi(Screenshoter)

        QMetaObject.connectSlotsByName(Screenshoter)
    # setupUi

    def retranslateUi(self, Screenshoter):
        Screenshoter.setWindowTitle(QCoreApplication.translate("Screenshoter", u"Screenshoter", None))
        self.label_2.setText(QCoreApplication.translate("Screenshoter", u"Net", None))
        self.select_net.setCurrentText("")
        self.select_net.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Screenshoter", u"Name", None))
        self.input_name.setPlaceholderText(QCoreApplication.translate("Screenshoter", u"MVL", None))
        self.label_4.setText(QCoreApplication.translate("Screenshoter", u"Full name", None))
        self.input_full_name.setPlaceholderText(QCoreApplication.translate("Screenshoter", u"Mass Vehicle Ledger", None))
        self.label_6.setText(QCoreApplication.translate("Screenshoter", u"font", None))
        self.label_7.setText(QCoreApplication.translate("Screenshoter", u"id_api", None))
        self.input_id_api.setPlaceholderText(QCoreApplication.translate("Screenshoter", u"mass-vehicle-ledger", None))
        self.get_price.setText(QCoreApplication.translate("Screenshoter", u"get", None))
        self.label_9.setText(QCoreApplication.translate("Screenshoter", u"link img", None))
        self.input_link_img.setPlaceholderText(QCoreApplication.translate("Screenshoter", u"https://assets.coingecko.com/coins/images/3447/small/ONT.png", None))
        self.label.setText(QCoreApplication.translate("Screenshoter", u"platform", None))
        self.check_trust.setText(QCoreApplication.translate("Screenshoter", u"TrustWallet", None))
        self.check_meta.setText(QCoreApplication.translate("Screenshoter", u"MetaMask", None))
        self.label_5.setText(QCoreApplication.translate("Screenshoter", u"lost", None))
        self.label_8.setText(QCoreApplication.translate("Screenshoter", u"coin_price", None))
        self.plus.setText(QCoreApplication.translate("Screenshoter", u"plus", None))
        self.generate.setText(QCoreApplication.translate("Screenshoter", u"generate", None))
        self.btn_state.setText(QCoreApplication.translate("Screenshoter", u"Trust Wallet", None))
        self.image.setText(QCoreApplication.translate("Screenshoter", u"TextLabel", None))
        self.back.setText(QCoreApplication.translate("Screenshoter", u"<", None))
        self.forward.setText(QCoreApplication.translate("Screenshoter", u">", None))
    # retranslateUi

