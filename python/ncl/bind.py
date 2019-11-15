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

class Bind:

    role = None
    component = None
    interface = None

    def __init__(self, role, component, interface=None):
        self.role = role
        self.component = component
        self.interface = interface

    def getElement(self):
        bind = etree.Element("bind")
        bind.set("role", self.role)
        bind.set("component", self.component)
        if self.interface is not None:
            bind.set("interface", self.interface)
        return bind
        

    def generate(self):
        print("Constructor call generate")

    pass
