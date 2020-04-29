#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

import sys
sys.path.insert(0, "..")

import tase2.client.client as tase2client
from time import sleep
import signal

conf_file = 'test_conn_conf.yml'
data_conf = 'simple_data_conf.json'

running = True

def sigint_handler(signalNumber, frame):
    global running
    running = False

def main():

    # user interruption handling
    signal.signal(signal.SIGINT, sigint_handler)

    # init iccp
    result = tase2client.init_iccp(conf_file)
    if (not result):
        print("ICCP init error")
    else:
        print("ICCP init ok")
    # create and start connection
    result = tase2client.connect_iccp()
    if (not result):
        print("ICCP connection error")
    else:
        print("ICCP connection ok")
    result = tase2client.start_iccp(data_conf)
    if (not result):
        print("ICCP client start-up error")
    else:
        print("ICCP client start-up ok")    
    # keep connection alive until user interrupts
    while(running):
       if (not result):
           break
       print("Client process running")
       sleep(10)
    
    quit()

if __name__ == '__main__':
    main()
