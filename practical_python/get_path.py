#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:32:59 2019

Print all PDF file paths under a root folder.
(some PDFs are under subfolder of the root folder)


@author: chengchen
"""

import os
from os import walk

dir_path = os.path.dirname(os.path.realpath(__file__))

f_list = []
for (dirpath, dirnames, filenames) in walk(dir_path):
    f_list.extend(filenames)
f_pdf_list = []
for f in f_list:
    if f[-4:]=='.pdf':
        f_pdf_list.append(f)
print(f_pdf_list)    