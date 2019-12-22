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

class Area:

    def __init__(self, id, coords=None, begin=None, end=None, beginText=None, endText=None, beginPosition=None, endPosition=None, first=None, last=None, label=None, clip=None):
        self.id = id
        self.coords = coords
        self.begin = begin
        self.end = end
        self.beginText = beginText
        self.endText = endText
        self.beginPosition = beginPosition
        self.endPosition = endPosition
        self.first = first
        self.last = last
        self.label = label
        self.clip = clip

    def getElement(self):
        area = etree.Element("area")
        area.set("id", self.id)
        if self.coords is not None:
            area.set("coords", self.coords)
        if self.begin is not None:
            area.set("begin", self.begin)
        if self.end is not None:
            area.set("end", self.end)
        if self.beginText is not None:
            area.set("beginText", self.beginText)
        if self.endText is not None:
            area.set("endText", self.endText)
        if self.beginPosition is not None:
            area.set("beginPosition", self.beginPosition)
        if self.endPosition is not None:
            area.set("endPosition", self.endPosition)
        if self.first is not None:
            area.set("first", self.first)
        if self.last is not None:
            area.set("last", self.last)
        if self.label is not None:
            area.set("label", self.label)
        if self.clip is not None:
            area.set("clip", self.clip)
        return area

    def generate(self):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, method="xml", pretty_print=True).decode()

    pass
