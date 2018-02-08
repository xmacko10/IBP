from front.table import Table
from back.low.filter_handle import FilterHandle
from operator import methodcaller
from back.high.bases.custom_comparsion import Comparison

from time import sleep
from PyQt5.QtWidgets import QHeaderView
# from front.main_window import Ui_MainWindow as mw



class Tabs(object):

    def __init__(self, table, parent):
        self.parent = parent
        self.chbox_list = []
        self.line_edit = None
        self.table = table
        self.printed_table = None
        self.table_layout = None

        self.col = None
        self.column_order = False

    def print_table(self, data_list=None, headers_list=None):
        if data_list is None:
            data_list = self.table.data_list
        if headers_list is None:
            headers_list = self.table.headers_list

        if self.table_layout.count() > 1:
            self.table_layout.removeWidget(self.printed_table)
        self.printed_table = Table(
                parent=self.parent, data_list=data_list,
                headers_list=headers_list)
        self.table_layout.addWidget(self.printed_table)

    def checkbox_handle(self, sender):
        for i, ch_box in enumerate(self.chbox_list):
            if sender == ch_box and i < len(self.chbox_list):
                if self.table.col_flags[i+1] == 1:
                    self.table.col_flags[i+1] = 0
                else:
                    self.table.col_flags[i+1] = 1

        headers, data = FilterHandle(table=self.table).table_from_flags()

        self.print_table(headers_list=headers, data_list=data)

    def line_edit_handle(self, sender):
        text = sender.text()
        headers = data = None
        if text == '':
            self.table.row_flags = [1 for _ in
                                    range(len(self.table.row_flags))]
            self.print_table()
            return

        try:
            for single_filter in text.split(','):

                filter_handler = FilterHandle(table=self.table)
                filter = filter_handler.process_filter(text=single_filter)

                if filter and self.table.validate_filter(filter=filter):
                    filter_handler.apply_filter(filter=filter)
                    headers, data = filter_handler.table_from_flags()
                else:
                    raise Exception
            self.print_table(headers_list=headers, data_list=data)
            self.table.row_flags = [1 for _ in
                                    range(len(self.table.row_flags))]
        except Exception:
            print('wrong filter')

    def test(self, value):
        # print(Comparison(value[self.col]).operand)
        return Comparison(value[self.col])

    def sort_column(self, col):
        print('col:', col)

        self.col = col

        # self.table.data_list = sorted(self.table.data_list,
        #                               key=self.test, reverse=True)

        # def test(value):
        #     # print('value:', value)
        #     # print('col:', col)
        #     print(Comparison(value[col]))
        #     return Comparison(value[col])

        if self.column_order is False:
            # print('if')
            self.table.data_list = sorted(self.table.data_list,
                                          key=self.test, reverse=True)
            self.column_order = True

        else:
            # print('else')
            self.table.data_list = sorted(self.table.data_list,
                                          key=self.test, reverse=False)
            # self.table.data_list.reverse()

            self.column_order = False

        # for row in self.table.data_list:
        #     print(row)

        self.print_table(headers_list=self.table.headers_list,
                           data_list=self.table.data_list)

        # self.printed_table.header.sectionClicked['int']. \
        #     connect(Ui_MainWindow.tab_changed)



class VmTab(Tabs):

    def __init__(self, table, parent):
        super(VmTab, self).__init__(table=table, parent=parent)

class DiskTab(Tabs):

    def __init__(self, table, parent):
        super(DiskTab, self).__init__(table=table, parent=parent)

class HostTab(Tabs):

    def __init__(self, table, parent):
        super(HostTab, self).__init__(table=table, parent=parent)




