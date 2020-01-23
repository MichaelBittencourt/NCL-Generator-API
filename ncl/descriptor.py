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
from ncl.param import Param

class Descriptor(AbstractElement):

    def __init__(self, id, player=None, explicitDur=None, region=None, freeze=None, moveLeft=None, moveRight=None, moveUp=None, moveDown=None, focusIndex=None, focusBorderColor=None, focusBorderWidth=None, focusBorderTransparency=None, focusSrc=None, focusSelSrc=None, selBorderColor=None, transIn=None, transOut=None):
        listAttributes = ["id", "player", "explicitDur", "region", "freeze", "moveLeft", "moveRight", "moveUp", "moveDown", "focusIndex", "focusBorderColor", "focusBorderWidth", "focusBorderTransparency", "focusSrc", "focusSelSrc", "selBorderColor", "transIn", "transOut"]

        listChildren = [Param]

        super().__init__("descriptor", listAttributes, listChildren)
        self.set("id", id)
        if player is not None:
            self.set("player", player)
        if explicitDur is not None:
            self.set("explicitDur", explicitDur)
        if region is not None:
            self.set("region", region)
        if freeze is not None:
            self.set("freeze", freeze)
        if moveLeft is not None:
            self.set("moveLeft", moveLeft)
        if moveRight is not None:
            self.set("moveRight", moveRight)
        if moveUp is not None:
            self.set("moveUp", moveUp)
        if moveDown is not None:
            self.set("moveDown", moveDown)
        if focusIndex is not None:
            self.set("focusIndex", focusIndex)
        if focusBorderColor is not None:
            self.set("focusBorderColor", focusBorderColor)
        if focusBorderWidth is not None:
            self.set("focusBorderWidth", focusBorderWidth)
        if focusBorderTransparency is not None:
            self.set("focusBorderTransparency", focusBorderTransparency)
        if focusSrc is not None:
            self.set("focusSrc", focusSrc)
        if focusSelSrc is not None:
            self.set("focusSelSrc", focusSelSrc)
        if selBorderColor is not None:
            self.set("selBorderColor", selBorderColor)
        if transIn is not None:
            self.set("transIn", transIn)
        if transOut is not None:
            self.set("transOut", transOut)

    def customizeItem(self, item):
        if isinstance(item, Param):
            item.setTagName("descriptorParam")
        return item

    pass
