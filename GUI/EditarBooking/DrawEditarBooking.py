# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarBooking.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DIALOG_NovoBooking(object):
    def setupUi(self, DIALOG_NovoBooking):
        DIALOG_NovoBooking.setObjectName("DIALOG_NovoBooking")
        DIALOG_NovoBooking.resize(417, 233)
        self.LBL_DL_Fabrica = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_DL_Fabrica.setGeometry(QtCore.QRect(10, 120, 110, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_DL_Fabrica.sizePolicy().hasHeightForWidth())
        self.LBL_DL_Fabrica.setSizePolicy(sizePolicy)
        self.LBL_DL_Fabrica.setMaximumSize(QtCore.QSize(110, 16777215))
        self.LBL_DL_Fabrica.setObjectName("LBL_DL_Fabrica")
        self.DATE_FimJanela = QtWidgets.QDateEdit(DIALOG_NovoBooking)
        self.DATE_FimJanela.setGeometry(QtCore.QRect(130, 180, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DATE_FimJanela.sizePolicy().hasHeightForWidth())
        self.DATE_FimJanela.setSizePolicy(sizePolicy)
        self.DATE_FimJanela.setMinimumSize(QtCore.QSize(110, 0))
        self.DATE_FimJanela.setMaximumSize(QtCore.QSize(110, 16777215))
        self.DATE_FimJanela.setCalendarPopup(True)
        self.DATE_FimJanela.setObjectName("DATE_FimJanela")
        self.DATE_DL_Fabrica = QtWidgets.QDateEdit(DIALOG_NovoBooking)
        self.DATE_DL_Fabrica.setGeometry(QtCore.QRect(10, 138, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DATE_DL_Fabrica.sizePolicy().hasHeightForWidth())
        self.DATE_DL_Fabrica.setSizePolicy(sizePolicy)
        self.DATE_DL_Fabrica.setMinimumSize(QtCore.QSize(110, 0))
        self.DATE_DL_Fabrica.setMaximumSize(QtCore.QSize(110, 16777215))
        self.DATE_DL_Fabrica.setCalendarPopup(True)
        self.DATE_DL_Fabrica.setObjectName("DATE_DL_Fabrica")
        self.SBX_QtdePedido = QtWidgets.QSpinBox(DIALOG_NovoBooking)
        self.SBX_QtdePedido.setGeometry(QtCore.QRect(10, 86, 110, 20))
        self.SBX_QtdePedido.setMaximum(1000)
        self.SBX_QtdePedido.setObjectName("SBX_QtdePedido")
        self.DATE_InicioJanela = QtWidgets.QDateEdit(DIALOG_NovoBooking)
        self.DATE_InicioJanela.setGeometry(QtCore.QRect(130, 138, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DATE_InicioJanela.sizePolicy().hasHeightForWidth())
        self.DATE_InicioJanela.setSizePolicy(sizePolicy)
        self.DATE_InicioJanela.setMinimumSize(QtCore.QSize(110, 0))
        self.DATE_InicioJanela.setMaximumSize(QtCore.QSize(110, 16777215))
        self.DATE_InicioJanela.setCalendarPopup(True)
        self.DATE_InicioJanela.setObjectName("DATE_InicioJanela")
        self.LBL_FimJanela = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_FimJanela.setGeometry(QtCore.QRect(130, 163, 110, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_FimJanela.sizePolicy().hasHeightForWidth())
        self.LBL_FimJanela.setSizePolicy(sizePolicy)
        self.LBL_FimJanela.setMinimumSize(QtCore.QSize(110, 0))
        self.LBL_FimJanela.setMaximumSize(QtCore.QSize(110, 16777215))
        self.LBL_FimJanela.setObjectName("LBL_FimJanela")
        self.DATE_DL_Porto = QtWidgets.QDateEdit(DIALOG_NovoBooking)
        self.DATE_DL_Porto.setGeometry(QtCore.QRect(10, 180, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DATE_DL_Porto.sizePolicy().hasHeightForWidth())
        self.DATE_DL_Porto.setSizePolicy(sizePolicy)
        self.DATE_DL_Porto.setMinimumSize(QtCore.QSize(110, 0))
        self.DATE_DL_Porto.setMaximumSize(QtCore.QSize(110, 16777215))
        self.DATE_DL_Porto.setCalendarPopup(True)
        self.DATE_DL_Porto.setObjectName("DATE_DL_Porto")
        self.LBL_Porto = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_Porto.setGeometry(QtCore.QRect(130, 63, 110, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_Porto.sizePolicy().hasHeightForWidth())
        self.LBL_Porto.setSizePolicy(sizePolicy)
        self.LBL_Porto.setMinimumSize(QtCore.QSize(110, 0))
        self.LBL_Porto.setMaximumSize(QtCore.QSize(110, 16777215))
        self.LBL_Porto.setObjectName("LBL_Porto")
        self.CHB_Cabotagem = QtWidgets.QCheckBox(DIALOG_NovoBooking)
        self.CHB_Cabotagem.setGeometry(QtCore.QRect(10, 210, 110, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CHB_Cabotagem.sizePolicy().hasHeightForWidth())
        self.CHB_Cabotagem.setSizePolicy(sizePolicy)
        self.CHB_Cabotagem.setMinimumSize(QtCore.QSize(110, 0))
        self.CHB_Cabotagem.setMaximumSize(QtCore.QSize(110, 16777215))
        self.CHB_Cabotagem.setObjectName("CHB_Cabotagem")
        self.LBL_InicioJanela = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_InicioJanela.setGeometry(QtCore.QRect(130, 120, 110, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_InicioJanela.sizePolicy().hasHeightForWidth())
        self.LBL_InicioJanela.setSizePolicy(sizePolicy)
        self.LBL_InicioJanela.setMinimumSize(QtCore.QSize(110, 0))
        self.LBL_InicioJanela.setMaximumSize(QtCore.QSize(110, 16777215))
        self.LBL_InicioJanela.setObjectName("LBL_InicioJanela")
        self.CBX_Fabrica = QtWidgets.QComboBox(DIALOG_NovoBooking)
        self.CBX_Fabrica.setGeometry(QtCore.QRect(130, 38, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CBX_Fabrica.sizePolicy().hasHeightForWidth())
        self.CBX_Fabrica.setSizePolicy(sizePolicy)
        self.CBX_Fabrica.setMinimumSize(QtCore.QSize(110, 0))
        self.CBX_Fabrica.setMaximumSize(QtCore.QSize(110, 16777215))
        self.CBX_Fabrica.setObjectName("CBX_Fabrica")
        self.LBL_Booking = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_Booking.setGeometry(QtCore.QRect(10, 20, 110, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_Booking.sizePolicy().hasHeightForWidth())
        self.LBL_Booking.setSizePolicy(sizePolicy)
        self.LBL_Booking.setMaximumSize(QtCore.QSize(110, 16777215))
        self.LBL_Booking.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBL_Booking.setObjectName("LBL_Booking")
        self.CBX_Porto = QtWidgets.QComboBox(DIALOG_NovoBooking)
        self.CBX_Porto.setGeometry(QtCore.QRect(130, 86, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CBX_Porto.sizePolicy().hasHeightForWidth())
        self.CBX_Porto.setSizePolicy(sizePolicy)
        self.CBX_Porto.setMinimumSize(QtCore.QSize(110, 0))
        self.CBX_Porto.setMaximumSize(QtCore.QSize(110, 16777215))
        self.CBX_Porto.setObjectName("CBX_Porto")
        self.LBL_DL_Porto = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_DL_Porto.setGeometry(QtCore.QRect(10, 163, 110, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_DL_Porto.sizePolicy().hasHeightForWidth())
        self.LBL_DL_Porto.setSizePolicy(sizePolicy)
        self.LBL_DL_Porto.setMaximumSize(QtCore.QSize(110, 16777215))
        self.LBL_DL_Porto.setObjectName("LBL_DL_Porto")
        self.LBL_QtdePedido = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_QtdePedido.setGeometry(QtCore.QRect(10, 63, 110, 13))
        self.LBL_QtdePedido.setObjectName("LBL_QtdePedido")
        self.TXB_Booking = QtWidgets.QLineEdit(DIALOG_NovoBooking)
        self.TXB_Booking.setGeometry(QtCore.QRect(10, 38, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TXB_Booking.sizePolicy().hasHeightForWidth())
        self.TXB_Booking.setSizePolicy(sizePolicy)
        self.TXB_Booking.setMinimumSize(QtCore.QSize(110, 0))
        self.TXB_Booking.setMaximumSize(QtCore.QSize(110, 16777215))
        self.TXB_Booking.setObjectName("TXB_Booking")
        self.LBL_Fabrica = QtWidgets.QLabel(DIALOG_NovoBooking)
        self.LBL_Fabrica.setGeometry(QtCore.QRect(130, 20, 110, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBL_Fabrica.sizePolicy().hasHeightForWidth())
        self.LBL_Fabrica.setSizePolicy(sizePolicy)
        self.LBL_Fabrica.setMinimumSize(QtCore.QSize(110, 0))
        self.LBL_Fabrica.setMaximumSize(QtCore.QSize(110, 16777215))
        self.LBL_Fabrica.setObjectName("LBL_Fabrica")
        self.PBT_Gravar = QtWidgets.QPushButton(DIALOG_NovoBooking)
        self.PBT_Gravar.setGeometry(QtCore.QRect(300, 130, 101, 41))
        self.PBT_Gravar.setObjectName("PBT_Gravar")
        self.PBT_Cancelar = QtWidgets.QPushButton(DIALOG_NovoBooking)
        self.PBT_Cancelar.setGeometry(QtCore.QRect(300, 180, 101, 41))
        self.PBT_Cancelar.setObjectName("PBT_Cancelar")

        self.retranslateUi(DIALOG_NovoBooking)
        QtCore.QMetaObject.connectSlotsByName(DIALOG_NovoBooking)

    def retranslateUi(self, DIALOG_NovoBooking):
        _translate = QtCore.QCoreApplication.translate
        DIALOG_NovoBooking.setWindowTitle(_translate("DIALOG_NovoBooking", "Novo Booking"))
        self.LBL_DL_Fabrica.setText(_translate("DIALOG_NovoBooking", "Deadline da Fábrica"))
        self.LBL_FimJanela.setText(_translate("DIALOG_NovoBooking", "Fim da Janela"))
        self.LBL_Porto.setText(_translate("DIALOG_NovoBooking", "Porto"))
        self.CHB_Cabotagem.setText(_translate("DIALOG_NovoBooking", "Cabotagem"))
        self.LBL_InicioJanela.setText(_translate("DIALOG_NovoBooking", "Inicio da Janela"))
        self.LBL_Booking.setText(_translate("DIALOG_NovoBooking", "Booking"))
        self.LBL_DL_Porto.setText(_translate("DIALOG_NovoBooking", "Deadline do Porto"))
        self.LBL_QtdePedido.setText(_translate("DIALOG_NovoBooking", "Quantidade"))
        self.LBL_Fabrica.setText(_translate("DIALOG_NovoBooking", "Fábrica"))
        self.PBT_Gravar.setText(_translate("DIALOG_NovoBooking", "Gravar"))
        self.PBT_Cancelar.setText(_translate("DIALOG_NovoBooking", "Cancelar"))
