#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

from lxml import etree
from ncl.body import Body
from ncl.head import Head
from ncl.port import Port
from ncl.media import Media
from ncl.region import Region
from ncl.descriptor import Descriptor
from ncl.causalconnector import CausalConnector
from ncl.simplecondition import SimpleCondition
from ncl.simplecondition import SimpleCondition
from ncl.compoundcondition import CompoundCondition
from ncl.simpleaction import SimpleAction
from ncl.compoundaction import CompoundAction
from ncl.link import Link
from ncl.bind import Bind
from ncl.area import Area
from ncl.property import Property

class Ncl:

    head = None
    body = None
    id = None
    xmlns = None

    def __init__(self, id=None, xmlns=None):
        self.id = id
        self.xmlns = xmlns
        self.head = Head() 
        self.body = Body() 

    def add(self, nclComponent):
        if isinstance(nclComponent, Region) or isinstance(nclComponent, Descriptor) or isinstance(nclComponent, CausalConnector):
            self.head.add(nclComponent)
        else:
           self.body.add(nclComponent)

    def getElement(self):
        nclCode = etree.Element('ncl')
        if self.id is not None:
            nclCode.set("id", self.id)
        if self.xmlns is not None:
            nclCode.set("xmlns", self.xmlns)
        nclCode.append(self.head.getElement())
        nclCode.append(self.body.getElement())
        return nclCode

    def generate(self):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, encoding="iso-8859-1", method="xml", pretty_print=True).decode()
    
    pass

if __name__ == "__main__":
    """import sys
    print("Console args[1] = " + sys.argv[1])"""
    print("Create a simple Example:")
    print("""from ncl import *
nclCode = Ncl(\"nclv1\", \"http://www.ncl.org.br/NCL3.0/EDTVProfile\")

region = Region(id=\"regImage\", height=\"15%\", width=\"100%\", top=\"0\", left=\"10%\", zIndex=\"10\")
descriptor = Descriptor(id=\"descImage\", region=\"regImage\")
media = Media(id=\"image\", descriptor=\"descImage\", src=\"lena.jpg\")
port = Port(id=\"pImage\", component=\"image\")

region2 = Region(id=\"regImage2\", height=\"15%\", width=\"100%\", top=\"0\", left=\"10%\", zIndex=\"10\")
descriptor2 = Descriptor(id=\"descImage2\", region=\"regImage2\")
media2 = Media(id=\"image2\", descriptor=\"descImage2\", src=\"lena.jpg\")
port2 = Port(id=\"pImage2\", component=\"image2\")

nclCode.add(region)
nclCode.add(descriptor)
nclCode.add(media)
nclCode.add(port)

nclCode.add(region2)
nclCode.add(descriptor2)
nclCode.add(media2)
nclCode.add(port2)
print(nclCode.generate())
          
generate this File file:
          
    """)
    nclCode = Ncl("nclv1", "http://www.ncl.org.br/NCL3.0/EDTVProfile")

    region = Region(id="regImage", height="15%", width="100%", top="0", left="10%", zIndex="10")
    descriptor = Descriptor(id="descImage", region="regImage")
    media = Media(id="image", descriptor="descImage", src="lena.jpg")
    port = Port(id="pImage", component="image")

    region2 = Region(id="regImage2", height="15%", width="100%", top="0", left="10%", zIndex="10")
    descriptor2 = Descriptor(id="descImage2", region="regImage2")
    media2 = Media(id="image2", descriptor="descImage2", src="lena.jpg")
    port2 = Port(id="pImage2", component="image2")

    nclCode.add(region)
    nclCode.add(descriptor)
    nclCode.add(media)
    nclCode.add(port)

    nclCode.add(region2)
    nclCode.add(descriptor2)
    nclCode.add(media2)
    nclCode.add(port2)
    print(nclCode.generate())

