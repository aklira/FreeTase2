#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"

import tase2.client.client as tase2client
import yaml

conf_file = 'config_tase2.yml'

def main():
    tase2client.start_iccp(conf_file)
    pass

if __name__ == '__main__':
    main()
