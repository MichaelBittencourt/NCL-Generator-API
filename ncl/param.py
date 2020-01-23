#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.abstractparam import AbstractParam

class Param(AbstractParam):

    def __init__(self, name, value, tagName=None):
        super().__init__("name", "value")
        self._setTagName(tagName)
        self.set("name", name)
        self.set("value", value)

    def setTagName(self, tagName):
        self._setTagName(tagName) 

    pass
