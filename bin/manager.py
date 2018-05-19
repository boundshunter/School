#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.main import Main

if __name__ == '__main__':
    func = Main()