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
from ncl.area import Area
from ncl.property import Property

class Media(AbstractElement):

    def __init__(self, id, descriptor, src, typeMedia=None, refer=None, instance=None):
        listAttributes = ["id", "descriptor", "src", "type", "refer", "instance"]
        listChildren = [Area, Property]
        super().__init__("media", listAttributes, listChildren)
        self.set("id", id)
        self.set("descriptor", descriptor)
        self.set("src", src)
        if typeMedia is not None:
            self.set("type", typeMedia)
        if refer is not None:
            self.set("refer", refer)
        if instance is not None:
            self.set("instance", instance)

    pass
