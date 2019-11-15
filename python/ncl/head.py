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
from ncl.region import Region
from ncl.descriptor import Descriptor
from ncl.causalconnector import CausalConnector

class Head:

    def __init__(self):
        self.listRegion = []
        self.listDescriptor = []
        self.listConnector = []

    def add(self, nclComponent):
        if isinstance(nclComponent, Region):
            self.listRegion.append(nclComponent)
        elif isinstance(nclComponent, Descriptor):
            self.listDescriptor.append(nclComponent)
        elif isinstance(nclComponent, CausalConnector):
            self.listConnector.append(nclComponent)

    def getElement(self):
        head = etree.Element("head")
        regionBase = etree.Element("regionBase")
        descriptorBase = etree.Element("descriptorBase")
        connectorBase = etree.Element("connectorBase")
        for i in self.listRegion:
            regionBase.append(i.getElement())
        for i in self.listDescriptor:
            descriptorBase.append(i.getElement())
        for i in self.listConnector:
            connectorBase.append(i.getElement())
        head.append(regionBase)
        head.append(descriptorBase)
        head.append(connectorBase)
        return head

    pass
