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
    result = iec61850.MmsConnection_connect(mms_connection, mmsError, remote_server, remote_port)

    iec61850.MmsConnection_deleteNamedVariableList(mms_connection,mmsError,domain,ds_name)
    
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
        iec61850.write_dataset(mms_connection, 
                               domain, 
                               ds_name, 
                               ts_name, 
                               buffer_time, 
                               integrity_time, 
                               REPORT_INTERVAL_TIMEOUT|REPORT_OBJECT_CHANGES|REPORT_BUFFERED)
                               
        print("Writing dataset successful")
    except:
        print("Error writing dataset")
        pass
    

if __name__ == '__main__':
    main()