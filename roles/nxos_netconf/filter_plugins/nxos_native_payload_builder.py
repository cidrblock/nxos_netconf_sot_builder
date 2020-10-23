
def nxos_native_payload_builder(hostvars, resources):
    nc_filter = {"System": {"@xmlns": "http://cisco.com/ns/yang/cisco-nx-os-device"}}
    for resource in resources:
        if resource in hostvars:
            nc_filter['System'][resource] = hostvars[resource]
    return nc_filter
  

class FilterModule(object):
    ''' Network interface filter '''

    def filters(self):
        return {
            'nxos_native_payload_builder': nxos_native_payload_builder
        }