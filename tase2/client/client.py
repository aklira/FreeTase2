#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

from tase2.common.iccpcommon import VCC, BilateralTable, Association, DataSet, DSTransferSet
from tase2.common.iccpdataobjects import IndicationPoint
import yaml, json
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
                 domain,
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
        self.domain = domain
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
        domain = tase2_conf['tase2_parameters']['domain']
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
                 domain,
                 assoc_id,
                 ae_title,
                 supported_features)


conn = None
vcc = None
iccpconf = None
dataconf = None

REPORT_BUFFERED=0x01
REPORT_INTERVAL_TIMEOUT=0x02
REPORT_OBJECT_CHANGES=0x04

integrity_time=0 
analog_buf=0 
digital_buf=0 
events_buf=0

def init_iccp(conf_file):
    global conn
    global vcc
    global conf
    success = False
# create tase2 conf from file 
    iccpconf = IccpConf.create_from_file(conf_file)

# create IccpConnection
    if (iccpconf.use_defaults == True):
        mms_connection = iec61850.MmsConnection_create()
    else:
        # connecting with custom ISO parameters: TSelector, SSelector, PSelector, AP-Title, AE-Qualifier
        local_tselector = iec61850.TSelector()
        local_tselector.size = len(iccpconf.local_tselector)
        local_tselector.value = iccpconf.local_tselector 
        local_sselector = iec61850.SSelector()
        local_sselector.size = len(iccpconf.local_sselector)
        local_sselector.value = iccpconf.local_sselector
        local_pselector = iec61850.PSelector()
        local_pselector.size = len(iccpconf.local_pselector)
        local_pselector.value = iccpconf.local_pselector 
        remote_tselector = iec61850.TSelector()
        remote_tselector.size = len(iccpconf.remote_tselector)
        remote_tselector.value = iccpconf.remote_tselector 
        remote_sselector = iec61850.SSelector()
        remote_sselector.size = len(iccpconf.remote_sselector)
        remote_sselector.value = iccpconf.remote_sselector 
        remote_pselector = iec61850.PSelector()
        remote_pselector.size = len(iccpconf.remote_pselector)
        remote_pselector.value = iccpconf.remote_pselector  
        mms_connection = iec61850.MmsConnection_createWisop(iccpconf.local_ap_title,
                                                            iccpconf.local_ae_qual,
                                                            local_tselector,
                                                            local_sselector,
                                                            local_pselector,
                                                            iccpconf.remote_ap_title, 
                                                            iccpconf.remote_ae_qual,
                                                            remote_tselector,
                                                            remote_sselector,
                                                            remote_pselector)
    remote_server = iccpconf.remote_server
    remote_port = iccpconf.remote_port
    conn = IccpConnection(mms_connection, remote_server, remote_port)

# create VCC
 # create bilateral table
    ap_title = iccpconf.remote_ap_title
    blt_id = iccpconf.blt_id
    blt_version = iccpconf.blt_version
    tase2_version = iccpconf.tase2_version
    bilateraltable = BilateralTable(ap_title, blt_id, blt_version, tase2_version)

    domain = iccpconf.domain
    vcc = VCC(bilateraltable, domain)

# create Association
    assoc_id = iccpconf.assoc_id
    ae_title = iccpconf.ae_title
    assoc = Association(assoc_id, ae_title, 0, None)
    vcc.add_assoc_to_vcc(assoc)

    success = True

    return success

def connect_iccp():
    global conn
    success = False
    try:
        success = conn.connect_to_server()
    except:
        pass
    return success

def start_iccp(dataconf_file):
    global conn
    global vcc
    mmsError = iec61850.toMmsErrorP()
    success = False
    chk_blt_tbl_ok = False
    del_datasets_ok = False
    read_dataconf_ok = False
    create_ts_ok = False
    create_ds_ok = False
    add_ds_ts_ok = False

# check bilateral tables attributes
    try:
        chk_blt_tbl_ok = check_bilateraltbl_attributes()
    except:
        print("Error in checking bilateral tables attributes")
        pass

# delete existing datasets
    try:
        if (len(vcc.datasets) != 0):
            for dataset in vcc.datasets:
                del_datasets_ok = dataset.delete_dataset(vcc.domain, dataset.name)
        else:
            del_datasets_ok = True
    except:
        print("Error in deleting datasets")
        pass

# create datasets from input file
    try:
        dataconf = readDataConf(dataconf_file, conn.MmsConnection, mmsError)
        read_dataconf_ok = (len(dataconf) != 0)
    except:
        pass

    try:        
        for ds_item in dataconf:
            vars = iec61850.LinkedList_create()
            name = iec61850.MmsVariableAccessSpecification_create(vcc.domain, "Transfer_Set_Name")
            tst = iec61850.MmsVariableAccessSpecification_create(vcc.domain, "Transfer_Set_Time_Stamp")
            dsc = iec61850.MmsVariableAccessSpecification_create(vcc.domain, "DSConditions_Detected")
            iec61850.LinkedList_add(vars, name)
            iec61850.LinkedList_add(vars, tst)
            iec61850.LinkedList_add(vars, dsc)

            var_s_lst = []
            for dv_item in ds_item.datavalues:
                var = iec61850.MmsVariableAccessSpecification_create(vcc.domain, dv_item.name.encode("utf-8"))
                iec61850.LinkedList_add(vars, var)
                # fixes a bug with the var pointing to the last item of the dv_item list 
                var_s_lst.append(iec61850.getMmsVASItemId(var))

            iec61850.MmsConnection_defineNamedVariableList(conn.MmsConnection, 
                                                           mmsError, 
                                                           vcc.domain, 
                                                           ds_item.name.encode("utf-8"), 
                                                           vars)
        create_ds_ok = True
    except:
        print("Error in creating datasets from input file")
        pass

# create transfersets
    ds_ts_lst = []
    try:
        for ds_item in dataconf:
            ds_ts = DSTransferSet(conn.MmsConnection, mmsError)
            next_ts = iec61850.MmsConnection_readVariable(conn.MmsConnection, 
                                                          mmsError, 
                                                          vcc.domain, 
                                                          "Next_DSTransfer_Set")
            next_ts_value = iec61850.MmsValue_toString(iec61850.MmsValue_getElement(next_ts, 2))
            #next_ts = ds_ts.get_next_transferset_value(vcc.domain)
            ds_ts.set_name(next_ts_value)
            ds_ts.set_dataset_name(ds_item.name)
            ds_ts.set_dataset_type(ds_item.ds_type)
            ds_ts.set_association_id(vcc.associations[0].association_id)
            ds_ts.set_status = "ENABLED"
            ds_ts_lst.append(ds_ts)

        create_ts_ok = (len(ds_ts_lst) != 0)
    except:
        print("Error in creating transfersets")
        pass

# add datasets to transfersets
    for ds_ts_item in ds_ts_lst:
        try:
            if (ds_ts_item.dataset_type == "analog"):
                print("analog dataset detected")
                add_ds_ts_ok = write_dataset(conn.MmsConnection,
                            mmsError,  
                            vcc.domain, 
                            ds_ts_item.dataset_name, 
                            ds_ts_item.name, 
                            analog_buf, 
                            integrity_time, 
                            REPORT_INTERVAL_TIMEOUT|REPORT_OBJECT_CHANGES|REPORT_BUFFERED)
            elif (ds_ts_item.dataset_type == "digital"):
                 print("digital dataset detected")
                 add_ds_ts_ok = write_dataset(conn.MmsConnection,
                            mmsError,  
                            vcc.domain, 
                            ds_ts_item.dataset_name, 
                            ds_ts_item.name, 
                            digital_buf, 
                            integrity_time, 
                            REPORT_INTERVAL_TIMEOUT|REPORT_OBJECT_CHANGES)
            elif (ds_ts_item.dataset_type == "events"):
                 print("events dataset detected")
                 add_ds_ts_ok = write_dataset(conn.MmsConnection,
                            mmsError,  
                            vcc.domain, 
                            ds_ts_item.dataset_name, 
                            ds_ts_item.name, 
                            events_buf, 
                            integrity_time, 
                            REPORT_OBJECT_CHANGES)
            else:
                add_ds_ts_ok = False
        except:
            print("Error in adding datasets to transfersets")
            pass
    success = chk_blt_tbl_ok and del_datasets_ok and read_dataconf_ok and create_ds_ok and create_ts_ok and add_ds_ts_ok
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
        else:
            iec61850.MmsConnection_conclude(conn.MmsConnection, mmsError)
    except:
        pass
    try:
        tase2version_mms = iec61850.MmsConnection_readVariable(conn.MmsConnection, mmsError, None, "TASE2_Version")
        tase2version_val_major = iec61850.MmsValue_toUint32(iec61850.MmsValue_getElement(tase2version_mms, 0))
        tase2version_val_minor = iec61850.MmsValue_toUint32(iec61850.MmsValue_getElement(tase2version_mms, 1))
        tase2version_str = str(tase2version_val_major) + "-" + str(tase2version_val_minor)
        if (tase2version_str == vcc.bilateraltable.tase2_version):
            t2ver_ok = True
        else:
            iec61850.MmsConnection_conclude(conn.MmsConnection, mmsError)
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

def readDataConf(json_file, mmsConnection, mmsError):
    with open(json_file, 'r') as data_conf:
        dataconf = json.load(data_conf)
    
    ds_lst = []
    for ds_item in dataconf['datasets']:
        dv_lst = []
        for dv_item in ds_item['ds_values']:
                dv = IndicationPoint(dv_item['id'], dv_item['type'])
                dv_lst.append(dv)
        ds = DataSet(mmsConnection, mmsError, ds_item['ds_name'], ds_item['ds_type'], dv_lst)
        ds_lst.append(ds)
    
    return ds_lst

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
    iec61850.MmsValue_setBoolean(elem, True)

    elem = iec61850.MmsValue_getElement(dataset, 8)
    iec61850.MmsValue_setBoolean(elem, True)

    elem = iec61850.MmsValue_getElement(dataset, 9)
    iec61850.MmsValue_setBoolean(elem, True)

    elem = iec61850.MmsValue_getElement(dataset, 10)
    if(all_changes_reported&REPORT_BUFFERED):
        iec61850.MmsValue_setBoolean(elem, False)
    else:
        iec61850.MmsValue_setBoolean(elem, True)

    elem = iec61850.MmsValue_getElement(dataset, 11)
    iec61850.MmsValue_setBoolean(elem, True)

    elem = iec61850.MmsValue_getElement(dataset, 12)
    iec61850.MmsValue_setInt32(elem, 0)

    result = iec61850.MmsConnection_writeVariable(mmsConnection, mmsError, domain, ts_name, dataset)
    print(result)

    success = True

    return success