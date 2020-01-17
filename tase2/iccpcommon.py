#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

'''
Free and open implementation of the IEC 60870-6 TASE.2 protocol
'''

class VCC:

class Domain:

class BilateralTable:

    def __init__(self
                ap_title,
                version,
                iccpversion,
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

class DataValue:

    def __init__(self, name, type, acs):
        self.name = name
        self.acs = acs

