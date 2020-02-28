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
                 RemotePort,
                 enabled = None,
                 error = None):
        self.MmsConnection = MmsConnection
        self.RemoteServer = RemoteServer
        self.RemotePort = RemotePort
        self.enabled = enabled
        self.error = error

    def connect_to_server(self):
        mmsError = iec61850.toMmsErrorP()
        result = iec61850.MmsConnection_connect(self.MmsConnection, mmsError, self.RemoteServer, self.RemotePort)
        return result

    def check_connection(self, id_iccp, loop_error):
        pass

    def command_variable(self, variable, value):
        pass

class IccpConf:
# TASE.2 client configuration

    def __init__(self,
                 remote_server,
                 remote_port,
                 keepalive,
                 tls,
                 use_defaults,
                 remote_ap_title,
                 remote_ae_qual,
                 remote_tselector,
                 remote_sselector,
                 remote_pselector,
                 local_ap_title,
                 local_ae_qual,
                 local_tselector,
                 local_sselector,
                 local_pselector,
                 blt_id,
                 blt_version,
                 tase2_version,
                 ds_name,
                 assoc_id,
                 ae_title,
                 supported_features):
        # transport parameters
        self.remote_server = remote_server
        self.remote_port = remote_port
        self.keepalive = keepalive
        self.tls = tls
        # iso parameters
        self.use_defaults = use_defaults
        self.remote_ap_title = remote_ap_title
        self.remote_ae_qual = remote_ae_qual
        self.remote_tselector = remote_tselector
        self.remote_sselector = remote_sselector
        self.remote_pselector = remote_pselector
        self.local_ap_title = local_ap_title
        self.local_ae_qual = local_ae_qual
        self.local_tselector = local_tselector
        self.local_sselector = local_sselector
        self.local_pselector = local_pselector
        # tase2 parameters
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
            tase2_conf = yaml.load(config, Loader=yaml.FullLoader)

        # set transport parameters
        remote_server = tase2_conf['transport_parameters']['remote_server']
        remote_port = tase2_conf['transport_parameters']['remote_port']
        keepalive = tase2_conf['transport_parameters']['keepalive']
        tls = tase2_conf['transport_parameters']['tls']
        # set iso parameters
        use_defaults = tase2_conf['iso_parameters']['use_defaults']
        remote_ap_title = tase2_conf['iso_parameters']['remote_ap_title']
        remote_ae_qual = tase2_conf['iso_parameters']['remote_ae_qual']
        remote_tselector = tase2_conf['iso_parameters']['remote_tselector']
        remote_sselector = tase2_conf['iso_parameters']['remote_sselector']
        remote_pselector = tase2_conf['iso_parameters']['remote_pselector']
        local_ap_title = tase2_conf['iso_parameters']['local_ap_title']
        local_ae_qual = tase2_conf['iso_parameters']['local_ae_qual']
        local_tselector = tase2_conf['iso_parameters']['local_tselector']
        local_sselector = tase2_conf['iso_parameters']['local_sselector']
        local_pselector = tase2_conf['iso_parameters']['local_pselector']
        # set tase 2 parameters
        blt_id = tase2_conf['tase2_parameters']['blt_id']
        blt_version = tase2_conf['tase2_parameters']['blt_version']
        tase2_version = tase2_conf['tase2_parameters']['tase2_version']
        ds_name = tase2_conf['tase2_parameters']['ds_name']
        assoc_id = tase2_conf['tase2_parameters']['assoc_id']
        ae_title = tase2_conf['tase2_parameters']['ae_title']
        supported_features = tase2_conf['tase2_parameters']['supported_features']

        return cls(remote_server,
                 remote_port,
                 keepalive,
                 tls,
                 use_defaults,
                 remote_ap_title,
                 remote_ae_qual,
                 remote_tselector,
                 remote_sselector,
                 remote_pselector,
                 local_ap_title,
                 local_ae_qual,
                 local_tselector,
                 local_sselector,
                 local_pselector,
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
    if (conf.use_defaults == True):
        mms_connection = iec61850.MmsConnection_create()
    else:
        # connecting with custom ISO parameters: TSelector, SSelector, PSelector, AP-Title, AE-Qualifier
        local_tselector = iec61850.TSelector()
        local_tselector.size = len(conf.local_tselector)
        local_tselector.value = conf.local_tselector 
        local_sselector = iec61850.SSelector()
        local_sselector.size = len(conf.local_sselector)
        local_sselector.value = conf.local_sselector
        local_pselector = iec61850.PSelector()
        local_pselector.size = len(conf.local_pselector)
        local_pselector.value = conf.local_pselector 
        remote_tselector = iec61850.TSelector()
        remote_tselector.size = len(conf.remote_tselector)
        remote_tselector.value = conf.remote_tselector 
        remote_sselector = iec61850.SSelector()
        remote_sselector.size = len(conf.remote_sselector)
        remote_sselector.value = conf.remote_sselector 
        remote_pselector = iec61850.PSelector()
        remote_pselector.size = len(conf.remote_pselector)
        remote_pselector.value = conf.remote_pselector  
        mms_connection = iec61850.MmsConnection_createWisop(conf.local_ap_title,
                                                            conf.local_ae_qual,
                                                            local_tselector,
                                                            local_sselector,
                                                            local_pselector,
                                                            conf.remote_ap_title, 
                                                            conf.remote_ae_qual,
                                                            remote_tselector,
                                                            remote_sselector,
                                                            remote_pselector)
    remote_server = conf.remote_server
    remote_port = conf.remote_port
    conn = IccpConnection(mms_connection, remote_server, remote_port)

# create VCC
 # create bilateral table
    ap_title = conf.remote_ap_title
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
        success = conn.connect_to_server()
    except:
        pass
    return success

def check_bilateraltbl_attributes():
# request "Bilateral_Table_ID", "TASE2_Version", and "Supported_Features"
# check with client local values
# if values don't match issue a conclude request to server
# loop until conflict is resolved
    global conn
    global vcc
    mmsError = iec61850.toMmsErrorP()
    bltid_ok = False
    t2ver_ok = False
    success = False
    try:
        bltid_mms = iec61850.MmsConnection_readVariable(conn.MmsConnection, mmsError, vcc.domain, "Bilateral_Table_ID")
        if (iec61850.MmsValue_toString(bltid_mms) == vcc.bilateraltable.bilateral_table_id):
            bltid_ok = True
    except:
        pass
    try:
        tase2version_mms = iec61850.MmsConnection_readVariable(conn.MmsConnection, mmsError, None, "TASE2_Version")
        tase2version_val_major = iec61850.MmsValue_toUint32(iec61850.MmsValue_getElement(tase2version_mms, 0))
        tase2version_val_minor = iec61850.MmsValue_toUint32(iec61850.MmsValue_getElement(tase2version_mms, 1))
        tase2version_str = str(tase2version_val_major) + "-" + str(tase2version_val_minor)
        if (tase2version_str == vcc.bilateraltable.tase2_version):
            t2ver_ok = True
    except:
        pass
    try:
        supp_feat_mms = iec61850.MmsConnection_readVariable(conn.MmsConnection, mmsError, None, "Supported_Features")
        feat_bitstring_size = iec61850.MmsValue_getBitStringSize(supp_feat_mms)
        lst1 = [1,2,3,4,5,6,7,8,9,10,11,12]
        lst2 = []
        for i in range(feat_bitstring_size):
            lst2.append(iec61850.MmsValue_getBitStringBit(supp_feat_mms,i))
        Supported_Features = [a*b for a,b in zip(lst1,lst2)]
        filter(lambda a: a != 0, Supported_Features)
        vcc.associations[0].supported_features = ".".join(str(Supported_Features))
    except:
        pass
    success = bltid_ok and t2ver_ok
    return success

def check_connections_threads(parameter):
    pass