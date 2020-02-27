#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

import iec61850

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
remote_server = "10.132.0.110"
remote_port = 102
mmsError = iec61850.toMmsErrorP()
result = iec61850.MmsConnection_connect(mms_connection, mmsError, remote_server, remote_port)
biltid = iec61850.MmsConnection_readVariable(mms_connection, mmsError, "TestDomain", "Bilateral_Table_ID")
bltid_value = iec61850.MmsValue_toString(biltid)
print("Bilateral_Table_ID: " + str(bltid_value))
tase2version = iec61850.MmsConnection_readVariable(mms_connection, mmsError, None, "TASE2_Version")
tase2version_val_major = iec61850.MmsValue_toUint32(iec61850.MmsValue_getElement(tase2version, 0))
tase2version_val_minor = iec61850.MmsValue_toUint32(iec61850.MmsValue_getElement(tase2version, 1))
print("TASE2_Version: " + str(tase2version_val_major) + "-" + str(tase2version_val_minor))
feat = iec61850.MmsConnection_readVariable(mms_connection, mmsError, None, "Supported_Features")
feat_bitstring_size = iec61850.MmsValue_getBitStringSize(feat)
lst1 = [1,2,3,4,5,6,7,8,9,10,11,12]
lst2 = []
for i in range(feat_bitstring_size):
    lst2.append(iec61850.MmsValue_getBitStringBit(feat,i))
Supported_Features = [a*b for a,b in zip(lst1,lst2)]   
print("Supported_Features:")
print(Supported_Features)