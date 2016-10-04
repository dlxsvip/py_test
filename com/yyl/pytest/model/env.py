#!/usr/bin/python
# -*- coding:UTF-8 -*-
__author__ = 'yyl'

import os


__conf_file_type__=['json','yaml']

def load(conf_file,type='json'):
    if type not in __conf_file_type__:
        raise Exception('Invalid file type %s Vailed types: %s'%(type,__conf_file_type__) )
    file_path = os.path.abspath(conf_file)
    if not os.path.isfile(file_path):
        raise Exception('File not exist. %s' % file_path)
    yf = eval('''%s.load(open(conf_file,'r'))''' % type)

    for key in yf.keys():
        globals()[key] = yf[key]