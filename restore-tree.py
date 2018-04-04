#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# recria a árvore de directórios guardada
# by pescadorDigital, 21/12/05
# version 0.2
# recovered 28/07/07

### BIBLIOTECAS ###
from os import makedirs
from xml.dom import minidom
import os.path
import xml.dom
import sys

### CONSTANTES ###

### FUNCOES ###
def walkTree(curDirElement,todir):
	for child in curDirElement.childNodes:
		if child.nodeType == xml.dom.Node.ELEMENT_NODE and child.nodeName == 'DIR':
			newdirname = todir + "/" + child.attributes['name'].value;
			print "Creating " + newdirname
			os.makedirs(newdirname)
			walkTree(child,newdirname)

### PROGRAMA PRINCIPAL #####

if __name__ == "__main__":
	xmldoc = minidom.parse(sys.argv[1])
	if len(sys.argv) < 3: todir = '.'
	else: todir = sys.argv[2]
	rootElem = xmldoc.documentElement
	walkTree(rootElem,todir)
