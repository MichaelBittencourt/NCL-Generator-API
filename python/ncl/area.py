#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.abstractelement import AbstractElement

class Area(AbstractElement):

    def __init__(self, id, coords=None, begin=None, end=None, beginText=None, endText=None, beginPosition=None, endPosition=None, first=None, last=None, label=None, clip=None):
        listAttributes = ["id", "coords", "begin", "end", "beginText", "endText", "beginPosition", "endPosition", "first", "last", "label", "clip"]
        super().__init__("area", listAttributes, [])
        self.set("id", id)
        if coords is not None:
            self.set("coords", coords)
        if begin is not None:
            self.set("begin", begin)
        if end is not None:
            self.set("end", end)
        if beginText is not None:
            self.set("beginText", beginText)
        if endText is not None:
            self.set("endText", endText)
        if beginPosition is not None:
            self.set("beginPosition", beginPosition)
        if endPosition is not None:
            self.set("endPosition", endPosition)
        if first is not None:
            self.set("first", first)
        if last is not None:
            self.set("last", last)
        if label is not None:
            self.set("label", label)
        if clip is not None:
            self.set("clip", clip)

    pass
