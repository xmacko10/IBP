# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_draft.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import csv
import os

from PyQt5 import QtCore, QtWidgets, QtGui

from back.high import vm, disk, host
from back.suplementary.config_file import create_config_file
from front.suplementary.decorators import header_signal
from front.suplementary.tab_sockets import (VmTab, DiskTab, HostTab)


# class CheckableComboBox(QtWidgets.QComboBox):
#     # once there is a checkState set, it is rendered
#     # here we assume default Unchecked
#     def addItem(self, item):
#         super(CheckableComboBox, self).addItem(item)
#         item = self.model().item(self.count()-1, 0)
#         item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
#         item.setCheckState(QtCore.Qt.Unchecked)
#
#     def itemChecked(self, index):
#         item = self.model().item(index, 0)
#         return item.checkState() == QtCore.Qt.Checked

# class RefreshButton(QtWidgets.QAbstractButton):
#
#     def __init__(self, parent):
#         super(RefreshButton, self).__init__(parent)


# class CheckableComboBox(QtWidgets.QComboBox):
#     def __init__(self):
#         super(CheckableComboBox, self).__init__()
#         self.view().pressed.connect(self.handleItemPressed)
#         self.setModel(QtGui.QStandardItemModel(self))
#
#     # def flags(self, index):
#     #     return QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
#
#     def handleItemPressed(self, index):
#         item = self.model().itemFromIndex(index)
#         if item.checkState() == QtCore.Qt.Checked:
#             item.setCheckState(QtCore.Qt.Unchecked)
#         else:
#             item.setCheckState(QtCore.Qt.Checked)



class Ui_MainWindow(object):

    # def __init__(self, parent, data_list, flags, connection, headers_list):
    def __init__(
            self, parent, connection, vm_table, disk_table, host_table,):
        self.parent = parent
        self.connection = connection
        # self.vm_tab = VmTab(table=vm_table, parent=parent)
        # self.disk_tab = DiskTab(table=disk_table, parent=parent)
        # self.host_tab = HostTab(table=host_table, parent=parent)
        # self.tplt_table = TpltTab(table=tplt_table, parent=parent)

        self.tabs_dict = {0: VmTab(table=vm_table, parent=parent),
                          1: DiskTab(table=disk_table, parent=parent),
                          2: HostTab(table=host_table, parent=parent)
                          }
        self.current_tab = None

    def setupUi(self, MainWindow):

        dir_name = os.path.dirname(__file__)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # ------------------------------
        # self.vm_tab.table_layout = self.verticalLayout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # self.vm_tab.table_layout = self.verticalLayout
        self.tabs_dict[0].table_layout = self.verticalLayout
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.toolbutton = QtWidgets.QToolButton(self.centralwidget)
        self.toolbutton.setText('Select Column ')
        self.toolmenu = QtWidgets.QMenu(self.centralwidget)
        # for i in range(len(self.vm_tab.values_table.col_flags)-1):
        for i in range(len(self.tabs_dict[0].values_table.col_flags) - 1):
            action = self.toolmenu.addAction("Column " + str(i))
            action.setCheckable(True)
            # action.setChecked(True)
            # action.setChecked(self.vm_tab.values_table.col_flags[i - 1])
            action.setChecked(self.tabs_dict[0].values_table.col_flags[i + 1])
            action.changed.connect(self.checkbox_clicked)
            # self.vm_tab.chbox_list.append(action)
            self.tabs_dict[0].chbox_list.append(action)
        self.toolbutton.setMenu(self.toolmenu)
        self.toolbutton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.verticalLayout_2.addWidget(self.toolbutton)

        # self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        #
        # self.checkBox_3.setCheckState(2)
        #
        # self.checkBox_3.setObjectName("checkBox_3")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_3)
        # self.checkBox_3.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_4.addWidget(self.checkBox_3)
        # self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        # self.checkBox_2.setObjectName("checkBox_2")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_2)
        # self.checkBox_2.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_4.addWidget(self.checkBox_2)
        # self.checkBox = QtWidgets.QCheckBox(self.tab)
        # self.checkBox.setObjectName("checkBox")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox)
        # self.checkBox.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_4.addWidget(self.checkBox)
        # self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        # self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        # self.checkBox_5.setObjectName("checkBox_5")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_5)
        # self.checkBox_5.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_5.addWidget(self.checkBox_5)
        # self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        # self.checkBox_4.setObjectName("checkBox_4")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_4)
        # self.checkBox_4.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_5.addWidget(self.checkBox_4)
        # self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        # self.checkBox_6.setObjectName("checkBox_6")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_6)
        # self.checkBox_6.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_5.addWidget(self.checkBox_6)
        # self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        # self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # self.checkBox_7 = QtWidgets.QCheckBox(self.tab)
        # self.checkBox_7.setObjectName("checkBox_7")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_7)
        # self.checkBox_7.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_6.addWidget(self.checkBox_7)
        # self.checkBox_9 = QtWidgets.QCheckBox(self.tab)
        # self.checkBox_9.setObjectName("checkBox_9")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_9)
        # self.checkBox_9.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_6.addWidget(self.checkBox_9)
        # self.checkBox_8 = QtWidgets.QCheckBox(self.tab)
        # self.checkBox_8.setObjectName("checkBox_8")
        # # ------------------------------
        # self.vm_tab.chbox_list.append(self.checkBox_8)
        # self.checkBox_8.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_6.addWidget(self.checkBox_8)
        # self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.line_edit_changed)
        # ------------------------------
        # self.vm_tab.line_edit = self.lineEdit
        self.tabs_dict[0].line_edit = self.lineEdit
        # self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.btn_1 = QtWidgets.QPushButton(self.tab)
        self.btn_1.setObjectName('btn_1')
        self.btn_1.clicked['bool'].connect(self.refresh)
        self.btn_1.setIcon(QtGui.QIcon(
            dir_name + '/suplementary/images/refresh.gif'))
            # '/home/smacko/git/IBP/front/suplementary/images/refresh.gif'))
        self.btn_1.setIconSize(QtCore.QSize(20, 20))
        # self.verticalLayout_2.addWidget(self.btn)
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName('horizontalLayaut_81')
        self.verticalLayout_2.addLayout(self.horizontalLayout_81)
        self.horizontalLayout_81.addWidget(self.btn_1)
        self.horizontalLayout_81.addWidget(self.lineEdit)

        # ------------------------------
        # ------------------------------
        # self.tableWidget = QtWidgets.QTableWidget(self.tab)
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(0)
        # self.tableWidget.setRowCount(0)
        # self.verticalLayout.addWidget(self.tableWidget)
        self.tab_changed(tab_number=0)
        # print('aaaaaaa')
        # self.vm_tab.printed_table.header.sectionClicked.\
        #     connect(self.header_clicked)
        # self.vm_tab.printed_table.header.sectionClicked['int'].\
        #     connect(self.header_clicked)
        # ------------------------------
        # ------------------------------
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        #------------------------------
        # self.disk_tab.table_layout = self.verticalLayout_4
        self.tabs_dict[1].table_layout = self.verticalLayout_4
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        # self.checkBox_10 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_10.setObjectName("checkBox_10")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_10)
        # self.checkBox_10.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_7.addWidget(self.checkBox_10)
        # self.checkBox_11 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_11.setObjectName("checkBox_11")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_11)
        # self.checkBox_11.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_7.addWidget(self.checkBox_11)
        # self.checkBox_12 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_12.setObjectName("checkBox_12")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_12)
        # self.checkBox_12.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_7.addWidget(self.checkBox_12)
        # self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        # self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        # self.checkBox_13 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_13.setObjectName("checkBox_13")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_13)
        # self.checkBox_13.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_8.addWidget(self.checkBox_13)
        # self.checkBox_14 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_14.setObjectName("checkBox_14")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_14)
        # self.checkBox_14.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_8.addWidget(self.checkBox_14)
        # self.checkBox_15 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_15.setObjectName("checkBox_15")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_15)
        # self.checkBox_15.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_8.addWidget(self.checkBox_15)
        # self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        # self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        # self.checkBox_16 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_16.setObjectName("checkBox_16")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_16)
        # self.checkBox_16.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_9.addWidget(self.checkBox_16)
        # self.checkBox_17 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_17.setObjectName("checkBox_17")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_17)
        # self.checkBox_17.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_9.addWidget(self.checkBox_17)
        # self.checkBox_18 = QtWidgets.QCheckBox(self.tab_2)
        # self.checkBox_18.setObjectName("checkBox_18")
        # # ------------------------------
        # self.disk_tab.chbox_list.append(self.checkBox_18)
        # self.checkBox_18.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_9.addWidget(self.checkBox_18)
        # self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        # self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self.line_edit_changed)
        #-------------------------------


        self.toolbutton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolbutton_2.setText('Select Column ')
        self.toolmenu_2 = QtWidgets.QMenu(self.centralwidget)
        # for i in range(len(self.disk_tab.values_table.col_flags)-1):
        for i in range(len(self.tabs_dict[1].values_table.col_flags) - 1):
            action = self.toolmenu_2.addAction("Column " + str(i))
            action.setCheckable(True)
            # action.setChecked(self.disk_tab.values_table.col_flags[i - 1])
            action.setChecked(self.tabs_dict[1].values_table.col_flags[i + 1])
            action.changed.connect(self.checkbox_clicked)
            # self.disk_tab.chbox_list.append(action)
            self.tabs_dict[1].chbox_list.append(action)
            # self.disk_tab.chbox_list.insert(i, action)
        # self.toolbutton.che
        self.toolbutton_2.setMenu(self.toolmenu_2)
        self.toolbutton_2.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.verticalLayout_5.addWidget(self.toolbutton_2)
        # self.verticalLayout_5.addWidget(self.ComboBox)

        # ------------------------------
        # self.disk_tab.line_edit = self.lineEdit_2
        self.tabs_dict[1].line_edit = self.lineEdit_2
        # self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.btn_2 = QtWidgets.QPushButton(self.tab)
        self.btn_2.setObjectName('btn_2')
        self.btn_2.clicked['bool'].connect(self.refresh)
        self.btn_2.setIcon(QtGui.QIcon(
            dir_name + '/suplementary/images/refresh.gif'))
            # '/home/smacko/git/IBP/front/suplementary/images/refresh.gif'))
        self.btn_2.setIconSize(QtCore.QSize(20, 20))
        # self.verticalLayout_2.addWidget(self.btn)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName('horizontalLayaut_82')
        self.verticalLayout_5.addLayout(self.horizontalLayout_82)
        self.horizontalLayout_82.addWidget(self.btn_2)
        self.horizontalLayout_82.addWidget(self.lineEdit_2)
        # ------------------------------
        # ------------------------------
        # ------------------------------
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        # ------------------------------
        # self.host_tab.table_layout = self.verticalLayout_7
        self.tabs_dict[2].table_layout = self.verticalLayout_7
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.toolbutton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolbutton_3.setText('Select Column ')
        self.toolmenu_3 = QtWidgets.QMenu(self.centralwidget)
        # for i in range(len(self.host_tab.values_table.col_flags)-1):
        for i in range(len(self.tabs_dict[2].values_table.col_flags) - 1):
            action = self.toolmenu_3.addAction("Column " + str(i))
            action.setCheckable(True)
            # action.setChecked(self.host_tab.values_table.col_flags[i - 1])
            action.setChecked(self.tabs_dict[2].values_table.col_flags[i + 1])
            action.changed.connect(self.checkbox_clicked)
            # self.host_tab.chbox_list.append(action)
            self.tabs_dict[2].chbox_list.append(action)
        self.toolbutton_3.setMenu(self.toolmenu_3)
        self.toolbutton_3.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.verticalLayout_8.addWidget(self.toolbutton_3)

        # self.checkBox_19 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_19.setObjectName("checkBox_19")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_19)
        # self.checkBox_19.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_11.addWidget(self.checkBox_19)
        # self.checkBox_20 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_20.setObjectName("checkBox_20")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_20)
        # self.checkBox_20.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_11.addWidget(self.checkBox_20)
        # self.checkBox_21 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_21.setObjectName("checkBox_21")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_21)
        # self.checkBox_21.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_11.addWidget(self.checkBox_21)
        # self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        # self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        # self.checkBox_22 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_22.setObjectName("checkBox_22")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_22)
        # self.checkBox_22.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_12.addWidget(self.checkBox_22)
        # self.checkBox_23 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_23.setObjectName("checkBox_23")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_23)
        # self.checkBox_23.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_12.addWidget(self.checkBox_23)
        # self.checkBox_24 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_24.setObjectName("checkBox_24")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_24)
        # self.checkBox_24.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_12.addWidget(self.checkBox_24)
        # self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        # self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        # self.checkBox_25 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_25.setObjectName("checkBox_25")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_25)
        # self.checkBox_25.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_13.addWidget(self.checkBox_25)
        # self.checkBox_26 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_26.setObjectName("checkBox_26")
        # # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_26)
        # self.checkBox_26.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_13.addWidget(self.checkBox_26)
        # self.checkBox_27 = QtWidgets.QCheckBox(self.tab_3)
        # self.checkBox_27.setObjectName("checkBox_27")
        # ------------------------------
        # self.host_tab.chbox_list.append(self.checkBox_27)
        # self.checkBox_27.stateChanged['int'].connect(self.checkbox_clicked)
        # self.horizontalLayout_13.addWidget(self.checkBox_27)
        # self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.returnPressed.connect(self.line_edit_changed)
        # ------------------------------
        # self.host_tab.line_edit = self.lineEdit_3
        self.tabs_dict[2].line_edit = self.lineEdit_3
        # self.verticalLayout_8.addWidget(self.lineEdit_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.btn_3 = QtWidgets.QPushButton(self.tab)
        self.btn_3.setObjectName('btn_3')
        self.btn_3.clicked['bool'].connect(self.refresh)
        self.btn_3.setIcon(QtGui.QIcon(
            dir_name + '/suplementary/images/refresh.gif'))
            # '/home/smacko/git/IBP/front/suplementary/images/refresh.gif'))
        self.btn_3.setIconSize(QtCore.QSize(20, 20))
        # self.verticalLayout_2.addWidget(self.btn)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setObjectName('horizontalLayaut_83')
        self.verticalLayout_8.addLayout(self.horizontalLayout_83)
        self.horizontalLayout_83.addWidget(self.btn_3)
        self.horizontalLayout_83.addWidget(self.lineEdit_3)

        # self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        # self.tableWidget_3.setObjectName("tableWidget_3")
        # self.tableWidget_3.setColumnCount(0)
        # self.tableWidget_3.setRowCount(0)
        # self.verticalLayout_7.addWidget(self.tableWidget_3)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.checkBox_28 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_28.setObjectName("checkBox_28")
        self.checkBox_28.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_15.addWidget(self.checkBox_28)
        self.checkBox_29 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_29.setObjectName("checkBox_29")
        self.checkBox_29.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_15.addWidget(self.checkBox_29)
        self.checkBox_30 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_30.setObjectName("checkBox_30")
        self.checkBox_30.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_15.addWidget(self.checkBox_30)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.checkBox_31 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_31.setObjectName("checkBox_31")
        self.checkBox_31.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_16.addWidget(self.checkBox_31)
        self.checkBox_32 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_32.setObjectName("checkBox_32")
        self.checkBox_32.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_16.addWidget(self.checkBox_32)
        self.checkBox_33 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_33.setObjectName("checkBox_33")
        self.checkBox_33.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_16.addWidget(self.checkBox_33)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.checkBox_34 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_34.setObjectName("checkBox_34")
        self.checkBox_34.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_17.addWidget(self.checkBox_34)
        self.checkBox_35 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_35.setObjectName("checkBox_35")
        self.checkBox_35.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_17.addWidget(self.checkBox_35)
        self.checkBox_36 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_36.setObjectName("checkBox_36")
        self.checkBox_36.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_17.addWidget(self.checkBox_36)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_11.addWidget(self.lineEdit_4)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.verticalLayout_10.addWidget(self.tableWidget_4)
        self.horizontalLayout_18.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.checkBox_37 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_37.setObjectName("checkBox_37")
        self.checkBox_37.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_19.addWidget(self.checkBox_37)
        self.checkBox_38 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_38.setObjectName("checkBox_38")
        self.checkBox_38.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_19.addWidget(self.checkBox_38)
        self.checkBox_39 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_39.setObjectName("checkBox_39")
        self.checkBox_39.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_19.addWidget(self.checkBox_39)
        self.verticalLayout_15.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.checkBox_40 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_40.setObjectName("checkBox_40")
        self.checkBox_40.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_20.addWidget(self.checkBox_40)
        self.checkBox_41 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_41.setObjectName("checkBox_41")
        self.checkBox_41.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_20.addWidget(self.checkBox_41)
        self.checkBox_42 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_42.setObjectName("checkBox_42")
        self.checkBox_42.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_20.addWidget(self.checkBox_42)
        self.verticalLayout_15.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.checkBox_43 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_43.setObjectName("checkBox_43")
        self.checkBox_43.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_21.addWidget(self.checkBox_43)
        self.checkBox_44 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_44.setObjectName("checkBox_44")
        self.checkBox_44.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_21.addWidget(self.checkBox_44)
        self.checkBox_45 = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_45.setObjectName("checkBox_45")
        self.checkBox_45.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_21.addWidget(self.checkBox_45)
        self.verticalLayout_15.addLayout(self.horizontalLayout_21)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_14.addWidget(self.lineEdit_5)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.verticalLayout_13.addWidget(self.tableWidget_5)
        self.horizontalLayout_22.addLayout(self.verticalLayout_13)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.checkBox_46 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_46.setObjectName("checkBox_46")
        self.checkBox_46.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_23.addWidget(self.checkBox_46)
        self.checkBox_47 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_47.setObjectName("checkBox_47")
        self.checkBox_47.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_23.addWidget(self.checkBox_47)
        self.checkBox_48 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_48.setObjectName("checkBox_48")
        self.checkBox_48.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_23.addWidget(self.checkBox_48)
        self.verticalLayout_18.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.checkBox_49 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_49.setObjectName("checkBox_49")
        self.checkBox_49.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_24.addWidget(self.checkBox_49)
        self.checkBox_50 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_50.setObjectName("checkBox_50")
        self.checkBox_50.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_24.addWidget(self.checkBox_50)
        self.checkBox_51 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_51.setObjectName("checkBox_51")
        self.checkBox_51.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_24.addWidget(self.checkBox_51)
        self.verticalLayout_18.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.checkBox_52 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_52.setObjectName("checkBox_52")
        self.checkBox_52.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_25.addWidget(self.checkBox_52)
        self.checkBox_53 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_53.setObjectName("checkBox_53")
        self.checkBox_53.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_25.addWidget(self.checkBox_53)
        self.checkBox_54 = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_54.setObjectName("checkBox_54")
        self.checkBox_54.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_25.addWidget(self.checkBox_54)
        self.verticalLayout_18.addLayout(self.horizontalLayout_25)
        self.verticalLayout_17.addLayout(self.verticalLayout_18)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_17.addWidget(self.lineEdit_6)
        self.verticalLayout_16.addLayout(self.verticalLayout_17)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.verticalLayout_16.addWidget(self.tableWidget_6)
        self.horizontalLayout_26.addLayout(self.verticalLayout_16)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.checkBox_55 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_55.setObjectName("checkBox_55")
        self.horizontalLayout_27.addWidget(self.checkBox_55)
        self.checkBox_56 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_56.setObjectName("checkBox_56")
        self.checkBox_56.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_27.addWidget(self.checkBox_56)
        self.checkBox_57 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_57.setObjectName("checkBox_57")
        self.checkBox_57.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_27.addWidget(self.checkBox_57)
        self.verticalLayout_21.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.checkBox_58 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_58.setObjectName("checkBox_58")
        self.checkBox_58.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_28.addWidget(self.checkBox_58)
        self.checkBox_59 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_59.setObjectName("checkBox_59")
        self.checkBox_59.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_28.addWidget(self.checkBox_59)
        self.checkBox_60 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_60.setObjectName("checkBox_60")
        self.checkBox_60.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_28.addWidget(self.checkBox_60)
        self.verticalLayout_21.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.checkBox_61 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_61.setObjectName("checkBox_61")
        self.checkBox_61.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_29.addWidget(self.checkBox_61)
        self.checkBox_62 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_62.setObjectName("checkBox_62")
        self.checkBox_62.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_29.addWidget(self.checkBox_62)
        self.checkBox_63 = QtWidgets.QCheckBox(self.tab_7)
        self.checkBox_63.setObjectName("checkBox_63")
        self.checkBox_63.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_29.addWidget(self.checkBox_63)
        self.verticalLayout_21.addLayout(self.horizontalLayout_29)
        self.verticalLayout_20.addLayout(self.verticalLayout_21)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_20.addWidget(self.lineEdit_7)
        self.verticalLayout_19.addLayout(self.verticalLayout_20)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.verticalLayout_19.addWidget(self.tableWidget_7)
        self.horizontalLayout_30.addLayout(self.verticalLayout_19)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.checkBox_64 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_64.setObjectName("checkBox_64")
        self.checkBox_64.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_31.addWidget(self.checkBox_64)
        self.checkBox_65 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_65.setObjectName("checkBox_65")
        self.checkBox_65.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_31.addWidget(self.checkBox_65)
        self.checkBox_66 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_66.setObjectName("checkBox_66")
        self.checkBox_66.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_31.addWidget(self.checkBox_66)
        self.verticalLayout_24.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.checkBox_67 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_67.setObjectName("checkBox_67")
        self.checkBox_67.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_32.addWidget(self.checkBox_67)
        self.checkBox_68 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_68.setObjectName("checkBox_68")
        self.checkBox_68.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_32.addWidget(self.checkBox_68)
        self.checkBox_69 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_69.setObjectName("checkBox_69")
        self.checkBox_69.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_32.addWidget(self.checkBox_69)
        self.verticalLayout_24.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.checkBox_70 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_70.setObjectName("checkBox_70")
        self.checkBox_70.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_33.addWidget(self.checkBox_70)
        self.checkBox_71 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_71.setObjectName("checkBox_71")
        self.checkBox_71.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_33.addWidget(self.checkBox_71)
        self.checkBox_72 = QtWidgets.QCheckBox(self.tab_8)
        self.checkBox_72.setObjectName("checkBox_72")
        self.checkBox_72.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_33.addWidget(self.checkBox_72)
        self.verticalLayout_24.addLayout(self.horizontalLayout_33)
        self.verticalLayout_23.addLayout(self.verticalLayout_24)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_23.addWidget(self.lineEdit_8)
        self.verticalLayout_22.addLayout(self.verticalLayout_23)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(0)
        self.tableWidget_8.setRowCount(0)
        self.verticalLayout_22.addWidget(self.tableWidget_8)
        self.horizontalLayout_34.addLayout(self.verticalLayout_22)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.checkBox_73 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_73.setObjectName("checkBox_73")
        self.checkBox_73.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_35.addWidget(self.checkBox_73)
        self.checkBox_74 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_74.setObjectName("checkBox_74")
        self.checkBox_74.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_35.addWidget(self.checkBox_74)
        self.checkBox_75 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_75.setObjectName("checkBox_75")
        self.checkBox_75.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_35.addWidget(self.checkBox_75)
        self.verticalLayout_27.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.checkBox_76 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_76.setObjectName("checkBox_76")
        self.checkBox_76.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_36.addWidget(self.checkBox_76)
        self.checkBox_77 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_77.setObjectName("checkBox_77")
        self.checkBox_77.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_36.addWidget(self.checkBox_77)
        self.checkBox_78 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_78.setObjectName("checkBox_78")
        self.checkBox_78.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_36.addWidget(self.checkBox_78)
        self.verticalLayout_27.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.checkBox_79 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_79.setObjectName("checkBox_79")
        self.checkBox_79.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_37.addWidget(self.checkBox_79)
        self.checkBox_80 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_80.setObjectName("checkBox_80")
        self.checkBox_80.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_37.addWidget(self.checkBox_80)
        self.checkBox_81 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_81.setObjectName("checkBox_81")
        self.checkBox_81.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_37.addWidget(self.checkBox_81)
        self.verticalLayout_27.addLayout(self.horizontalLayout_37)
        self.verticalLayout_26.addLayout(self.verticalLayout_27)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_26.addWidget(self.lineEdit_9)
        self.verticalLayout_25.addLayout(self.verticalLayout_26)
        self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_9)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(0)
        self.tableWidget_9.setRowCount(0)
        self.verticalLayout_25.addWidget(self.tableWidget_9)
        self.horizontalLayout_38.addLayout(self.verticalLayout_25)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.tab_10)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.checkBox_82 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_82.setObjectName("checkBox_82")
        self.checkBox_82.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_39.addWidget(self.checkBox_82)
        self.checkBox_83 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_83.setObjectName("checkBox_83")
        self.checkBox_83.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_39.addWidget(self.checkBox_83)
        self.checkBox_84 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_84.setObjectName("checkBox_84")
        self.checkBox_84.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_39.addWidget(self.checkBox_84)
        self.verticalLayout_30.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.checkBox_85 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_85.setObjectName("checkBox_85")
        self.checkBox_85.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_40.addWidget(self.checkBox_85)
        self.checkBox_86 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_86.setObjectName("checkBox_86")
        self.checkBox_86.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_40.addWidget(self.checkBox_86)
        self.checkBox_87 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_87.setObjectName("checkBox_87")
        self.checkBox_87.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_40.addWidget(self.checkBox_87)
        self.verticalLayout_30.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.checkBox_88 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_88.setObjectName("checkBox_88")
        self.checkBox_88.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_41.addWidget(self.checkBox_88)
        self.checkBox_89 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_89.setObjectName("checkBox_89")
        self.checkBox_89.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_41.addWidget(self.checkBox_89)
        self.checkBox_90 = QtWidgets.QCheckBox(self.tab_10)
        self.checkBox_90.setObjectName("checkBox_90")
        self.checkBox_90.stateChanged['int'].connect(self.checkbox_clicked)
        self.horizontalLayout_41.addWidget(self.checkBox_90)
        self.verticalLayout_30.addLayout(self.horizontalLayout_41)
        self.verticalLayout_29.addLayout(self.verticalLayout_30)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_29.addWidget(self.lineEdit_10)
        self.verticalLayout_28.addLayout(self.verticalLayout_29)
        self.tableWidget_10 = QtWidgets.QTableWidget(self.tab_10)
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_10.setColumnCount(0)
        self.tableWidget_10.setRowCount(0)
        self.verticalLayout_28.addWidget(self.tableWidget_10)
        self.horizontalLayout_42.addLayout(self.verticalLayout_28)
        self.tabWidget.addTab(self.tab_10, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAsd_2 = QtWidgets.QMenu(self.menubar)
        self.menuAsd_2.setObjectName("menuAsd_2")
        self.menuQwe = QtWidgets.QMenu(self.menuAsd_2)
        self.menuQwe.setObjectName("menuQwe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered['bool'].connect(self.menu_item_clicked)

        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport.triggered['bool'].connect(self.export)

        # self.toolbutton_x = QtWidgets.QToolButton(self.centralwidget)
        # self.toolbutton_x.setText('Select Column ')
        # self.toolmenu_x = QtWidgets.QMenu(self.centralwidget)
        # for i in range(len(self.vm_tab.values_table.col_flags) - 1):
        #     action = self.toolmenu_x.addAction("Column " + str(i))
        #     action.setCheckable(True)
        #     action.setChecked(self.vm_tab.values_table.col_flags[i - 1])
        #     action.changed.connect(self.checkbox_clicked)
        #     self.vm_tab.chbox_list.append(action)

        self.actionAsd = QtWidgets.QAction(MainWindow)
        self.actionAsd.setObjectName("actionAsd")

        self.actionAsd.setCheckable(True)

        self.actionAsddd = QtWidgets.QAction(MainWindow)
        self.actionAsddd.setObjectName("actionAsddd")
        self.actionSdff = QtWidgets.QAction(MainWindow)
        self.actionSdff.setObjectName("actionSdff")
        self.actionSdfsf = QtWidgets.QAction(MainWindow)
        self.actionSdfsf.setObjectName("actionSdfsf")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionAsd)
        self.menuQwe.addAction(self.actionSdff)
        self.menuQwe.addAction(self.actionSdfsf)
        self.menuAsd_2.addAction(self.menuQwe.menuAction())
        self.menuAsd_2.addSeparator()
        self.menuAsd_2.addAction(self.actionAsddd)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAsd_2.menuAction())

        self.tabWidget.tabBarClicked['int'].connect(self.tab_changed)

        # if hasattr(self.vm_tab.printed_table, 'header'):
        #     self.vm_tab.printed_table.header.setObjectName("header")
        # self.vm_tab.printed_table.header.sectionClicked['int']. \
        #     connect(self.header_clicked)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Virtual Machines"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Disks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Hosts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Storage Domains"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Clusters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Data Centers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Templates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "NICs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Networks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Tab 10"))
        self.menuFile.setTitle(_translate("MainWindow", "file"))
        self.menuAsd_2.setTitle(_translate("MainWindow", "asd"))
        self.menuQwe.setTitle(_translate("MainWindow", "qwe"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionExport.setText(_translate("MainWindow", "export"))
        self.actionAsd.setText(_translate("MainWindow", "asd"))
        self.actionAsddd.setText(_translate("MainWindow", "asddd"))
        self.actionSdff.setText(_translate("MainWindow", "sdff"))
        self.actionSdfsf.setText(_translate("MainWindow", "sdfsf"))

    def tab_changed(self, tab_number):
        self.current_tab = tab_number
        # print('tab:', self.current_tab)

        # if self.tabs_dict[self.current_tab].printed_table:
        self.tabs_dict[self.current_tab].print_table()
        self.tabs_dict[self.current_tab].printed_table.\
            header.sectionClicked['int'].connect(self.header_clicked)
        self.tabs_dict[self.current_tab].printed_table.\
            cellDoubleClicked['int', 'int'].connect(self.redirect)


        # if tab_number == 0 and (hasattr(self, 'tableWidget') is False):
        #     self.vm_tab.print_table()
        #     self.tableWidget = self.vm_tab.printed_table
        #     self.vm_tab.printed_table.header.setObjectName("header")
        #     self.vm_tab.printed_table.header.sectionClicked['int']. \
        #         connect(self.header_clicked)
        #     self.vm_tab.printed_table.cellDoubleClicked['int', 'int'].\
        #         connect(self.redirect)
        # if tab_number == 1 and (hasattr(self, 'tableWidget_2') is False):
        #     # print('disk')
        #     # self.disk_tab.table.table_from_flags()
        #     self.disk_tab.print_table()
        #     self.tableWidget_2 = self.disk_tab.printed_table
        #     self.disk_tab.printed_table.header.setObjectName("header_2")
        #     self.disk_tab.printed_table.header.sectionClicked['int']. \
        #         connect(self.header_clicked)
        # if tab_number == 2 and (hasattr(self, 'tableWidget_3') is False):
        #     # print('host')
        #     self.host_tab.print_table()
        #     self.tableWidget_3 = self.host_tab.printed_table
        #     self.host_tab.printed_table.header.setObjectName("header_3")
        #     self.host_tab.printed_table.header.sectionClicked['int']. \
        #         connect(self.header_clicked)

    # def checkbox_clicked(self, number):
    @header_signal
    def checkbox_clicked(self):
        sender = self.centralwidget.sender()
        # print('sender:', sender.objectName())

        self.tabs_dict[self.current_tab].checkbox_handle(sender=sender)

        # if sender in self.vm_tab.chbox_list:
        #     self.vm_tab.checkbox_handle(sender=sender)
        # if sender in self.disk_tab.chbox_list:
        #     self.disk_tab.checkbox_handle(sender=sender)
        # if sender in self.host_tab.chbox_list:
        #     self.host_tab.checkbox_handle(sender=sender)

    @header_signal
    def line_edit_changed(self):
        sender = self.centralwidget.sender()
        # print('text:', sender.text())

        self.tabs_dict[self.current_tab].line_edit_handle(text=sender.text())

        # if sender.objectName() == 'lineEdit':
        #     self.vm_tab.line_edit_handle(sender=sender)
        # if sender.objectName() == 'lineEdit_2':
        #     self.disk_tab.line_edit_handle(sender=sender)
        # if sender.objectName() == 'lineEdit_3':
        #     self.host_tab.line_edit_handle(sender=sender)

    @header_signal
    def header_clicked(self, col):
        # sender = self.centralwidget.sender()
        # print(sender.objectName())
        # if sender.objectName() == 'header':
        #     self.vm_tab.sort_column(col=col)
        # if sender.objectName() == 'header_2':
        #     self.disk_tab.sort_column(col=col)
        # if sender.objectName() == 'header_3':
        #     self.host_tab.sort_column(col=col)
        self.tabs_dict[self.current_tab].sort_column(col=col)

    def menu_item_clicked(self, bool):
        sender = self.centralwidget.sender()
        # print('sender:', sender.objectName())
        if sender.objectName() == 'actionSave':
            # create_config_file(
            #     vm_tab=self.vm_tab, disk_tab=self.disk_tab,
            #     host_tab=self.host_tab)
            create_config_file(
                vm_tab=self.tabs_dict[0], disk_tab=self.tabs_dict[1],
                host_tab=self.tabs_dict[2])

    @header_signal
    def refresh(self, clicked):
        sender = self.centralwidget.sender()
        print('refresh:', sender.objectName())

        # # import ovirtsdk4 as sdk
        # # connection = sdk.Connection(
        # #     username='admin@internal', password='qum5net', insecure=True,
        # #     url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com' +
        # #         '/ovirt-engine/api',
        # #     # ca_file=ca_file,
        # # )
        #
        # # self.tabs_dict[self.current_tab].values_table
        #
        # if sender.objectName() == 'btn_1':
        #     # sender.setIcon(QtGui.QIcon(
        #     #     'front/suplementary/images/x.png'))
        #     # self.btn_1.setIconSize(QtCore.QSize(20, 20))
        #     # self.btn_1.setEnabled(False)
        #     # self.btn_1.setDisabled(True)
        #     self.vm_tab.values_table = vm.Vm(
        #         connection=self.connection, col_flags=self.vm_tab.values_table.col_flags)
        #     self.vm_tab.print_table()
        #     # self.btn_1.setIcon(QtGui.QIcon(
        #     #     'front/suplementary/images/refresh.gif'))
        #     # self.btn_1.setEnabled(True)
        #     # self.btn_1.setDisabled(False)
        # if sender.objectName() == 'btn_2':
        #     self.disk_tab.values_table = disk.Disk(
        #         connection=self.connection, col_flags=self.disk_tab.values_table.col_flags)
        #     self.disk_tab.print_table()
        # if sender.objectName() == 'btn_3':
        #     self.host_tab.values_table = host.Host(
        #         connection=self.connection, col_flags=self.host_tab.values_table.col_flags)
        #     self.host_tab.print_table()
        #
        #
        # # connection.close()

    def export(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(
            self.parent, 'Open file', '/home')
        if file_name[0]:
            with open(file_name[0], 'w') as file:
                writer = csv.writer(file)
                # if self.current_tab == 0:
                #     self.vm_tab.values_table.table_from_flags()
                #     writer.writerow(self.vm_tab.values_table.current_headers_list)
                #     writer.writerows(self.vm_tab.values_table.current_data_list)
                # if self.current_tab == 1:
                #     self.disk_tab.values_table.table_from_flags()
                #     writer.writerow(self.disk_tab.values_table.current_headers_list)
                #     writer.writerows(self.disk_tab.values_table.current_data_list)
                # if self.current_tab == 2:
                #     self.host_tab.values_table.table_from_flags()
                #     writer.writerow(self.host_tab.values_table.current_headers_list)
                #     writer.writerows(self.host_tab.values_table.current_data_list)

                self.tabs_dict[self.current_tab].values_table.\
                    table_from_flags()
                writer.writerow(
                    self.tabs_dict[self.current_tab].values_table.
                        current_headers_list)
                writer.writerows(
                    self.tabs_dict[self.current_tab].values_table.
                        current_data_list)

    def redirect(self, row, col):
        sender = self.centralwidget.sender()
        print("sender:", sender, "row:", row, "col:", col)

        if col in self.tabs_dict[self.current_tab].redirect_dict:
            target_tab = self.tabs_dict[self.current_tab].redirect_dict[col]

            tab_names = {0: 'vm', 1: 'disks', 2: 'hosts'}

            search_string = tab_names[self.current_tab] + ' = ' + \
                            self.tabs_dict[self.current_tab].values_table.\
                            current_data_list[row][0]
            self.tabs_dict[target_tab].line_edit.setText(search_string)
            self.tabs_dict[target_tab].line_edit_handle(text=search_string)

            self.tabWidget.setCurrentIndex(target_tab)
            self.tab_changed(tab_number=target_tab)



