#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

from iccpcommon import DataValue

class IndicationPoint(DataValue):

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
                 COVClass):
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
       self.timestamp
       self.timestampquality
       self.COVClass

