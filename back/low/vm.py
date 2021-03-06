

import back.low.cluster as Cluster
from back.low.bases import base
from back.suplementary.cell_item import CellItem
from back.suplementary.conversion import to_MB


class VmList(base.ListBase):

    def __init__(self, connection):
        super(VmList, self).__init__(connection=connection)
        self._service = self._service.vms_service()
        self._list = self._service.list()


class Vm(base.SpecificBase):

    def __init__(self, connection, id):
        super(Vm, self).__init__(connection=connection, id=id)
        self._service = self._service.vms_service().vm_service(id=id)
        self._info = self._service.get()

    def _cl_version(self):
        name = 'Cluster version'
        cl = self._connection.follow_link(self._info._cluster)
        cl_version = Cluster.Cluster(connection=self._connection, id=cl.id).\
            version().value
        return CellItem(name=name, value=cl_version)

    def disks_obj(self):
        disk_attachments = self._connection.\
            follow_link(self._info.disk_attachments)
        return [self._connection.follow_link(attachment.disk)
                for attachment in disk_attachments]

    def _disks(self):
        name = 'Disks'
        return CellItem(
            name=name, value=[disk.name for disk in self.disks_obj()]
        )

    def bootable_disk(self):
        for disk in self.disks_obj():
            if disk.bootable:
                return disk
        return None

    def host_obj(self):
        if self._info._host:
            return self._connection.follow_link(self._info._host)
        else:
            return None

    def _host(self):
        name = 'Host'
        if self.host_obj():
            return CellItem(name=name, value=self.host_obj().name)
        else:
            return CellItem(name=name)

    def _memory(self):
        name = 'Memory'
        return CellItem(name=name, value=to_MB(self._info._memory))

    def _memory_max(self):
        name = 'Max memory'
        return CellItem(name=name, value=to_MB(self._info.memory_policy.max))

    def nics_obj(self):
        nics = self._connection.follow_link(self._info._nics)
        return [nic for nic in nics]

    def _nics(self):
        name = 'NICs'
        return CellItem(name=name, value=[nic.name for nic in self.nics_obj()])

    def _os(self):
        name = 'OS'
        return CellItem(name=name, value=self._info._os.type)

    def template_obj(self):
        return self._connection.follow_link(self._info._template)

    def _template(self):
        name = 'Template'
        template = self.template_obj().name
        if template == 'Blank':
            return CellItem(name=name)
        else:
            return CellItem(name=name, value=template)

    def _st_memory_installed(self):
        name = 'Installed memory'
        return CellItem(
            name=name,
            value=self._connection.follow_link(self._info.statistics)
        )

    def _status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info._status.name)

    def storage_domain(self):
        name = 'Storage domain'
        from back.low.storage_domain import Storage, StorageList
        storage_domains = []
        storages_list = StorageList(connection=self._connection).list()
        for storage in storages_list:
            storage_vms = Storage(
                connection=self._connection, id=storage.id).vms_obj()
            for vm in storage_vms:
                if vm and vm.id == self._info.id:
                    storage_domains.append(storage.name)
        return CellItem(name=name, value=storage_domains)

    def cluster_obj(self):
        return self._connection.follow_link(self._info.cluster)

    def _cluster(self):
        name = 'Cluster'
        return CellItem(
            name=name,
            value=self.cluster_obj().name
        )

    def _consoles(self):
        name = 'Console'
        console_service = self._service.graphics_consoles_service()
        return CellItem(
            name=name,
            value=[
                console.protocol.name for console in console_service.list()
            ][0]
        )

    def vnics_obj(self):
        return [
            self._connection.follow_link(nic.vnic_profile)
            for nic in self.nics_obj()
        ]

    def networks_obj(self):
        return [
            self._connection.follow_link(vnic.network)
            for vnic in self.vnics_obj()
        ]

    def _networks(self):
        name = 'Networks'
        return CellItem(
            name=name, value=[net.name for net in self.networks_obj()]
        )

    def methods_list(self):
        return [
            self.name, self.id, self._status, self._consoles, self._cluster,
            self._cl_version, self._host, self._memory, self._memory_max,
            self._os, self._template, self._disks, self._nics, self._networks,
            self.storage_domain
        ]
