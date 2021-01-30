# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(603, 158)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_source = QLineEdit(self.centralwidget)
        self.line_source.setObjectName(u"line_source")

        self.horizontalLayout.addWidget(self.line_source)

        self.button_source = QPushButton(self.centralwidget)
        self.button_source.setObjectName(u"button_source")

        self.horizontalLayout.addWidget(self.button_source)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_target = QLineEdit(self.centralwidget)
        self.line_target.setObjectName(u"line_target")

        self.horizontalLayout_2.addWidget(self.line_target)

        self.button_target = QPushButton(self.centralwidget)
        self.button_target.setObjectName(u"button_target")

        self.horizontalLayout_2.addWidget(self.button_target)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.spin_fps = QSpinBox(self.centralwidget)
        self.spin_fps.setObjectName(u"spin_fps")
        self.spin_fps.setValue(30)

        self.horizontalLayout_3.addWidget(self.spin_fps)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spin_memory = QSpinBox(self.centralwidget)
        self.spin_memory.setObjectName(u"spin_memory")

        self.horizontalLayout_3.addWidget(self.spin_memory)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spin_blur = QSpinBox(self.centralwidget)
        self.spin_blur.setObjectName(u"spin_blur")

        self.horizontalLayout_3.addWidget(self.spin_blur)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.double_spin_face = QDoubleSpinBox(self.centralwidget)
        self.double_spin_face.setObjectName(u"double_spin_face")
        self.double_spin_face.setMaximum(1.000000000000000)
        self.double_spin_face.setSingleStep(0.050000000000000)

        self.horizontalLayout_3.addWidget(self.double_spin_face)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.double_spin_plate = QDoubleSpinBox(self.centralwidget)
        self.double_spin_plate.setObjectName(u"double_spin_plate")
        self.double_spin_plate.setMaximum(1.000000000000000)
        self.double_spin_plate.setSingleStep(0.050000000000000)

        self.horizontalLayout_3.addWidget(self.double_spin_plate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radio_custom_blur = QRadioButton(self.centralwidget)
        self.radio_custom_blur.setObjectName(u"radio_custom_blur")

        self.horizontalLayout_4.addWidget(self.radio_custom_blur)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.progress = QProgressBar(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setEnabled(True)
        self.progress.setValue(0)

        self.horizontalLayout_5.addWidget(self.progress)

        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")

        self.horizontalLayout_5.addWidget(self.button_start)

        self.button_abort = QPushButton(self.centralwidget)
        self.button_abort.setObjectName(u"button_abort")

        self.horizontalLayout_5.addWidget(self.button_abort)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DashcamCleaner", None))
        self.button_source.setText(QCoreApplication.translate("MainWindow", u"Select video", None))
        self.button_target.setText(QCoreApplication.translate("MainWindow", u"Select target", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Target FPS:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Frame memory:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blur size:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Face threshold:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Plate threshold:", None))
        self.radio_custom_blur.setText(QCoreApplication.translate("MainWindow", u"Use custom blur", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.button_abort.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
    # retranslateUi

