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
from ncl.action import Action

class SimpleAction(AbstractElement, Action):

    def __init__(self, role, delay=None, eventType=None, actionType=None, value=None, min=None, max=None, qualifier=None, repeat=None, repeatDelay=None, duration=None, by=None):
        listAttributes = ["role", "delay", "eventType", "actionType", "value", "min", "max", "qualifier", "repeat", "repeatDelay", "duration", "by"]
        super().__init__("simpleAction", listAttributes, [])
        self.set("role", role)
        if delay is not None:
            self.set("delay", delay)
        if eventType is not None:
            self.set("eventType", eventType)
        if actionType is not None:
            self.set("actionType", actionType)
        if value is not None:
            self.set("value", value)
        if min is not None:
            self.set("min", min)
        if max is not None:
            self.set("max", max)
        if qualifier is not None:
            self.set("qualifier", qualifier)
        if repeat is not None:
            self.set("repeat", repeat)
        if repeatDelay is not None:
            self.set("repeatDelay", repeatDelay)
        if duration is not None:
            self.set("duration", duration)
        if by is not None:
            self.set("by", by)

        pass
