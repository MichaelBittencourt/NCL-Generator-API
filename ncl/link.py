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
from ncl.bind import Bind
from ncl.param import Param

class Link(AbstractElement):

    def __init__(self, xconnector, id=None):

        listAttributes = ["id", "xconnector"]

        listChildren = [Bind, Param]
        super().__init__("link", listAttributes, listChildren)

        self.set("xconnector", xconnector)
        if id is not None:
            self.set("id", id)

    def customizeItem(self, item):
        if isinstance(item, Param):
            item.setTagName("linkParam")
        return item

    pass
