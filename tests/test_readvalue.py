#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

import iec61850

domain = "TestDomain"
ds_name = "ds_real"
itemId = "tm1"

remote_server = "10.132.0.110"
remote_port = 102

def main():
    local_tselector = iec61850.TSelector()
    local_tselector.size = 2
    local_tselector.value = [0, 1]
    local_sselector = iec61850.SSelector()
    local_sselector.size = 2
    local_sselector.value = [0, 1]
    local_pselector = iec61850.PSelector()
    local_pselector.size = 4
    local_pselector.value = [0, 0, 0, 1] 
    remote_tselector = iec61850.TSelector()
    remote_tselector.size = 2
    remote_tselector.value = [0, 1] 
    remote_sselector = iec61850.SSelector()
    remote_sselector.size = 2
    remote_sselector.value = [0, 1] 
    remote_pselector = iec61850.PSelector()
    remote_pselector.size = 4
    remote_pselector.value = [0, 0, 0, 1]  
    mms_connection = iec61850.MmsConnection_createWisop("1.2.32.2",1,local_tselector,local_sselector,local_pselector,"1.2.3", 21,remote_tselector,remote_sselector,remote_pselector)
    mmsError = iec61850.toMmsErrorP()
    conn = iec61850.MmsConnection_connect(mms_connection, mmsError, remote_server, remote_port)

    vars = iec61850.LinkedList_create()
    name = iec61850.MmsVariableAccessSpecification_create(domain, "Transfer_Set_Name")
    tst = iec61850.MmsVariableAccessSpecification_create(domain, "Transfer_Set_Time_Stamp")
    dsc = iec61850.MmsVariableAccessSpecification_create(domain, "DSConditions_Detected")
    iec61850.LinkedList_add(vars, name)
    iec61850.LinkedList_add(vars, tst)
    iec61850.LinkedList_add(vars, dsc)

    iec61850.MmsConnection_defineNamedVariableList(mms_connection, 
                                                   mmsError, 
                                                   domain, 
                                                   ds_name, 
                                                   vars)

    value = iec61850.MmsConnection_readVariable(mms_connection, mmsError, domain, itemId)
    val_part1 = iec61850.MmsValue_toDouble(iec61850.MmsValue_getElement(value, 0))
    val_part2 = iec61850.MmsValue_getElement(value, 1)
    print(val_part1)
    print(val_part2)

if __name__ == '__main__':
    main()