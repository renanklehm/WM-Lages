"""PyQT imports"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem

"""GUI Draw imports"""
from GUI.MainWindow.DrawMainWindow import Ui_MainWindow
from GUI.BuscarPedido.DrawBuscarPedido import Ui_DIALOG_BuscaPedido
from GUI.EditarCNTR.DrawEditarCNTR import Ui_DIALOG_EditarCNTR
from GUI.EditarViagem.DrawEditarViagem import Ui_DIALOG_EditarViagem
from GUI.EditarBooking.DrawEditarBooking import Ui_DIALOG_NovoBooking

from DataBase import *
from DateTools import *
from Objects import *

import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.dataBase = DataBaseConnection()
        self.dateTools = DateTolls()
        self.setupUi(self)
        self.setupConnections()
        self.setupComboBox()
        self.DATE_DataViagem.setDate(self.dateTools.today)
        self.FillCNTRTable()
        self.FillViagensTable()

    def setupConnections(self):
        self.PBT_Salvar.clicked.connect(self.SalvarBooking)
        self.PBT_Novo.clicked.connect(self.ShowNovoBooking)
        self.PBT_Buscar.clicked.connect(self.ShowBuscarBooking)
        self.PBT_Excluir.clicked.connect(self.ExcluirBooking)
        self.PBT_ExcluirCNTR.clicked.connect(self.ExcluirCNTR)
        self.PBT_AplicarFiltro.clicked.connect(self.FillCNTRTable)
        self.PBT_EditarCNTR.clicked.connect(lambda: self.ShowEditarCNTR(False))
        self.PBT_IncluirCNTR.clicked.connect(lambda: self.ShowEditarCNTR(True))
        self.PBT_NovaViagem.clicked.connect(lambda: self.ShowEditarViagem(True))
        self.PBT_FiltroViagem.clicked.connect(self.FillViagensTable)
        self.TABLE_Status.cellClicked.connect(self.AllowEdit)
    
    def setupComboBox(self):
        self.CBX_Fabrica.clear()
        self.CBX_Porto.clear()
        self.CBX_Status.clear()
        self.CBX_StatusEstoque.clear()
        self.CBX_Fabrica.addItems(self.dataBase.GetFabricas())
        self.CBX_Porto.addItems(list(self.dataBase.GetPortos()))
        self.CBX_Status.addItems(list(self.dataBase.GetStatusPedido()))
        self.CBX_StatusEstoque.addItems(list(self.dataBase.GetStatusCNTR()))
        self.CBX_Status.setCurrentText('')
        self.CBX_StatusEstoque.setCurrentText('')

    #region SaveCalls
    def SalvarBooking(self):
        ### FALTA FAZER ###
        return
    #endregion

    #region LoadCalls
    def OpenBooking(self, booking):
        datastream = self.dataBase.OpenBooking(str(booking))
        self.TXB_Booking.setText(str(datastream[1]))
        self.CBX_Status.setCurrentText(str(datastream[2]))
        self.CHB_Cabotagem.setChecked(bool(datastream[3]))
        self.CBX_Fabrica.setCurrentText(str(datastream[4]))
        self.CBX_Porto.setCurrentText(str(datastream[5]))
        self.DATE_DL_Fabrica.setDate(self.dateTools.GetDate(datastream[6]))
        self.DATE_DL_Porto.setDate(self.dateTools.GetDate(datastream[8]))
        self.DATE_InicioJanela.setDate(self.dateTools.GetDate(datastream[8]))
        self.DATE_FimJanela.setDate(self.dateTools.GetDate(datastream[9]))
        self.FillBookingTable(str(datastream[1]))
    #endregion

    #region DeleteCalls
    def ExcluirBooking(self):
        self.dataBase.DeleteBooking(self.TXB_Pedido.text())
        self.NovoBooking()
    
    def ExcluirCNTR(self):
        index = (self.TABLE_Estoque.selectionModel().currentIndex())
        value = index.sibling(index.row(), 0).data()
        self.dataBase.DeleteCNTR(value)
        self.FillCNTRTable()
    #endregion

    #region FillCalls
    def FillBookingTable(self, booking):
        self.TABLE_Status.clear()
        
        dataStream = self.dataBase.FillBookingTable(booking)

        names = ['ID', 'Oferta', 'Container', 'Status', 'Tara', 'Terminal', 'Armador', 'CPF', 'Motorista', 'Placa Cavalo', 'Placa Carreta', 'Expurgo']
        self.TABLE_Status.setRowCount(len(dataStream))
        self.TABLE_Status.setHorizontalHeaderLabels(names)

        for row in range(len(dataStream)):

            for col in range(len(dataStream[row])):
                
                self.TABLE_Status.setItem(row, col, QTableWidgetItem(str(dataStream[row][col])))
    
    def FillCNTRTable(self):

        self.TABLE_Estoque.clear()
        
        dataStream = self.dataBase.FillCNTRTable(self.TXB_BK.text(),
                                                 self.TXB_CNTR.text(),
                                                 self.CBX_StatusEstoque.currentText())

        names = ['Container', 'Booking', 'Status', 'Freetime', 'Armador', 'Terminal', 'Tara', 'Expurgo', 'CPF', 'Motorista', 'Placa Cavalo', 'Placa Carreta', 'OBS']
        
        self.TABLE_Estoque.setRowCount(len(dataStream))
        self.TABLE_Estoque.setHorizontalHeaderLabels(names)

        for row in range(len(dataStream)):

            for col in range(len(dataStream[row])):

                self.TABLE_Estoque.setItem(row, col, QTableWidgetItem(str(dataStream[row][col])))
    
    def FillViagensTable(self):

        self.TABLE_Viagens.clear()
        
        dataStream = self.dataBase.FillViagensTable(self.TXB_CNTRViagem.text(),
                                                    self.TXB_BookingViagem.text(),
                                                    self.CBX_StatusViagem.currentText(),
                                                    self.DATE_DataViagem.text(),
                                                    bool(self.CHB_SelectALL.isChecked()))

        names = ['ID', 'Status', 'Booking', 'CNTR', 'Início', 'Fim', 'CPF', 'Motorista', 'Placa Cavalo', 'Placa Carreta', 'Spot']
        
        self.TABLE_Viagens.setRowCount(len(dataStream))
        self.TABLE_Viagens.setHorizontalHeaderLabels(names)

        for row in range(len(dataStream)):

            for col in range(len(dataStream[row])):

                self.TABLE_Viagens.setItem(row, col, QTableWidgetItem(str(dataStream[row][col])))
    #endregion

    #region ShowCalls
    def ShowNovoBooking(self):
        self.editarBookingDialog = EditarBookingDialog(self)
        self.editarBookingDialog.show()
    
    def ShowBuscarBooking(self):
        self.buscarBookingDialog = BuscarBookingDialog(self)
        self.buscarBookingDialog.show()

    def ShowEditarCNTR(self, isNew):
        if (isNew):
            self.editarCNTRDialog = EditarCNTRDialog(self)
        else:
            index = (self.TABLE_Estoque.selectionModel().currentIndex())
            value = index.sibling(index.row(), 0).data()
            self.editarCNTRDialog = EditarCNTRDialog(self, value)
        
        self.editarCNTRDialog.show()
    
    def ShowEditarViagem(self, isNew):
        if (isNew):
            self.editarViagemDialog = EditarViagemDialog(self)
        
        self.editarViagemDialog.show()
    #endregion

    def AllowEdit(self):

        index = (self.TABLE_Status.selectionModel().currentIndex())
        print(index.column)
        if (index.column == 2):
            self.TABLE_Status.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        else:
            self.TABLE_Status.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

class EditarBookingDialog(QtWidgets.QDialog, Ui_DIALOG_NovoBooking):
    def __init__(self, _parentWindow, parent=None):
        super(EditarBookingDialog, self).__init__(parent)
        self.dataBase = DataBaseConnection()
        self.dateTools = DateTolls()
        self.parentWindow = _parentWindow
        self.setupUi(self)
        self.setupConnections()
        self.setupComboBox()

    def setupConnections(self):        
        self.PBT_Gravar.clicked.connect(self.SaveBooking)
    
    def setupComboBox(self):
        self.DATE_DL_Fabrica.setDate(self.dateTools.today)
        self.DATE_DL_Porto.setDate(self.dateTools.today)
        self.DATE_InicioJanela.setDate(self.dateTools.today)
        self.DATE_FimJanela.setDate(self.dateTools.today)
        self.CBX_Fabrica.addItems(self.dataBase.GetFabricas())
        self.CBX_Porto.addItems(self.dataBase.GetPortos())
    
    def SaveBooking(self):
        novoBooking = Booking(self.TXB_Booking.text(),
                              'Aberto',
                              self.CHB_Cabotagem.isChecked(),
                              self.CBX_Fabrica.currentText(),
                              self.CBX_Porto.currentText(),
                              self.DATE_DL_Fabrica.text(),
                              self.DATE_DL_Porto.text(),
                              self.DATE_InicioJanela.text(),
                              self.DATE_FimJanela.text(),
                              self.SBX_QtdePedido.text())
        
        self.dataBase.SaveBooking(novoBooking)
        self.CreateOfertas(int(self.SBX_QtdePedido.text()), 
                           self.TXB_Booking.text())
        self.parentWindow.OpenBooking(novoBooking.booking)
        self.hide()
    
    def CreateOfertas(self, qtde, booking):
        novaOferta = Oferta(booking)
        self.dataBase.NewOferta(novaOferta, qtde)

class EditarCNTRDialog(QtWidgets.QDialog, Ui_DIALOG_EditarCNTR):
    def __init__(self, _parentWindow, cntr = None, parent = None):
        super(EditarCNTRDialog, self).__init__(parent)
        self.parentWindow = _parentWindow
        self.dataBase = DataBaseConnection()
        self.dateTools = DateTolls()
        self.setupUi(self)
        self.setupConnections()
        self.setupComboBox()

        if (cntr == None):
            self.DATE_Coleta.setDate(self.dateTools.today)
        else:
            self.OpenCNTR(cntr)

    def setupConnections(self):
        self.PBT_Gravar.clicked.connect(self.SalvarCNTR)
        self.PBT_Cancelar.clicked.connect(self.Fechar)

    def setupComboBox(self):
        self.CBX_Armador.clear()
        self.CBX_Status.clear()
        self.CBX_TerminalVazio.clear()
        self.CBX_Armador.addItems(self.dataBase.GetArmadores())
        self.CBX_Status.addItems(self.dataBase.GetStatusCNTR())
        self.CBX_TerminalVazio.addItems(self.dataBase.GetTerminais())

    def Fechar(self):
        self.hide()

    #region SaveCalls
    def SalvarCNTR(self):
        novoCNTR = CNTR(
                        self.TXB_Unidade.text(),
                        self.CBX_Status.currentText(),
                        self.TXB_Booking.text(),
                        self.SBX_Tara.text(),
                        self.CBX_Armador.currentText(),
                        self.CBX_TerminalVazio.currentText(),
                        self.DATE_Coleta.text(),
                        20,                                            #GAMBIARRA
                        '',
                        int(self.CHB_Expurgo.isChecked())
                        )
        
        self.dataBase.SaveCNTR(novoCNTR)
        self.parentWindow.FillCNTRTable()
        self.Fechar()
    #endregion

    #region LoadCalls
    def OpenCNTR(self, cntr):
        dataStream = self.dataBase.OpenCNTR(cntr)
        self.TXB_Unidade.setText(dataStream[0])
        self.CBX_Status.setCurrentText(dataStream[2])
        self.TXB_Booking.setText(dataStream[3])
        self.SBX_Tara.setValue(dataStream[4])
        self.CBX_Armador.setCurrentText(dataStream[5])
        self.CBX_TerminalVazio.setCurrentText(dataStream[6])
        self.DATE_Coleta.setDate(self.dateTools.GetDate(dataStream[7]))
        self.CHB_Expurgo.setChecked(bool(dataStream[10]))
    #endregion

class BuscarBookingDialog(QtWidgets.QDialog, Ui_DIALOG_BuscaPedido):
    def __init__(self, _parentWindow, parent = None):
        super(BuscarBookingDialog, self).__init__(parent)
        self.parentWindow = _parentWindow
        self.setupUi(self)
        self.setupConnections()
        self.dataBase = DataBaseConnection()
        self.FillTable()
    
    def setupConnections(self):
        self.TXB_Busca.editingFinished.connect(self.FillTable)
        self.PBT_Selecionar.clicked.connect(self.SelecionarPedido)

    #region FillCalls
    def FillTable(self):
        self.TABLE_BuscarPedido.clear()

        dataStream = self.dataBase.FillBookingSearch(self.TXB_Busca.text())

        names = ['Booking', 'Status', 'Dead Line']
        self.TABLE_BuscarPedido.setRowCount(len(dataStream))
        self.TABLE_BuscarPedido.setHorizontalHeaderLabels(names)

        for row in range(len(dataStream)):

            for col in range(len(dataStream[row])):

                self.TABLE_BuscarPedido.setItem(row, col, QTableWidgetItem(str(dataStream[row][col])))
    #endregion

    #region SelectCalls
    def SelecionarPedido(self):
        index = (self.TABLE_BuscarPedido.selectionModel().currentIndex())
        value = index.sibling(index.row(), 0).data()
        
        self.parentWindow.OpenBooking(value)
        self.hide()
    #endregion

class EditarViagemDialog(QtWidgets.QDialog, Ui_DIALOG_EditarViagem):
    def __init__(self, _parentWindow, viagem = None, parent=None):
        super(EditarViagemDialog, self).__init__(parent)
        self.dataBase = DataBaseConnection()
        self.dateTools = DateTolls()
        self.parentWindow = _parentWindow
        self.setupUi(self)
        self.setupConnections()
        self.setupComboBox()

        if (viagem == None):
            self.DATE_Fim.setDate(self.dateTools.today)
            self.DATE_Inicio.setDate(self.dateTools.today)

    def setupConnections(self):
        self.TXB_CPF.editingFinished.connect(self.AutoFillConjunto)
        self.PBT_Gravar.clicked.connect(self.SaveViagem)
        self.PBT_Cancelar.clicked.connect(self.Fechar)
    
    def setupComboBox(self):
        self.CBX_Carreta.clear()
        self.CBX_Cavalo.clear()
        self.CBX_Destino.clear()
        self.CBX_Motorista.clear()
        self.CBX_Origem.clear()
        self.CBX_StatusViagem.clear()
        self.CBX_TipoViagem.clear()
        self.CBX_Motorista.addItems(self.dataBase.GetMotorista())
        self.CBX_Cavalo.addItems(self.dataBase.GetCavalo())
        self.CBX_Carreta.addItems(self.dataBase.GetCarreta())
        self.CBX_Origem.addItems(self.dataBase.GetTerminais())
        self.CBX_Origem.addItems(self.dataBase.GetFabricas())
        self.CBX_Destino.addItems(self.dataBase.GetFabricas())
        self.CBX_Destino.addItems(self.dataBase.GetPortos())
        self.CBX_StatusViagem.addItems(self.dataBase.GetStatusViagem())
        self.CBX_TipoViagem.addItems(self.dataBase.GetTipoViagem())
    
    def Fechar(self):
        self.hide()

    def AutoFillConjunto(self):
        cpf = self.TXB_CPF.text()
        self.CBX_Motorista.setCurrentText(self.dataBase.GetMotorista(cpf))
        self.CBX_Cavalo.setCurrentText(self.dataBase.GetCavalo(cpf))
        self.CBX_Carreta.setCurrentText(self.dataBase.GetCarreta(cpf))

    def SaveViagem(self):
        NovaViagem = Viagem(self.CBX_StatusViagem.currentText(),
                            self.TXB_CNTR.text(),
                            self.CBX_TipoViagem.currentText(),
                            self.DATE_Inicio.text(),
                            self.DATE_Fim.text(),
                            self.CBX_Origem.currentText(),
                            self.CBX_Destino.currentText(),
                            self.TXB_CPF.text(),
                            self.CBX_Motorista.currentText(),
                            self.CBX_Cavalo.currentText(),
                            self.CBX_Carreta.currentText(),
                            int(self.CHB_Spot.isChecked()))
        
        self.dataBase.SaveViagem(NovaViagem)
        self.parentWindow.FillViagensTable()
        self.Fechar()

