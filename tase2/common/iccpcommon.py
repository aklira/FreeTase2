#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

from abc import ABC, abstractmethod

class VCC:
    
    def __init__(self):
        pass
    
class Domain:

    def __init__(self):
        pass

class BilateralTable:

# bilateral_table_id: identifies the version number of the BT
# tase2_version: identifies the version number of TASE.2

    def __init__(self,
                ap_title,
                bilateral_table_id,
                tase2_version,
                domain,
                ae_titles,
                associations,
                datavalues,
                datasets,
                infomessages,
                transferaccounts,
                transfersets,
                devices,
                programs,
                eventenrollments):
       self.ap-title = ap-title
       self.version = version
       self.iccpversion = iccpversion
       self.domain = domain
       self.ae-titles = ae-titles
       self.associations = associations
       self.datavalues = datavalues
       self.datasets = datasets
       self.infomessages = infomessages
       self.transferaccounts = transferaccounts
       self.transfersets = transfersets
       self.devices = devices
       self.programs = programs
       self.eventenrollments = eventenrollments
       
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
    def setDataValue(self):
        pass

    @abstractmethod    
    def getDataValueNames(self):
        pass

    @abstractmethod
    def getDataValueType(self):
        pass


