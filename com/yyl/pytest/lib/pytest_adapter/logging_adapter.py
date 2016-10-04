#!/usr/bin/env python
# encoding: utf-8

import os
import logging
import logging.config

def pytest_addoption(parser):
    ''' add options for generate results and structure file '''
    group = parser.getgroup("Test", "Test options")
    group.addoption('--logconf', action="store",
                    metavar="path", default="config/logging.conf",
                    help="path for logging config file, default %default")

def pytest_configure(config):

    ''' read or use default option value, create default file '''
    logconf = config.getoption("--logconf")
    current_dir = os.getcwd()

    if not os.path.isdir('%s/log' % current_dir):
        os.makedirs('%s/log' % current_dir)

    curr_file = os.path.abspath(logconf)

    if os.path.isfile(curr_file):
        ''' load logging configuration '''
        logging.config.fileConfig(curr_file)
    else:
        raise Exception('Cannot find logging configuration file:%s' % logconf)
