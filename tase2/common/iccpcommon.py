#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

from abc import ABCMeta, abstractmethod
import iec61850

class VCC:
# a TASE.2 VCC is mapped onto an MMS VMD
    
    def __init__(self,
                bilateraltable,
                domain,
                associations=[],
                datavalues=[],
                datasets=[],
                infomessages=[],
                transferaccounts=[],
                transfersets=[],
                devices=[],
                programs=[],
                eventenrollments=[]):
        self.bilateraltable = bilateraltable                
        self.domain = domain
        self.associations = associations
        self.datavalues = datavalues
        self.datasets = datasets
        self.infomessages = infomessages
        self.transferaccounts = transferaccounts
        self.transfersets = transfersets
        self.devices = devices
        self.programs = programs
        self.eventenrollments = eventenrollments
    
    def add_assoc_to_vcc(self, association):
        self.associations.append(association)
    
class Domain:
# a TASE.2 Domain is mapped onto an MMS Domain

    def __init__(self):
        pass

class BilateralTable:
# used to represent the information represented in the MMS VMD
# bilateral_table_id: identifies the version number of the BT
# tase2_version: identifies the version number of TASE.2

    def __init__(self,
                ap_title,
                blt_id,
                blt_version,
                tase2_version):
        self.bilateral_table_id = blt_id
        self.ap_title = ap_title
        self.version = blt_version
        self.tase2_version = tase2_version
       
class Association:
# supported_features: identifies the building blocks supported in the TASE.2 server

    def __init__(self, 
                 association_id, 
                 ae_title, 
                 qos, 
                 supported_features):
        self.association_id = association_id
        self.ae_title = ae_title
        self.qos = qos
        self.supported_features = supported_features
    
    def associate(self):
        pass

    def conclude(self):
        pass

    def abort(self):
        pass

class DataValue(object):
# abstract class representing either a IndicationPoint or ControlPoint or ProtectionEquipmentEvent

    __metaclass__ = ABCMeta

    def __init__(self, access_controls):
        super().__init__()
        self.acs = access_controls

    @abstractmethod    
    def getDataValue(self):
        pass

    @abstractmethod
    def setDataValue(self, value):
        pass

    @abstractmethod    
    def getDataValueNames(self):
        pass

    @abstractmethod
    def getDataValueType(self):
        pass

class DataSet():
# class representing a Dataset
    def __init__(self,
                 MmsConnection,
                 mmsError,
                 name,
                 scope,
                 transferset_id,
                 dsconditions_detected,
                 eventcode_detected,
                 transferset_timestamp,
                 datavalues,
                 access_controls):
        self.MmsConnection = MmsConnection
        self.mmsError = mmsError
        self.name = name
        self.scope = scope
        self.transferset_id = transferset_id
        self.dsconditions_detected = dsconditions_detected
        self.eventcode_detected = eventcode_detected
        self.transferset_timestamp = transferset_timestamp
        self.datavalues = datavalues
        self.access_controls = access_controls

    def create_dataset(self, ds_name, offset):
        pass

    def delete_dataset(self, ds_name, dataset_id):
        success = False
        try:
            iec61850.MmsConnection_deleteNamedVariableList(self.MmsConnection, 
                                                           self.mmsError, 
                                                           ds_name, 
                                                           dataset_id)
            success = True
        except:
            pass
        return success
    
    def get_dataset_element_values(self):
        pass

    def set_dataset_element_values(self):
        pass

    def get_dataset_names(self):
        pass

    def get_dataset_element_names(self):
        pass

class TransferSet(object):
# abstract class representing TransferSet

    __metaclass__ = ABCMeta

    def __init__(self,
                 MmsConnection,
                 mmsError,
                 name=None,
                 association_id=None,
                 status="DISABLED",
                 access_controls=None):
        super().__init__()
        self.MmsConnection = MmsConnection
        self.mmsError = mmsError
        self.name = name
        self.association_id = association_id
        self.status = status
        self.access_controls = access_controls
    
    @abstractmethod    
    def start_transfer(self):
        pass

    @abstractmethod    
    def stop_transfer(self):
        pass

    @abstractmethod    
    def get_next_transferset_value(self):
        pass

    @abstractmethod    
    def condition_monitoring(self):
        pass

    @abstractmethod    
    def transfer_report(self):
        pass

class DSTransferSet(TransferSet):
# class representing a DSTransferSet

    def __init__(self,
                 MmsConnection,
                 mmsError,    
                 name=None,
                 association_id=None,
                 status="ENABLED",
                 access_controls=None,
                 dataset_name=None,
                 DSTransmissionsPars=None,
                 EventCodeRequested=None):
        super().__init__(name,
                         association_id,
                         status,
                         access_controls,
                         MmsConnection,
                         mmsError)
        self.dataset_name = dataset_name
        self.DSTransmissionsPars = DSTransmissionsPars
        self.EventCodeRequested = EventCodeRequested

    def set_name(self, name):
        self.name = name

    def set_association_id(self, association_id):
        self.association_id = association_id

    def set_status(self, status):
        self.status = status

    def set_acs(self, acs):
        self.access_controls = acs  

    def set_dataset_name(self, ds_name):
        self.dataset_name = ds_name

    def set_DSTransmissionsPars(self, DSTransmissionsPars):
        self.DSTransmissionsPars = DSTransmissionsPars

    def set_EventCodeRequested(self, EventCodeRequested):
        self.EventCodeRequested = EventCodeRequested

    def start_transfer(self):
        pass
 
    def stop_transfer(self):
        pass

    def get_next_transferset_value(self, domain):
        next_ts_value = None
        try:
            next_ts = iec61850.MmsConnection_readVariable(self.MmsConnection, 
                                                          self.mmsError, 
                                                          domain, 
                                                          "Next_DSTransfer_Set")
            next_ts_value = iec61850.MmsValue_toString(iec61850.MmsValue_getElement(next_ts, 2))
        except:
            pass
        return next_ts_value

    def condition_monitoring(self):
        pass
    
    def transfer_report(self):
        pass

class Device():
# abstract class representing either a Device
    pass

