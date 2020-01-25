#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

from ncl.abstractelement import AbstractElement
from ncl.body import Body
from ncl.head import Head
from ncl.regionbase import RegionBase
from ncl.descriptorbase import DescriptorBase
from ncl.connectorbase import ConnectorBase
from ncl.port import Port
from ncl.media import Media
from ncl.region import Region
from ncl.descriptor import Descriptor
from ncl.causalconnector import CausalConnector
from ncl.simplecondition import SimpleCondition
from ncl.compoundcondition import CompoundCondition
from ncl.assessmentstatement import AssessmentStatement
from ncl.attributeassessment import AttributeAssessment
from ncl.compoundstatement import CompoundStatement
from ncl.simpleaction import SimpleAction
from ncl.compoundaction import CompoundAction
from ncl.link import Link
from ncl.bind import Bind
from ncl.area import Area
from ncl.property import Property
from ncl.param import Param
from ncl.connectorparam import ConnectorParam

class Ncl(AbstractElement):

    def __init__(self, id, title=None, xmlns=None):
        listAttributes = ["id", "title", "xmlns"]
        listChildren = [Head, Body]
        super().__init__("ncl", listAttributes, listChildren)
        self.set("id", id)
        if title is not None:
            self.set("title", title)
        if xmlns is not None:
            self.set("xmlns", xmlns)
        self.add(Head())
        self.add(Body())

    def generate(self):
        return super().generate(encoding="iso-8859-1")
    
    pass
