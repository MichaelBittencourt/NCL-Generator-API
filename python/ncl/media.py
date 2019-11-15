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

class Media:

    id = None
    descriptor = None
    src = None

    def __init__(self, id, descriptor, src):
        self.id = id
        self.descriptor = descriptor
        self.src = src

    def getElement(self):
        media = etree.Element("media")
        media.set("id", self.id)
        media.set("descriptor", self.descriptor)
        media.set("src", self.src)
        return media

    pass
