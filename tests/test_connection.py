#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

import tase2.client.client as tase2client

conf_file = 'test_conn_conf.yml'

def main():
    tase2client.start_iccp(conf_file)
    result = tase2client.connect_iccp()
    print(result)

if __name__ == '__main__':
    main()
