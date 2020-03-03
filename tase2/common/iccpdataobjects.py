#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

from tase2.common.iccpcommon import DataValue

class IndicationPoint(DataValue):
# class representing a IndicationPoint

    def __init__(self,
                 name,
                 type,
                 realvalue,
                 statevalue,
                 discretevalue,
                 qualityclass,
                 validity,
                 currentsource,
                 normalsource,
                 normalvalue,
                 timestampclass,
                 timestamp,
                 timestampquality,
                 COVClass,
                 acs):
       super().__init__(acs) 
       self.name = name
       self.type = type
       self.realvalue = realvalue
       self.statevalue = statevalue
       self.discretevalue = discretevalue
       self.qualityclass = qualityclass
       self.validity = validity
       self.currentsource = currentsource
       self.normalsource = normalsource
       self.timestampclass = timestampclass
       self.timestamp = timestamp
       self.timestampquality = timestampquality
       self.COVClass = COVClass
    
    def getDataValue(self):
        pass

    def setDataValue(self, value):
        pass

    def getDataValueNames(self):
        pass

    def getDataValueType(self):
        pass

class ControlPoint(DataValue):
# class representing a ControlPoint

    def __init__(self,
                 name,
                 type,
                 commandvalue,
                 setpointtype,
                 setpointrealvalue,
                 setpointdiscretevalue,
                 deviceclass,
                 checkbackname,
                 state,
                 timeout,
                 tagclass,
                 tag,
                 tagstate,
                 reason,
                 acs):
       super().__init__(acs)
       self.name = name
       self.type = type
       self.commandvalue = commandvalue
       self.setpointtype = setpointtype
       self.setpointrealvalue = setpointrealvalue
       self.setpointdiscretevalue = setpointdiscretevalue
       self.deviceclass = deviceclass
       self.checkbackname = checkbackname
       self.state = state
       self.timeout = timeout
       self.tagclass = tagclass
       self.tag = tag
       self.tagstate = tagstate
       self.reason = reason
    
    def getDataValue(self):
        pass

    def setDataValue(self, value):
        pass

    def getDataValueNames(self):
        pass

    def getDataValueType(self):
        pass

class ProtectionEquipmentEvent(DataValue):
# class representing a ProtectionEquipmentEvent

    def __init__(self):
        pass

