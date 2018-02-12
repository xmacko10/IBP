import re
import operator
from back.high.bases.custom_comparsion import Comparison


class FilterHandle(object):

    def __init__(self, table):
        self.table = table

    # def table_from_flags(self):
    #     headers = []
    #     data = []
    #
    #     for i, flag in enumerate(self.table.col_flags):
    #         if flag == 1:
    #             headers.append(self.table.headers_list[i])
    #
    #     # for j, row in enumerate(self.table.data_list):
    #     #     data_row = []
    #     #     for i, flag in enumerate(self.table.col_flags):
    #     #         if flag == 1:
    #     #             data_row.append(row[i])
    #     #     if self.table.row_flags[j]:
    #     #         data.append(data_row)
    #
    #     for j, row in enumerate(self.table.data_list):
    #         if self.table.row_flags[j]:
    #             data_row = []
    #             for i, flag in enumerate(self.table.col_flags):
    #                 if flag == 1:
    #                     data_row.append(row[i])
    #             data.append(data_row)
    #
    #     return headers, data

    def process_filter(self, text):

        class Filter(object):

            def __init__(self, column, operand, value):
                self.column = column
                self.operand = operand
                self.value = value

        ops = {
            '>': operator.gt, '<': operator.lt, '=': operator.eq}

        # filter_regex = r'\s*(\S+)\s*(>|<|=)\s*(\S+)\s*'
        filter_regex = r'\s*(w+|\w+\s{0,1}\w+)\s*(>|<|=)\s*(\S+)\s*'
        match = re.match(filter_regex, text, re.I)

        # print('1:', match.group(1))
        # print('2:', match.group(2))
        # print('3:', match.group(3))

        if match:
            attribute = match.group(1)
            operand = ops[match.group(2)]
            value = match.group(3)

            attribute_column = None
            for i, header in enumerate(self.table.headers_list):
                # print(header)
                if attribute == header:
                    attribute_column = i
                    break

            if attribute_column is not None:
                filter = Filter(
                    column=attribute_column, operand=operand, value=value)
                return filter
            else:
                return None
        else:
            return None

    def apply_filter(self, filter):
        # print(filter.operand)
        for i, row in enumerate(self.table.data_list):
            # if filter.operand(row[filter.column], filter.value) is False:
            if filter.operand(Comparison(row[filter.column]),
                              Comparison(filter.value)) is False:
                self.table.row_flags[i] = 0
