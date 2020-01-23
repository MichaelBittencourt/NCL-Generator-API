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

class Bind(AbstractElement):

    def __init__(self, role, component, interface=None, descriptor=None):

        listAttributes = ["role", "component", "interface", "descriptor"]

        """TODO: create bindParam object and use class param"""
        listChildren = []

        super().__init__("bind", listAttributes, listChildren)
        self.set("role", role)
        self.set("component", component)
        if interface is not None:
            self.set("interface", interface)
        if descriptor is not None:
            self.set("descriptor", descriptor)

    pass
