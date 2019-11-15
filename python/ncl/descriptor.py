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

class Descriptor:

    id = None
    region = None

    def __init__(self, id, region):
        self.id = id
        self.region = region

    def getElement(self):
        descriptor = etree.Element("descriptor")
        descriptor.set("id", self.id)
        descriptor.set("region", self.region)
        return descriptor
        

    def generate(self):
        print("Constructor call generate")

    pass
