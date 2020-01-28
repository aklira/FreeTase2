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

    def read_dataset(self,
                     ds_name,
                     offset):
        pass

    def create_dataset(self,
                       ds_name,
                       offset):
        pass

    def write_dataset(self, 
                      id_iccp, 
                      ds_name, 
                      ts_name, 
                      buffer_time, 
                      integrity_time, 
                      all_changes_reported):
        pass

    def get_next_transferset(self, id_iccp):
        pass

    def check_connection(self, id_iccp, loop_error):
        pass

    def command_variable(self, variable, value):
        pass

def read_conf(file):
    pass

