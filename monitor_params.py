# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor_params.ui'
#
# Created: Mon Jul 11 12:05:01 2016
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MonitorParams(object):
    def setupUi(self, MonitorParams):
        MonitorParams.setObjectName(_fromUtf8("MonitorParams"))
        MonitorParams.resize(800, 480)
        MonitorParams.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(MonitorParams)
        self.horizontalLayout_2.setMargin(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_8 = QtGui.QWidget(MonitorParams)
        self.horizontalLayout_8.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayout_8)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_13 = QtGui.QWidget(self.horizontalLayout_8)
        self.verticalLayout_13.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayout_13)
        self.verticalLayout_2.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label = QtGui.QLabel(self.verticalLayout_13)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Century Schoolbook\";"))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_11.addWidget(self.label)
        self.capV_out = QtGui.QLabel(self.verticalLayout_13)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.capV_out.setFont(font)
        self.capV_out.setStyleSheet(_fromUtf8("font: 75 18pt \"Century Schoolbook\";\n"
"background-color: rgb(255, 255, 255);"))
        self.capV_out.setAlignment(QtCore.Qt.AlignCenter)
        self.capV_out.setObjectName(_fromUtf8("capV_out"))
        self.verticalLayout_11.addWidget(self.capV_out)
        self.verticalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.verticalLayout_13)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Century Schoolbook\";"))
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.freq_out = QtGui.QLabel(self.verticalLayout_13)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.freq_out.setFont(font)
        self.freq_out.setStyleSheet(_fromUtf8("font: 75 18pt \"Century Schoolbook\";\n"
"background-color: rgb(255, 255, 255);"))
        self.freq_out.setAlignment(QtCore.Qt.AlignCenter)
        self.freq_out.setObjectName(_fromUtf8("freq_out"))
        self.verticalLayout_4.addWidget(self.freq_out)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.verticalLayout_13)
        self.verticalLayout_12 = QtGui.QWidget(self.horizontalLayout_8)
        self.verticalLayout_12.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayout_12)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_3 = QtGui.QLabel(self.verticalLayout_12)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Century Schoolbook\";"))
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_7.addWidget(self.label_3)
        self.opV_out = QtGui.QLabel(self.verticalLayout_12)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.opV_out.setFont(font)
        self.opV_out.setStyleSheet(_fromUtf8("font: 75 18pt \"Century Schoolbook\";\n"
"background-color: rgb(255, 255, 255);"))
        self.opV_out.setAlignment(QtCore.Qt.AlignCenter)
        self.opV_out.setObjectName(_fromUtf8("opV_out"))
        self.verticalLayout_7.addWidget(self.opV_out)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_8 = QtGui.QLabel(self.verticalLayout_12)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Century Schoolbook\";"))
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_6.addWidget(self.label_8)
        self.invC_out = QtGui.QLabel(self.verticalLayout_12)
        self.invC_out.setStyleSheet(_fromUtf8("font: 75 18pt \"Century Schoolbook\";\n"
"background-color: rgb(255, 255, 255);"))
        self.invC_out.setAlignment(QtCore.Qt.AlignCenter)
        self.invC_out.setObjectName(_fromUtf8("invC_out"))
        self.verticalLayout_6.addWidget(self.invC_out)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addWidget(self.verticalLayout_12)
        self.verticalLayout_5 = QtGui.QWidget(self.horizontalLayout_8)
        self.verticalLayout_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayout_5)
        self.verticalLayout_3.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalFrame_2 = QtGui.QFrame(self.verticalLayout_5)
        self.verticalFrame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.verticalFrame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.verticalFrame_2.setObjectName(_fromUtf8("verticalFrame_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_9 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_8.addWidget(self.label_9)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setMargin(0)
        self.label_4.setIndent(11)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_2 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setIndent(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_7 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_9.addWidget(self.label_7)
        self.label_10 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setIndent(9)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_9.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_9.addWidget(self.label_11)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.dial = QtGui.QDial(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)
        self.dial.setMouseTracking(False)
        self.dial.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.dial.setMaximum(100)
        self.dial.setSingleStep(2)
        self.dial.setPageStep(10)
        self.dial.setTracking(True)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(2.7)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.horizontalLayout_7.addWidget(self.dial)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_14 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_10.addWidget(self.label_14)
        self.label_16 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_16.setIndent(9)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_10.addWidget(self.label_16)
        self.label_15 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_10.addWidget(self.label_15)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem2 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_13 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_6.addWidget(self.label_13)
        self.label_12 = QtGui.QLabel(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        spacerItem3 = QtGui.QSpacerItem(54, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.hmipot_IN = QtGui.QDoubleSpinBox(self.verticalFrame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hmipot_IN.sizePolicy().hasHeightForWidth())
        self.hmipot_IN.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.hmipot_IN.setFont(font)
        self.hmipot_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.hmipot_IN.setAlignment(QtCore.Qt.AlignCenter)
        self.hmipot_IN.setSuffix(_fromUtf8(""))
        self.hmipot_IN.setSingleStep(1.0)
        self.hmipot_IN.setObjectName(_fromUtf8("hmipot_IN"))
        self.verticalLayout_8.addWidget(self.hmipot_IN)
        self.verticalLayout_3.addWidget(self.verticalFrame_2)
        spacerItem4 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalFrame = QtGui.QFrame(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(8)
        self.horizontalFrame.setFont(font)
        self.horizontalFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.horizontalFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.horizontalFrame.setObjectName(_fromUtf8("horizontalFrame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setContentsMargins(12, 9, 12, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_heatON = QtGui.QPushButton(self.horizontalFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_heatON.sizePolicy().hasHeightForWidth())
        self.btn_heatON.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_heatON.setFont(font)
        self.btn_heatON.setMouseTracking(True)
        self.btn_heatON.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 159, 0);"))
        self.btn_heatON.setIconSize(QtCore.QSize(16, 28))
        self.btn_heatON.setAutoDefault(True)
        self.btn_heatON.setObjectName(_fromUtf8("btn_heatON"))
        self.horizontalLayout_3.addWidget(self.btn_heatON)
        self.btn_heatOFF = QtGui.QPushButton(self.horizontalFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_heatOFF.sizePolicy().hasHeightForWidth())
        self.btn_heatOFF.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_heatOFF.setFont(font)
        self.btn_heatOFF.setMouseTracking(True)
        self.btn_heatOFF.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);"))
        self.btn_heatOFF.setIconSize(QtCore.QSize(0, 0))
        self.btn_heatOFF.setAutoDefault(True)
        self.btn_heatOFF.setObjectName(_fromUtf8("btn_heatOFF"))
        self.horizontalLayout_3.addWidget(self.btn_heatOFF)
        self.verticalLayout_3.addWidget(self.horizontalFrame)
        self.horizontalWidget_2 = QtGui.QWidget(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName(_fromUtf8("horizontalWidget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_4.setContentsMargins(12, 9, 12, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btn_bck = QtGui.QPushButton(self.horizontalWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_bck.sizePolicy().hasHeightForWidth())
        self.btn_bck.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_bck.setFont(font)
        self.btn_bck.setMouseTracking(True)
        self.btn_bck.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.btn_bck.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Picture11.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_bck.setIcon(icon)
        self.btn_bck.setIconSize(QtCore.QSize(16, 23))
        self.btn_bck.setAutoDefault(True)
        self.btn_bck.setDefault(False)
        self.btn_bck.setFlat(False)
        self.btn_bck.setObjectName(_fromUtf8("btn_bck"))
        self.horizontalLayout_4.addWidget(self.btn_bck)
        self.verticalLayout_3.addWidget(self.horizontalWidget_2)
        self.horizontalLayout.addWidget(self.verticalLayout_5)
        self.horizontalLayout_2.addWidget(self.horizontalLayout_8)

        self.retranslateUi(MonitorParams)
        QtCore.QMetaObject.connectSlotsByName(MonitorParams)

    def retranslateUi(self, MonitorParams):
        MonitorParams.setWindowTitle(QtGui.QApplication.translate("MonitorParams", "DashBoard", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MonitorParams", "CAP Volt", None, QtGui.QApplication.UnicodeUTF8))
        self.capV_out.setText(QtGui.QApplication.translate("MonitorParams", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MonitorParams", "Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.freq_out.setText(QtGui.QApplication.translate("MonitorParams", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MonitorParams", "OP Volt", None, QtGui.QApplication.UnicodeUTF8))
        self.opV_out.setText(QtGui.QApplication.translate("MonitorParams", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MonitorParams", "INV Current", None, QtGui.QApplication.UnicodeUTF8))
        self.invC_out.setText(QtGui.QApplication.translate("MonitorParams", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MonitorParams", "HMI POT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MonitorParams", "40.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MonitorParams", "50.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MonitorParams", "60.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MonitorParams", "30.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MonitorParams", "20.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MonitorParams", "10.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MonitorParams", "70.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MonitorParams", "80.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MonitorParams", "90.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MonitorParams", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MonitorParams", "100.0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_heatON.setText(QtGui.QApplication.translate("MonitorParams", "Heat ON", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_heatOFF.setText(QtGui.QApplication.translate("MonitorParams", "Heat OFF", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
