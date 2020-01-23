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

class Port(AbstractElement):

    def __init__(self, id, component, interface=None):
        listAttributes = ["id", "component", "interface"]
        super().__init__("port", listAttributes, [])
        self.set("id", id)
        self.set("component", component)
        if interface is not None:
            self.set("interface", interface)

    pass

