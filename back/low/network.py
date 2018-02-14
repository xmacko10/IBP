from back.low.bases import base, statisctics_base
from ovirtsdk4 import types


class NetworkList(base.ListBase):

    def __init__(self, connection):
        super(NetworkList, self).__init__(connection=connection)
        self._service = self._service.networks_service()
        self._list = self._service.list()


class Network(base.SpecificBase):

    def __init__(self, connection, net_id):
        super(Network, self).__init__(connection=connection)
        self._service = self._service.networks_service().\
            network_service(id=net_id)
        self._info = self._service.get()


