# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_controls.ui'
#
# Created: Mon Jul 11 12:01:14 2016
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SetControls(object):
    def setupUi(self, SetControls):
        SetControls.setObjectName(_fromUtf8("SetControls"))
        SetControls.resize(800, 480)
        SetControls.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(SetControls)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_16 = QtGui.QWidget(SetControls)
        self.horizontalLayout_16.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayout_16)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_5 = QtGui.QFrame(self.horizontalLayout_16)
        self.verticalLayout_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.verticalLayout_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.verticalLayout_5.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayout_5)
        self.verticalLayout_3.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_11 = QtGui.QLabel(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.max_current_IN = QtGui.QDoubleSpinBox(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_current_IN.sizePolicy().hasHeightForWidth())
        self.max_current_IN.setSizePolicy(sizePolicy)
        self.max_current_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.max_current_IN.setObjectName(_fromUtf8("max_current_IN"))
        self.verticalLayout_3.addWidget(self.max_current_IN)
        self.label_13 = QtGui.QLabel(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.max_capV_IN = QtGui.QDoubleSpinBox(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_capV_IN.sizePolicy().hasHeightForWidth())
        self.max_capV_IN.setSizePolicy(sizePolicy)
        self.max_capV_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.max_capV_IN.setObjectName(_fromUtf8("max_capV_IN"))
        self.verticalLayout_3.addWidget(self.max_capV_IN)
        self.label_17 = QtGui.QLabel(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_3.addWidget(self.label_17)
        self.high_Q_IN = QtGui.QDoubleSpinBox(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.high_Q_IN.sizePolicy().hasHeightForWidth())
        self.high_Q_IN.setSizePolicy(sizePolicy)
        self.high_Q_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.high_Q_IN.setObjectName(_fromUtf8("high_Q_IN"))
        self.verticalLayout_3.addWidget(self.high_Q_IN)
        self.label_6 = QtGui.QLabel(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.max_pwr_IN = QtGui.QDoubleSpinBox(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_pwr_IN.sizePolicy().hasHeightForWidth())
        self.max_pwr_IN.setSizePolicy(sizePolicy)
        self.max_pwr_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.max_pwr_IN.setObjectName(_fromUtf8("max_pwr_IN"))
        self.verticalLayout_3.addWidget(self.max_pwr_IN)
        self.label_9 = QtGui.QLabel(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.max_voltage_IN = QtGui.QDoubleSpinBox(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_voltage_IN.sizePolicy().hasHeightForWidth())
        self.max_voltage_IN.setSizePolicy(sizePolicy)
        self.max_voltage_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.max_voltage_IN.setObjectName(_fromUtf8("max_voltage_IN"))
        self.verticalLayout_3.addWidget(self.max_voltage_IN)
        self.label_15 = QtGui.QLabel(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_3.addWidget(self.label_15)
        self.max_freq_IN = QtGui.QDoubleSpinBox(self.verticalLayout_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_freq_IN.sizePolicy().hasHeightForWidth())
        self.max_freq_IN.setSizePolicy(sizePolicy)
        self.max_freq_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.max_freq_IN.setObjectName(_fromUtf8("max_freq_IN"))
        self.verticalLayout_3.addWidget(self.max_freq_IN)
        self.horizontalLayout.addWidget(self.verticalLayout_5)
        self.verticalLayout_1 = QtGui.QFrame(self.horizontalLayout_16)
        self.verticalLayout_1.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.verticalLayout_1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.verticalLayout_1.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_1.setObjectName(_fromUtf8("verticalLayout_1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayout_1)
        self.verticalLayout.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_10 = QtGui.QLabel(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.min_current_IN = QtGui.QDoubleSpinBox(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_current_IN.sizePolicy().hasHeightForWidth())
        self.min_current_IN.setSizePolicy(sizePolicy)
        self.min_current_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.min_current_IN.setObjectName(_fromUtf8("min_current_IN"))
        self.verticalLayout.addWidget(self.min_current_IN)
        self.label_12 = QtGui.QLabel(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.min_capV_IN = QtGui.QDoubleSpinBox(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_capV_IN.sizePolicy().hasHeightForWidth())
        self.min_capV_IN.setSizePolicy(sizePolicy)
        self.min_capV_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.min_capV_IN.setObjectName(_fromUtf8("min_capV_IN"))
        self.verticalLayout.addWidget(self.min_capV_IN)
        self.label_16 = QtGui.QLabel(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout.addWidget(self.label_16)
        self.low_Q_IN = QtGui.QDoubleSpinBox(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.low_Q_IN.sizePolicy().hasHeightForWidth())
        self.low_Q_IN.setSizePolicy(sizePolicy)
        self.low_Q_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.low_Q_IN.setObjectName(_fromUtf8("low_Q_IN"))
        self.verticalLayout.addWidget(self.low_Q_IN)
        self.label_7 = QtGui.QLabel(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.min_pwr_IN = QtGui.QDoubleSpinBox(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_pwr_IN.sizePolicy().hasHeightForWidth())
        self.min_pwr_IN.setSizePolicy(sizePolicy)
        self.min_pwr_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.min_pwr_IN.setObjectName(_fromUtf8("min_pwr_IN"))
        self.verticalLayout.addWidget(self.min_pwr_IN)
        self.label_8 = QtGui.QLabel(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.min_voltage_IN = QtGui.QDoubleSpinBox(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_voltage_IN.sizePolicy().hasHeightForWidth())
        self.min_voltage_IN.setSizePolicy(sizePolicy)
        self.min_voltage_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.min_voltage_IN.setObjectName(_fromUtf8("min_voltage_IN"))
        self.verticalLayout.addWidget(self.min_voltage_IN)
        self.label_14 = QtGui.QLabel(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout.addWidget(self.label_14)
        self.min_freq_IN = QtGui.QDoubleSpinBox(self.verticalLayout_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_freq_IN.sizePolicy().hasHeightForWidth())
        self.min_freq_IN.setSizePolicy(sizePolicy)
        self.min_freq_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.min_freq_IN.setObjectName(_fromUtf8("min_freq_IN"))
        self.verticalLayout.addWidget(self.min_freq_IN)
        self.horizontalLayout.addWidget(self.verticalLayout_1)
        self.verticalLayout_4 = QtGui.QFrame(self.horizontalLayout_16)
        self.verticalLayout_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 139, 255);"))
        self.verticalLayout_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.verticalLayout_4.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayout_4)
        self.verticalLayout_2.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.currentTrip_IN = QtGui.QDoubleSpinBox(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTrip_IN.sizePolicy().hasHeightForWidth())
        self.currentTrip_IN.setSizePolicy(sizePolicy)
        self.currentTrip_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.currentTrip_IN.setObjectName(_fromUtf8("currentTrip_IN"))
        self.verticalLayout_2.addWidget(self.currentTrip_IN)
        self.label_2 = QtGui.QLabel(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.capVTrip_IN = QtGui.QDoubleSpinBox(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capVTrip_IN.sizePolicy().hasHeightForWidth())
        self.capVTrip_IN.setSizePolicy(sizePolicy)
        self.capVTrip_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.capVTrip_IN.setObjectName(_fromUtf8("capVTrip_IN"))
        self.verticalLayout_2.addWidget(self.capVTrip_IN)
        self.label_3 = QtGui.QLabel(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.QTrip_IN = QtGui.QDoubleSpinBox(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QTrip_IN.sizePolicy().hasHeightForWidth())
        self.QTrip_IN.setSizePolicy(sizePolicy)
        self.QTrip_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.QTrip_IN.setObjectName(_fromUtf8("QTrip_IN"))
        self.verticalLayout_2.addWidget(self.QTrip_IN)
        self.label_4 = QtGui.QLabel(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.ctrl_IN = QtGui.QComboBox(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrl_IN.sizePolicy().hasHeightForWidth())
        self.ctrl_IN.setSizePolicy(sizePolicy)
        self.ctrl_IN.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ctrl_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ctrl_IN.setObjectName(_fromUtf8("ctrl_IN"))
        self.ctrl_IN.addItem(_fromUtf8(""))
        self.ctrl_IN.addItem(_fromUtf8(""))
        self.ctrl_IN.addItem(_fromUtf8(""))
        self.ctrl_IN.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.ctrl_IN)
        self.label_5 = QtGui.QLabel(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.feedback_IN = QtGui.QComboBox(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feedback_IN.sizePolicy().hasHeightForWidth())
        self.feedback_IN.setSizePolicy(sizePolicy)
        self.feedback_IN.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.feedback_IN.setObjectName(_fromUtf8("feedback_IN"))
        self.feedback_IN.addItem(_fromUtf8(""))
        self.feedback_IN.addItem(_fromUtf8(""))
        self.feedback_IN.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.feedback_IN)
        spacerItem = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(1)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem1 = QtGui.QSpacerItem(131, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.btn_bck = QtGui.QPushButton(self.verticalLayout_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_bck.sizePolicy().hasHeightForWidth())
        self.btn_bck.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
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
        self.btn_bck.setIconSize(QtCore.QSize(16, 16))
        self.btn_bck.setAutoDefault(True)
        self.btn_bck.setObjectName(_fromUtf8("btn_bck"))
        self.horizontalLayout_13.addWidget(self.btn_bck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout.addWidget(self.verticalLayout_4)
        self.horizontalLayout_2.addWidget(self.horizontalLayout_16)

        self.retranslateUi(SetControls)
        self.ctrl_IN.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SetControls)

    def retranslateUi(self, SetControls):
        SetControls.setWindowTitle(QtGui.QApplication.translate("SetControls", " Set Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("SetControls", "Max. Current", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("SetControls", "Max. CAP Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("SetControls", "High Q", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SetControls", "Max. Power", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("SetControls", "Max. Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("SetControls", "Max. Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("SetControls", "Min Current", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("SetControls", "Min. CAP Volatge", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("SetControls", "Low Q", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SetControls", "Min Power", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SetControls", "Min. Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("SetControls", "Min. Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SetControls", "Current Trip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SetControls", "CAP Volatge Trip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SetControls", " Q Trip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SetControls", "Control Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrl_IN.setItemText(0, QtGui.QApplication.translate("SetControls", "Local POT", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrl_IN.setItemText(1, QtGui.QApplication.translate("SetControls", "Remote POT", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrl_IN.setItemText(2, QtGui.QApplication.translate("SetControls", "PLC POT", None, QtGui.QApplication.UnicodeUTF8))
        self.ctrl_IN.setItemText(3, QtGui.QApplication.translate("SetControls", "HMI POT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SetControls", "Feedback Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.feedback_IN.setItemText(0, QtGui.QApplication.translate("SetControls", "Power Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.feedback_IN.setItemText(1, QtGui.QApplication.translate("SetControls", "Voltage Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.feedback_IN.setItemText(2, QtGui.QApplication.translate("SetControls", "Current Mode", None, QtGui.QApplication.UnicodeUTF8))

import images_rc