```
python3 -m venv venv
source venv/bin/activate
pip install ansible-base
pip install ncclient
pip install xmltodict
ansible-galaxy collection install cisco.nxos -p ./collections
ansible-galaxy collection install ansible.utils -p ./collections
ansible-playbook -i inventory build_sot.yaml
ansible-playbook -i inventory deploy_sot.yaml
```

```yaml

PLAY [nxos101] ****************************************************************************************************

TASK [include_role : nxos_netconf] ********************************************************************************

TASK [nxos_netconf : Set the inventory directory] *****************************************************************
ok: [nxos101]

TASK [nxos_netconf : Ensure the inventory directory exists] *******************************************************
changed: [nxos101]

TASK [nxos_netconf : Get the config using the filter] *************************************************************
ok: [nxos101]

TASK [nxos_netconf : Copy each resource to a file] ****************************************************************
changed: [nxos101] => (item=adjacency-items)
changed: [nxos101] => (item=arp-items)
changed: [nxos101] => (item=bd-items)
changed: [nxos101] => (item=boot-items)
changed: [nxos101] => (item=cdp-items)
changed: [nxos101] => (item=cfs-items)
changed: [nxos101] => (item=clock-items)
changed: [nxos101] => (item=conng-items)
changed: [nxos101] => (item=dhcp-items)
changed: [nxos101] => (item=dns-items)
changed: [nxos101] => (item=ethpm-items)
changed: [nxos101] => (item=fm-items)
changed: [nxos101] => (item=icmpv4-items)
changed: [nxos101] => (item=icmpv6-items)
changed: [nxos101] => (item=igmpsnoop-items)
changed: [nxos101] => (item=inst-items)
changed: [nxos101] => (item=install-items)
changed: [nxos101] => (item=intf-items)
changed: [nxos101] => (item=ipqos-items)
changed: [nxos101] => (item=ipv4-items)
changed: [nxos101] => (item=ipv6-items)
changed: [nxos101] => (item=l2fm-items)
changed: [nxos101] => (item=lacp-items)
changed: [nxos101] => (item=lldp-items)
changed: [nxos101] => (item=lsnode-items)
changed: [nxos101] => (item=mac-items)
changed: [nxos101] => (item=macsec-items)
changed: [nxos101] => (item=mgmt-items)
changed: [nxos101] => (item=name)
changed: [nxos101] => (item=nd-items)
changed: [nxos101] => (item=npv-items)
changed: [nxos101] => (item=nxapi-items)
changed: [nxos101] => (item=ops-items)
changed: [nxos101] => (item=ospf-items)
changed: [nxos101] => (item=pc-items)
changed: [nxos101] => (item=pltfm-items)
changed: [nxos101] => (item=poe-items)
changed: [nxos101] => (item=snmp-items)
changed: [nxos101] => (item=stp-items)
changed: [nxos101] => (item=systemTable-items)
changed: [nxos101] => (item=time-items)
changed: [nxos101] => (item=udld-items)
changed: [nxos101] => (item=userext-items)
changed: [nxos101] => (item=vrfTable-items)
changed: [nxos101] => (item=vrrp-items)

PLAY RECAP ********************************************************************************************************
nxos101                    : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

```yaml
(venv) ➜  netconf_docs ansible-playbook -i inventory deploy_sot.yaml                                                              

PLAY [nxos101] ****************************************************************************************************

TASK [include_role : nxos_netconf] ********************************************************************************

TASK [nxos_netconf : Get the config using the filter] *************************************************************
ok: [nxos101]

TASK [nxos_netconf : Build the intended config payload] ***********************************************************
ok: [nxos101]

TASK [nxos_netconf : Show the intended changes] *******************************************************************
ok: [nxos101]

TASK [nxos_netconf : Deploy the configuration] ********************************************************************
skipping: [nxos101]

TASK [nxos_netconf : Get the config using the filter] *************************************************************
skipping: [nxos101]

TASK [nxos_netconf : Show the deployed changes] *******************************************************************
skipping: [nxos101]

TASK [nxos_netconf : debug] ***************************************************************************************
ok: [nxos101] => {
    "msg": "No deployment necessary"
}

PLAY RECAP ********************************************************************************************************
nxos101                    : ok=4    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   

(venv) ➜  netconf_docs ansible-playbook -i inventory deploy_sot.yaml

PLAY [nxos101] ****************************************************************************************************

TASK [include_role : nxos_netconf] ********************************************************************************

TASK [nxos_netconf : Get the config using the filter] *************************************************************
ok: [nxos101]

TASK [nxos_netconf : Build the intended config payload] ***********************************************************
ok: [nxos101]

TASK [nxos_netconf : Show the intended changes] *******************************************************************
--- before
+++ after
@@ -9440,7 +9440,7 @@
     "lldp-items['inst-items'].portIdSubType": "long",
     "lldp-items['inst-items'].txFreq": "30",
     "lldp-items['inst-items']['if-items']['If-list'][0].adminRxSt": "enabled",
-    "lldp-items['inst-items']['if-items']['If-list'][0].adminSt": "enabled",
+    "lldp-items['inst-items']['if-items']['If-list'][0].adminSt": "disabled",
     "lldp-items['inst-items']['if-items']['If-list'][0].adminTxSt": "enabled",
     "lldp-items['inst-items']['if-items']['If-list'][0].id": "eth1/107",
     "lldp-items['inst-items']['if-items']['If-list'][0].tlvSetVlan": "0",

changed: [nxos101]

TASK [nxos_netconf : Deploy the configuration] ********************************************************************
changed: [nxos101]

TASK [nxos_netconf : Get the config using the filter] *************************************************************
ok: [nxos101]

TASK [nxos_netconf : Show the deployed changes] *******************************************************************
--- before
+++ after
@@ -9440,7 +9440,7 @@
     "lldp-items['inst-items'].portIdSubType": "long",
     "lldp-items['inst-items'].txFreq": "30",
     "lldp-items['inst-items']['if-items']['If-list'][0].adminRxSt": "enabled",
-    "lldp-items['inst-items']['if-items']['If-list'][0].adminSt": "enabled",
+    "lldp-items['inst-items']['if-items']['If-list'][0].adminSt": "disabled",
     "lldp-items['inst-items']['if-items']['If-list'][0].adminTxSt": "enabled",
     "lldp-items['inst-items']['if-items']['If-list'][0].id": "eth1/107",
     "lldp-items['inst-items']['if-items']['If-list'][0].tlvSetVlan": "0",

changed: [nxos101]

TASK [nxos_netconf : debug] ***************************************************************************************
skipping: [nxos101]

PLAY RECAP ********************************************************************************************************
nxos101                    : ok=6    changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

(venv) ➜  netconf_docs 
```