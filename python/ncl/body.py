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
from ncl.port import Port
from ncl.media import Media
from ncl.link import Link

class Body:

    listPort = []
    listMedia = []
    listLink = []

    def __init__(self):
        self.listPort = []
        self.listMedia = []
        self.listLink = []

    def add(self, nclComponent):
        if isinstance(nclComponent, Port):
            self.listPort.append(nclComponent)
        elif isinstance(nclComponent, Media):
            self.listMedia.append(nclComponent)
        elif isinstance(nclComponent, Link):
            self.listLink.append(nclComponent)

    def getElement(self):
        head = etree.Element("body")
        for i in self.listPort:
            head.append(i.getElement())
        for i in self.listMedia:
            head.append(i.getElement())
        for i in self.listLink:
            head.append(i.getElement())
        return head

    pass

