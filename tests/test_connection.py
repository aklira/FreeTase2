#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

import sys
sys.path.insert(0, "..")

import tase2.client.client as tase2client
from time import sleep

conf_file = 'test_conn_conf.yml'

def main():
    tase2client.start_iccp(conf_file)
    # create and start connection
    result = tase2client.connect_iccp()
    # check bilateral tables attributes
    result = tase2client.check_bilateraltbl_attributes()
    # keep connection alive until user interrupts
    while 1:
       print(result)
       sleep(10)

if __name__ == '__main__':
    main()
