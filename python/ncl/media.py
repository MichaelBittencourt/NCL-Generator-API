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
from ncl.area import Area
from ncl.property import Property

class Media:

    def __init__(self, id, descriptor, src, typeMedia=None, refer=None, instance=None):
        self.id = id
        self.descriptor = descriptor
        self.src = src
        self.type = typeMedia
        self.refer = refer
        self.instance = instance
        self.listArea = []
        self.listProperty = []

    def add(self, nclComponent):
        if isinstance(nclComponent, Area):
            self.listArea.append(nclComponent)
        elif isinstance(nclComponent, Property):
            self.listProperty.append(nclComponent)

    def getElement(self):
        media = etree.Element("media")
        media.set("id", self.id)
        media.set("descriptor", self.descriptor)
        media.set("src", self.src)
        if self.type is not None:
            media.set("type", self.type)
        if self.refer is not None:
            media.set("refer", self.refer)
        if self.instance is not None:
            media.set("instance", self.instance)
        for i in self.listArea:
            media.append(i.getElement())
        for i in self.listProperty:
            media.append(i.getElement())
        return media

    def generate(self):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, method="xml", pretty_print=True).decode()

    pass
