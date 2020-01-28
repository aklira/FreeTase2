#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

from abc import ABC, abstractmethod

class VCC:
# a TASE.2 VCC is mapped onto an MMS VMD
    
    def __init__(self,
                bilateraltable,
                domain=None,
                ae_titles=None,
                associations=None,
                datavalues=None,
                datasets=None,
                infomessages=None,
                transferaccounts=None,
                transfersets=None,
                devices=None,
                programs=None,
                eventenrollments=None):
        self.bilateraltable = bilateraltable                
        self.domain = domain
        self.ae_titles = ae_titles
        self.associations = associations
        self.datavalues = datavalues
        self.datasets = datasets
        self.infomessages = infomessages
        self.transferaccounts = transferaccounts
        self.transfersets = transfersets
        self.devices = devices
        self.programs = programs
        self.eventenrollments = eventenrollments
    
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
                bilateral_table_id,
                version,
                tase2_version):
        self.bilateral_table_id = bilateral_table_id
        self.ap_title = ap_title
        self.version = version
        self.tase2_version = tase2_version
       
class Association():

# supported_features: identifies the building blocks supported in the TASE.2 server

    def __init__(self, 
                 association_id, 
                 ae_title, 
                 qos, 
                 supported_features): # 
        self.association_id = association_id
        self. ae_title =  ae_title
        self.qos = qos
        self.supported_features = supported_features
    
    def associate(self):
        pass

    def conclude(self):
        pass

    def abort(self):
        pass

class DataValue(ABC):

    def __init__(self, acs):
        super().__init__()
        self.acs = acs

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


