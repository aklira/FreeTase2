#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

from tase2.common.iccpcommon import VCC, BilateralTable, Association
import yaml
import iec61850

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
        mmsError = 0
        result = iec61850.MmsConnection_connect(self.MmsConnection, mmsError, self.RemoteServer, 102)
        return result

    def check_connection(self, id_iccp, loop_error):
        pass

    def command_variable(self, variable, value):
        pass

class IccpConf:
# TASE.2 client configuration

    def __init__(self,
                 remote_server,
                 ap_title,
                 blt_id,
                 blt_version,
                 tase2_version,
                 ds_name,
                 assoc_id,
                 ae_title,
                 supported_features):
        self.remote_server = remote_server
        self.ap_title = ap_title
        self.blt_id = blt_id
        self.blt_version = blt_version
        self.tase2_version = tase2_version
        self.ds_name = ds_name
        self.assoc_id = assoc_id
        self.ae_title = ae_title
        self.supported_features = supported_features
    
    @classmethod
    def create_from_file(cls, conf_file):
        # read conf file
        # create instance from input values
        # return cls(args)

        with open(conf_file, 'r') as config:
            tase2_conf = yaml.load(config)

        remote_server = tase2_conf['remote_server']
        ap_title = tase2_conf['ap_title']
        blt_id = tase2_conf['blt_id']
        blt_version = tase2_conf['blt_version']
        tase2_version = tase2_conf['tase2_version']
        ds_name = tase2_conf['ds_name']
        assoc_id = tase2_conf['assoc_id']
        ae_title = tase2_conf['ae_title']
        supported_features = tase2_conf['supported_features']

        return cls(remote_server,
                   ap_title,
                   blt_id,
                   blt_version,
                   tase2_version,
                   ds_name,
                   assoc_id,
                   ae_title,
                   supported_features)


conn = None
vcc = None
conf = None

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

def start_iccp(conf_file):
    global conn
    global vcc
    global conf
# create tase2 conf from file 
    conf = IccpConf.create_from_file(conf_file)

# create IccpConnection
    mms_connection = iec61850.MmsConnection_create()
    remote_server = conf.remote_server
    conn = IccpConnection(mms_connection, remote_server)

# create VCC
 # create bilateral table
    ap_title = conf.ap_title
    blt_id = conf.blt_id
    blt_version = conf.blt_version
    tase2_version = conf.tase2_version
    bilateraltable = BilateralTable(ap_title, blt_id, blt_version, tase2_version)

    ds_name = conf.ds_name
    vcc = VCC(bilateraltable, ds_name)

# create Association
    assoc_id = conf.assoc_id
    ae_title = conf.ae_title
    supported_features = conf.supported_features
    assoc = Association(assoc_id, ae_title, 0, supported_features)
    vcc.add_assoc_to_vcc(assoc)

# delete existing datasets
# create transfersets
# create datasets
# add datasets to transfersets
    pass

def connect_iccp():
    success = False
    try:
        conn.connect_to_server()
        success = True
    except:
        pass
    return success


def check_connections_threads(parameter):
    pass