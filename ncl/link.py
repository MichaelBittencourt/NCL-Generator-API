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
from ncl.bind import Bind

class Link(AbstractElement):

    def __init__(self, xconnector, id=None):

        listAttributes = ["id", "xconnector"]

        """TODO: create linkParam object and use class param"""
        listChildren = [Bind]
        super().__init__("link", listAttributes, listChildren)

        self.set("xconnector", xconnector)
        if id is not None:
            self.set("id", id)

    pass
