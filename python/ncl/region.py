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

class Region:

    id = None
    height = None
    width = None
    title = None
    top = None
    botton = None
    left = None
    right = None
    zIndex = None
    listRegion = []


    def __init__(self, id=None, height=None, width=None, title=None,  top=None, botton=None, left=None, right=None, zIndex=None):
        self.id = id
        self.height = height
        self.width = width
        self.top = top
        self.left = left
        self.zIndex = zIndex
        self.listRegion = []

    def getElement(self):
        region = etree.Element("region")
        region.set("id", self.id)
        region.set("height", self.height)
        region.set("width", self.width)
        if self.top is not None:
            region.set("top", self.top)
        if self.left is not None:
            region.set("left", self.left)
        if self.zIndex is not None:
            region.set("zIndex", self.zIndex)
        for i in self.listRegion:
            region.append(i.getElement())
        return region
        
    def generate(self):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, method="xml", pretty_print=True).decode()
    
    def add(self, nclComponent):
        if isinstance(nclComponent, Region):
            self.listRegion.append(nclComponent)

    def getChild(self, id):
        for iten in self.listRegion:
            if item.getId() == id: 
                return item

    def setId(self, id):
        self.id = id;

    def getId(self):
        return self.id

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setTop(self, top):
        self.top = top

    def getTop(self):
        return self.top

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def setZIndex(self, zIndex):
        self.zIndex = zIndex

    def getZIndex(self):
        return self.zIndex

    """
    def setListRegion(self, listRegion):
        self.listRegion = listRegion

    def getListRegion(self):
        return self.listRegion
    """
    pass

