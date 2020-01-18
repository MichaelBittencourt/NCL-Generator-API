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
from ncl.port import Port
from ncl.property import Property
from ncl.media import Media
from ncl.link import Link

class Body(AbstractElement):

    def __init__(self, id=None):
        listAttributes = ["id"]
        """
        TODO: Still needs add Context, Switch, Meta, Metadata
        [OBS] The body can be a special Context
        """
        listChildren = [Port, Property, Media, Link]
        super().__init__("body", listAttributes, listChildren)
        if id is not None:
            self.set("id", id)

    pass

