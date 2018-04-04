from . import base
from ovirtsdk4 import types


class StatisticsListBase(base.ListBase):

    def __init__(self, connection, id):
        super(StatisticsListBase, self).__init__(connection=connection)
        self._connection = connection
        self._id = id

    # def statistic_objects_list(self, flags):
    #     pass


class StatisticBase(base.SpecificBase):

    def __init__(self, connection):
        super(StatisticBase, self).__init__(connection=connection)

    def name(self):
        return self._info.name

    def type(self):
        return self._info.type

    def unit(self):
        # return self._info.unit.name
        unit = self._info.unit
        if unit == types.StatisticUnit.BITS_PER_SECOND:
            return 'b/s'
        if unit == types.StatisticUnit.BYTES:
            return 'B'
        if unit == types.StatisticUnit.BYTES_PER_SECOND:
            return 'B/s'
        if unit == types.StatisticUnit.COUNT_PER_SECOND:
            return 'c/s'
        if unit == types.StatisticUnit.NONE:
            return ''
        if unit == types.StatisticUnit.PERCENT:
            return '%'
        if unit == types.StatisticUnit.SECONDS:
            return 's'

    def value(self):
        #todo poriesit ako to bude s viacerimi hodnotami
        if len(self._info.values) > 0:
            return self._info.values[0].datum
        else:
            return '--'
