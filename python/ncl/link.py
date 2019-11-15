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
from ncl.bind import Bind

class Link:

    xconnector = None
    listBinds = []

    def __init__(self, xconnector):
        self.xconnector = xconnector
        self.listBinds = []

    def add(self, nclComponent):
        if isinstance(nclComponent, Bind):
            self.listBinds.append(nclComponent)

    def getElement(self):
        link = etree.Element("link", xconnector=self.xconnector)
        for i in self.listBinds:
            link.append(i.getElement())
        return link

    def generate(self):
        print("Constructor call generate")

    pass
