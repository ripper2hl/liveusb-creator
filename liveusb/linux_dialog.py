# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/liveusb-creator.ui'
#
# Created: Fri Dec 12 13:46:45 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(690, 538)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(477, 519))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(477, 519))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("background-image: url(:/liveusb-header-bg.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/liveusb-header-left.png")))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setMargin(-1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet(_fromUtf8("background-image: url(:/liveusb-header-bg.png);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/liveusb-header-right.png")))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setMargin(-1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_9.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.isoBttn = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isoBttn.sizePolicy().hasHeightForWidth())
        self.isoBttn.setSizePolicy(sizePolicy)
        self.isoBttn.setObjectName(_fromUtf8("isoBttn"))
        self.horizontalLayout_7.addWidget(self.isoBttn)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.downloadGroup = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadGroup.sizePolicy().hasHeightForWidth())
        self.downloadGroup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.downloadGroup.setFont(font)
        self.downloadGroup.setObjectName(_fromUtf8("downloadGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.downloadGroup)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.downloadCombo = QtGui.QComboBox(self.downloadGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadCombo.sizePolicy().hasHeightForWidth())
        self.downloadCombo.setSizePolicy(sizePolicy)
        self.downloadCombo.setObjectName(_fromUtf8("downloadCombo"))
        self.horizontalLayout_6.addWidget(self.downloadCombo)
        self.refreshReleasesButton = QtGui.QPushButton(self.downloadGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshReleasesButton.sizePolicy().hasHeightForWidth())
        self.refreshReleasesButton.setSizePolicy(sizePolicy)
        self.refreshReleasesButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshReleasesButton.setIcon(icon)
        self.refreshReleasesButton.setFlat(True)
        self.refreshReleasesButton.setObjectName(_fromUtf8("refreshReleasesButton"))
        self.horizontalLayout_6.addWidget(self.refreshReleasesButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.downloadGroup)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.driveBox = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driveBox.sizePolicy().hasHeightForWidth())
        self.driveBox.setSizePolicy(sizePolicy)
        self.driveBox.setEditable(False)
        self.driveBox.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.driveBox.setDuplicatesEnabled(False)
        self.driveBox.setObjectName(_fromUtf8("driveBox"))
        self.horizontalLayout.addWidget(self.driveBox)
        self.refreshDevicesButton = QtGui.QPushButton(self.groupBox_2)
        self.refreshDevicesButton.setText(_fromUtf8(""))
        self.refreshDevicesButton.setIcon(icon)
        self.refreshDevicesButton.setFlat(True)
        self.refreshDevicesButton.setObjectName(_fromUtf8("refreshDevicesButton"))
        self.horizontalLayout.addWidget(self.refreshDevicesButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.overlayTitle = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overlayTitle.sizePolicy().hasHeightForWidth())
        self.overlayTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.overlayTitle.setFont(font)
        self.overlayTitle.setObjectName(_fromUtf8("overlayTitle"))
        self.gridLayout_4 = QtGui.QGridLayout(self.overlayTitle)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.overlaySlider = QtGui.QSlider(self.overlayTitle)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overlaySlider.sizePolicy().hasHeightForWidth())
        self.overlaySlider.setSizePolicy(sizePolicy)
        self.overlaySlider.setMaximum(2047)
        self.overlaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.overlaySlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.overlaySlider.setObjectName(_fromUtf8("overlaySlider"))
        self.gridLayout_4.addWidget(self.overlaySlider, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.overlayTitle)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.nonDestructiveButton = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nonDestructiveButton.sizePolicy().hasHeightForWidth())
        self.nonDestructiveButton.setSizePolicy(sizePolicy)
        self.nonDestructiveButton.setChecked(True)
        self.nonDestructiveButton.setObjectName(_fromUtf8("nonDestructiveButton"))
        self.horizontalLayout_5.addWidget(self.nonDestructiveButton)
        self.destructiveButton = QtGui.QRadioButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destructiveButton.sizePolicy().hasHeightForWidth())
        self.destructiveButton.setSizePolicy(sizePolicy)
        self.destructiveButton.setObjectName(_fromUtf8("destructiveButton"))
        self.horizontalLayout_5.addWidget(self.destructiveButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout.addWidget(self.startButton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fedora Live USB Creator", None))
        self.groupBox.setWhatsThis(_translate("MainWindow", "This button allows you to browse for an existing Live CD ISO that you have previously downloaded.  If you do not select one, a release will be downloaded for you automatically.", None))
        self.groupBox.setTitle(_translate("MainWindow", "Use existing Live CD", None))
        self.isoBttn.setText(_translate("MainWindow", "Browse", None))
        self.isoBttn.setShortcut(_translate("MainWindow", "Alt+B", None))
        self.downloadGroup.setWhatsThis(_translate("MainWindow", "If you do not select an existing Live CD, the selected release will be downloaded for you.", None))
        self.downloadGroup.setTitle(_translate("MainWindow", "Download Fedora", None))
        self.groupBox_2.setWhatsThis(_translate("MainWindow", "This is the USB stick that you want to install your Live CD on.  This device must be formatted with the FAT filesystem.", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Target Device", None))
        self.overlayTitle.setWhatsThis(_translate("MainWindow", "By allocating extra space on your USB stick for a persistent overlay, you will be able to store data and make permanent modifications to your live operating system.  Without it, you will not be able to save data that will persist after a reboot.", "comment!"))
        self.overlayTitle.setTitle(_translate("MainWindow", "Persistent Storage (0 MB)", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Method", None))
        self.nonDestructiveButton.setToolTip(_translate("MainWindow", "This method uses the \'cp\' command to copy the files from the ISO on to your USB key, without deleting any existing files.", None))
        self.nonDestructiveButton.setText(_translate("MainWindow", "Non-destructive (cp)", None))
        self.destructiveButton.setToolTip(_translate("MainWindow", "This method uses the \'dd\' comand to copy the ISO directly to your USB device, destroying any pre-existing data/partitions. This method tends to be more reliable with regard to booting, especially with UEFI systems. This method also works with DVD images.", None))
        self.destructiveButton.setText(_translate("MainWindow", "Overwrite device (dd)", None))
        self.textEdit.setWhatsThis(_translate("MainWindow", "This is the status console, where all messages get written to.", None))
        self.progressBar.setWhatsThis(_translate("MainWindow", "This is the progress bar that will indicate how far along in the LiveUSB creation process you are", None))
        self.startButton.setWhatsThis(_translate("MainWindow", "This button will begin the LiveUSB creation process.  This entails optionally downloading a release (if an existing one wasn\'t selected),  extracting the ISO to the USB device, creating the persistent overlay, and installing the bootloader.", None))
        self.startButton.setText(_translate("MainWindow", "Create Live USB", None))

import resources_rc
