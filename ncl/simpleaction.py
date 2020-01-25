#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.simple import Simple
from ncl.action import Action

class SimpleAction(Simple, Action):

    def __init__(self, role, delay=None, eventType=None, actionType=None, value=None, min=None, max=None, qualifier=None, repeat=None, repeatDelay=None, duration=None, by=None):
        super().__init__(role, eventType, delay, min, max, qualifier)
        listAttributes = ["actionType", "value", "repeat", "repeatDelay", "duration", "by"]
        self._setTagName("simpleAction")
        self._appendAttributes(listAttributes)
        if actionType is not None:
            self.set("actionType", actionType)
        if value is not None:
            self.set("value", value)
        if repeat is not None:
            self.set("repeat", repeat)
        if repeatDelay is not None:
            self.set("repeatDelay", repeatDelay)
        if duration is not None:
            self.set("duration", duration)
        if by is not None:
            self.set("by", by)

        pass
