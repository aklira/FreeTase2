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
    # init iccp
    result = tase2client.init_iccp(conf_file)
    if (not result):
        print("ICCP init error")
    # create and start connection
    result = tase2client.connect_iccp()
    if (not result):
        print("ICCP connection error")
    result = tase2client.start_iccp()
    if (not result):
        print("ICCP start-up error")    
    # keep connection alive until user interrupts
    while 1:
       print(result)
       sleep(10)

if __name__ == '__main__':
    main()
