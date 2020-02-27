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
print("Bilateral_Table_ID: " +  bltid_value)
tase2version = iec61850.MmsConnection_readVariable(mms_connection, mmsError, "TestDomain", "TASE2_Version")
tase2version_value = iec61850.MmsValue_toString(tase2version)
print("TASE2_Version: " +  tase2version_value)
feat = iec61850.MmsConnection_readVariable(mms_connection, mmsError, "TestDomain", "Supported_Features")
feat_value = iec61850.MmsValue_toString(feat)
print("Supported_Features: " +  feat_value)