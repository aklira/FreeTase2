#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

# import "mms_types.h"
# import "mms_value_internal.h"
# import "mms_client_connection.h"
from tase2.common.iccpcommon import VCC, BilateralTable, Association
import yaml

class IccpConnection:
# TASE.2 connection management

    def __init__(self, 
                 MmsConnection, 
                 RemoteServer,
                 enabled = None,
                 error = None):
        self.MmsConnection = MmsConnection
        self.RemoteServer = RemoteServer
        self.enabled = enabled
        self.error = error

    def connect_to_server(self):
        pass

    def check_connection(self, id_iccp, loop_error):
        pass

    def command_variable(self, variable, value):
        pass

conn = None
vcc = None

def read_dataset(ds_name, offset):
    pass

def create_dataset(ds_name, offset):
    pass

def write_dataset(id_iccp, 
                  ds_name, 
                  ts_name, 
                  buffer_time, 
                  integrity_time, 
                  all_changes_reported):
    pass

def get_next_transferset(self, id_iccp):
    pass

def read_conf(file):
    pass

def start_iccp():
# create IccpConnection
    mms_connection = None # use method MmsConnection_create() from mms_client_connection.h
    remote_server = None # use read_conf(file)
    conn = IccpConnection(mms_connection, remote_server)
# create VCC
 # create bilateral table
    ap_title = None # use read_conf(file)
    blt_id = None # use read_conf(file)
    version = None # use read_conf(file)
    tase2_version = None # use read_conf(file)
    bilateraltable = BilateralTable(ap_title, blt_id, version, tase2_version)

    ds_name = None # use read_conf(file)
    vcc = VCC(bilateraltable, ds_name)
# create Association
    assoc_id = None # use read_conf(file)
    ae_title = None # use read_conf(file)
    supported_features = None # use read_conf(file)
    assoc = Association(assoc_id, ae_title, 0, supported_features)
    vcc.add_assoc_to_vcc(assoc)
# delete existing datasets
# create transfersets
# create datasets
# add datasets to transfersets
    pass

def check_connections_threads(parameter):
    pass