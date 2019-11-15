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

class Port:

    id = None
    component = None

    def __init__(self, id, component):
        self.id = id
        self.component = component

    def getElement(self):
        port = etree.Element("port")
        port.set("id", self.id)
        port.set("component", self.component)
        return port

    pass

