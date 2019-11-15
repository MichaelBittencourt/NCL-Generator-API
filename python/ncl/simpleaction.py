#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from lxml import etree

class SimpleAction:

    role = None

    def __init__(self, role):
        self.role = role

    def getElement(self):
        simpleAction = etree.Element("simpleAction")
        simpleAction.set("role", self.role)
        return simpleAction
        

    def generate(self):
        print("Constructor call generate")

    pass
