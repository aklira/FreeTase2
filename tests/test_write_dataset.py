#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

import iec61850

domain = "TestDomain"
ds_name = "TSetAnalog"
buffer_time = 0
integrity_time = 60

REPORT_BUFFERED = 0x01
REPORT_INTERVAL_TIMEOUT = 0x02
REPORT_OBJECT_CHANGES = 0x04

remote_server = "10.132.0.110"
remote_port = 102

def write_dataset(mmsConnection,
                  mmsError,  
                  domain, 
                  ds_name, 
                  ts_name, 
                  buffer_time, 
                  integrity_time, 
                  all_changes_reported):
    
    success = False

    typeSpec = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(typeSpec, 1) # MMS_STRUCTURE
    iec61850.setMmsVSTypeSpecElementCount(typeSpec, 13)
    iec61850.MmsVSTypeSpecElements_create(typeSpec, 13)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 1) # MMS_STRUCTURE
    iec61850.setMmsVSTypeSpecElementCount(element, 3)
    iec61850.MmsVSTypeSpecElements_create(element, 3)

    inside_element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(inside_element, 5) # MMS_UNSIGNED
    iec61850.setMmsVSTypeSpecUInt(inside_element, 8)
    iec61850.setMmsVSTypeSpecElementCount(inside_element, 3)
    iec61850.setMmsVSTypeSpecElement(element, inside_element, 0)

    inside_element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(inside_element, 8) # MMS_VISIBLE_STRING
    iec61850.setMmsVSTypeSpecVString(inside_element, -129)
    iec61850.setMmsVSTypeSpecElement(element, inside_element, 1)

    inside_element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(inside_element, 8) # MMS_VISIBLE_STRING
    iec61850.setMmsVSTypeSpecVString(inside_element, -129)
    iec61850.setMmsVSTypeSpecElement(element, inside_element, 2)

    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 0)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 4) # MMS_INTEGER
    iec61850.setMmsVSTypeInteger(element, 8)
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 1)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 4) # MMS_INTEGER
    iec61850.setMmsVSTypeInteger(element, 8)
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 2)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 4) # MMS_INTEGER
    iec61850.setMmsVSTypeInteger(element, 8)
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 3)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 4) # MMS_INTEGER
    iec61850.setMmsVSTypeInteger(element, 8)
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 4)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 4) # MMS_INTEGER
    iec61850.setMmsVSTypeInteger(element, 8)
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 5)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 3) # MMS_BIT_STRING
    iec61850.setMmsVSTypebitString(element, 5)
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 6)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 2) # MMS_BOOLEAN
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 7)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 2) # MMS_BOOLEAN
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 8)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 2) # MMS_BOOLEAN
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 9)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 2) # MMS_BOOLEAN
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 10)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 2) # MMS_BOOLEAN
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 11)

    element = iec61850.MmsVariableSpecification_create(1)
    iec61850.setMmsVSType(element, 4) # MMS_INTEGER
    iec61850.setMmsVSTypeInteger(element, 8)
    iec61850.setMmsVSTypeSpecElement(typeSpec, element, 12)

    dataset = iec61850.MmsValue_newStructure(typeSpec)

    elem = iec61850.MmsValue_getElement(dataset, 0)

    ielem = iec61850.MmsValue_getElement(elem, 0)
    iec61850.MmsValue_setUint8(ielem, 1)

    ielem = iec61850.MmsValue_getElement(elem, 1)
    iec61850.MmsValue_setVisibleString(ielem, domain)

    ielem = iec61850.MmsValue_getElement(elem, 2)
    iec61850.MmsValue_setVisibleString(ielem, ds_name)

    elem = iec61850.MmsValue_getElement(dataset, 1)
    iec61850.MmsValue_setInt32(elem, 0)

    elem = iec61850.MmsValue_getElement(dataset, 2)
    iec61850.MmsValue_setInt32(elem, 0)

    elem = iec61850.MmsValue_getElement(dataset, 3)
    iec61850.MmsValue_setInt32(elem, 0)

    elem = iec61850.MmsValue_getElement(dataset, 4)
    iec61850.MmsValue_setInt32(elem, buffer_time) # Buffer interval

    elem = iec61850.MmsValue_getElement(dataset, 5)
    iec61850.MmsValue_setInt32(elem, integrity_time) # Integrity check time

    elem = iec61850.MmsValue_getElement(dataset, 6)

    if(all_changes_reported&REPORT_INTERVAL_TIMEOUT):
        iec61850.MmsValue_setBitStringBit(elem, 1, True)
	
    if(all_changes_reported&REPORT_OBJECT_CHANGES): 
        iec61850.MmsValue_setBitStringBit(elem, 2, True)
    
    elem = iec61850.MmsValue_getElement(dataset, 7)
    iec61850.MmsValue_setBoolean(elem, False)

    elem = iec61850.MmsValue_getElement(dataset, 8)
    iec61850.MmsValue_setBoolean(elem, False)

    elem = iec61850.MmsValue_getElement(dataset, 9)
    iec61850.MmsValue_setBoolean(elem, False) # Report By Exception

    elem = iec61850.MmsValue_getElement(dataset, 10)
    if(all_changes_reported&REPORT_BUFFERED):
        iec61850.MmsValue_setBoolean(elem, False)
    else:
        iec61850.MmsValue_setBoolean(elem, True)

    elem = iec61850.MmsValue_getElement(dataset, 11)
    iec61850.MmsValue_setBoolean(elem, True)

    elem = iec61850.MmsValue_getElement(dataset, 12)
    iec61850.MmsValue_setInt32(elem, 0)

    #DEBUG
    import pdb; pdb.set_trace()
    
    print("Before MmsConnection_writeVariable")

    result = iec61850.MmsConnection_writeVariable(mmsConnection, mmsError, domain, ts_name, dataset)
    print(result)

    success = True

    return success

def main():
    result = False
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
    result = iec61850.MmsConnection_connect(mms_connection, mmsError, remote_server, remote_port)

    iec61850.MmsConnection_deleteNamedVariableList(mms_connection, 
                                                   mmsError, 
                                                   domain, 
                                                   ds_name)
    
    handler = iec61850.informationReportHandler_create()

    iec61850.MmsConnection_setInformationReportHandler(mms_connection, handler, mms_connection)

    vars = iec61850.LinkedList_create()
    #name = iec61850.MmsVariableAccessSpecification_create(domain, "Transfer_Set_Name")
    #tst = iec61850.MmsVariableAccessSpecification_create(domain, "Transfer_Set_Time_Stamp")
    #dsc = iec61850.MmsVariableAccessSpecification_create(domain, "DSConditions_Detected")
    #iec61850.LinkedList_add(vars, name)
    #iec61850.LinkedList_add(vars, tst)
    #iec61850.LinkedList_add(vars, dsc)

    var = iec61850.MmsVariableAccessSpecification_create(domain, "tm1")
    iec61850.LinkedList_add(vars, var)

    iec61850.MmsConnection_defineNamedVariableList(mms_connection, 
                                                   mmsError, 
                                                   domain, 
                                                   ds_name, 
                                                   vars)

    next_ts = iec61850.MmsConnection_readVariable(mms_connection, 
                                                  mmsError, 
                                                  domain, 
                                                  "Next_DSTransfer_Set")
    ts_name = iec61850.MmsValue_toString(iec61850.MmsValue_getElement(next_ts, 2))

    try:
        result = write_dataset(mms_connection, 
                               mmsError, 
                               domain, 
                               ds_name, 
                               ts_name,
                               buffer_time,
                               integrity_time, 
                               REPORT_BUFFERED|REPORT_INTERVAL_TIMEOUT|REPORT_OBJECT_CHANGES)
        print(result)
    except:
        print("Error writing dataset")
        pass
    

if __name__ == '__main__':
    main()