
def nxos_native_filter_builder(resources):
    nc_filter = {"System": {"@xmlns": "http://cisco.com/ns/yang/cisco-nx-os-device"}}
    for resource in resources:
        nc_filter['System'][resource] = None
    return nc_filter
  
class FilterModule(object):
    ''' Network interface filter '''

    def filters(self):
        return {
            'nxos_native_filter_builder': nxos_native_filter_builder
        }