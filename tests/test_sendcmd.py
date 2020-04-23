#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

import iec61850
import sys

domain = "TestDomain"
itemId = ["tc1"]

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

    if (conn):
        print("Connection established!\n")
        for item in itemId:
            if (sys.argv[1] == "ON"):
                #value = iec61850.MmsValue_newBoolean(True)
                value = iec61850.MmsValue_newVisibleString("ON")
            elif (sys.argv[1] == "OFF"):
                #value = iec61850.MmsValue_newBoolean(False)
                value = iec61850.MmsValue_newVisibleString("OFF")
            else:
                print("Unknown command!\n")
            
            result = iec61850.MmsConnection_writeVariable(mms_connection, mmsError, domain, item, value)
            print(result)
    else:
        print("Connection failed!\n")

if __name__ == '__main__':
    main()