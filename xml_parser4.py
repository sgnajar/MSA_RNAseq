#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom,parse("C:/Users/Sasan Najar/Desktop/DDX1.xml")

collection = DOMTree.documentElement

if collection.hasAttribute("BlastOutput"):
    print "root element : %s" % collection.getAttribute("BlastOutput")
