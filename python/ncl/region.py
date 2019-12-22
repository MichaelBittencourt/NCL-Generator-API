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

class Region(AbstractElement):

    def __init__(self, id, height=None, width=None, title=None,  top=None, botton=None, left=None, right=None, zIndex=None):
        listAttributes = ["id", "height", "width", "title",  "top", "botton", "left", "right", "zIndex"]
        listChildren = [Region]
        super().__init__("region", listAttributes, listChildren)
        self.set("id", id)
        if title is not None:
            self.set("title", title)
        if height is not None:
            self.set("height", height)
        if width is not None:
            self.set("width", width)
        if top is not None:
            self.set("top", top)
        if botton is not None:
            self.set("botton", botton)
        if left is not None:
            self.set("left", left)
        if right is not None:
            self.set("right", right)
        if zIndex is not None:
            self.set("zIndex", zIndex)

    pass

