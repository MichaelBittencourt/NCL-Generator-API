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

class Property:

    def __init__(self, name, value=None, externable=None):
        self.name = name
        self.value = value
        self.externable = externable

    def getElement(self):
        propertyElement = etree.Element("property")
        propertyElement.set("name", self.name)
        propertyElement.set("value", self.value)
        if self.externable is not None:
            propertyElement.set("externable", self.value)
        return propertyElement
    
    def generate(self):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, method="xml", pretty_print=True).decode()

    pass
