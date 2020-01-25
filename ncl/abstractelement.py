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
from abc import ABC, abstractmethod
from collections import OrderedDict


class AbstractElement(ABC):

    @abstractmethod
    def __init__(self, name, listAttributes, listChildren):
        self._name = name
        self._setListAttributes(listAttributes)
        self._setListChildren(listChildren)

    def _setTagName(self, tagName):
        self._name = tagName

    def _appendAttributes(self, listAttributes):
        for attribute in listAttributes:
            assert (isinstance(attribute, str)), "Each Param need be a string attribute!" 
            self.__listAttributes[attribute] = None

    def _appendChildren(self, listChildren):
        for child in listChildren:
            # TODO Try check if is possible create a interface seems to Java to implemente the interface GetterElementIF
            # assert (issubclass(child, AbstractElement)), "each list element need be inherit from AbstractElement!" 
            assert (isinstance(child, type)), "Each child need be a class prefered inherit from AbstractElement!" 
            self.__listChildren[child] = []

    def _getListAttributes(self):
        return self.__listAttributes

    def _setListAttributes(self, listAttributes):
        assert (isinstance(listAttributes, list)), "The param \"listAttributes\" need be a list of strings!" 
        self.__listAttributes = OrderedDict()
        self._appendAttributes(listAttributes)

    def _getListChildren(self):
        return self.__listChildren

    def _setListChildren(self, listChildren):
        assert (isinstance(listChildren, list)), "The param \"listChildren\" need be a list of NCL Element Classes(inherit from AbstractElement)!" 
        self.__listChildren = OrderedDict()
        self._appendChildren(listChildren)

    def add(self, nclComponent):
        for item in self.__listChildren:
            if isinstance(nclComponent, item):
                self.__listChildren[item].append(nclComponent)
                return True;
        else:
            """
            I can use this to convert OrderedDict in list
            tempChildrenList = [(k, v) for k, v in self.__listChildren.items()][::-1]
            for key in tempChildrenList:
            """
            couldAddElement = False;
            for key in self.__listChildren:
                if self.__listChildren[key] is not None:
                    for item in self.__listChildren[key][::-1]: #I use a reverse list to insert new element in the more recently object
                        couldAddElement = item.add(nclComponent)
                        if couldAddElement:
                            break;
                if couldAddElement:
                    break;
            return couldAddElement;
        return False

    def set(self, attribute, value):
        if attribute in self.__listAttributes:
            self.__listAttributes[attribute] = value;

    def get(self, attribute):
        if attribute in self.__listAttributes:
            return self.__listAttributes[attribute];
        return None

    def getElement(self):
        element = etree.Element(self._name)
        for key in self.__listAttributes:
            if self.__listAttributes[key] is not None:
                element.set(key, self.__listAttributes[key])
        for key in self.__listChildren:
            if self.__listChildren[key] is not None:
                for item in self.__listChildren[key]:
                    element.append(self.customizeItem(item).getElement())
        return element

    def customizeItem(self, item):
        return item

    def generate(self, encoding=None):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, encoding=encoding, method="xml", pretty_print=True).decode()

    pass
