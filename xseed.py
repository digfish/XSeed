#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# xseed.py
# script em python para guardar uma arvore de directórios num ficheiro XML
# by pescadorDigital, 20/12/05
# versão 0.1

### BIBLIOTECAS ###

from os import listdir
from os.path import isdir,islink
import os
import os.path
import xml.dom.minidom
import sys
from xml.dom.minidom import getDOMImplementation

### CONSTANTES ###

### FUNCOES ###

def visitparse(this_dir,cur_element):
	parent_path,dirname = os.path.split(this_dir)
	new_element = newdoc.createElement("DIR")
	new_element.setAttribute("name",dirname)
	cur_element.appendChild(new_element)
	for f in listdir(this_dir):
		abs_path = os.path.join(this_dir,f)
		if isdir(abs_path) and not islink(abs_path):
			visitparse(abs_path,new_element)

def syntax():
	return sys.argv[0] + " [directory] [xml dir tree]"


### PROGRAMA PRINCIPAL #####
if __name__ == "__main__":
	impl = getDOMImplementation()
	newdoc = impl.createDocument(None,"TREE", None)
	root_element = newdoc.documentElement
	
	if len(sys.argv) < 2:
		_dir = os.getcwd()
	else: 
		if len(sys.argv) == 1:
			print syntax()
		else:
			_dir = sys.argv[1]

	
	# despises the final /
	if _dir[-1] == '/'  : _dir = _dir[:-1]
	if _dir == ".": _dir = os.getcwd()
	(path,dirname) = os.path.split(_dir)
	xmlfilename = "%s_dirtree.xml" % dirname
	print "Writing directory tree in %s !" % xmlfilename
	xmlfile = file(xmlfilename,"w+")
	visitparse(_dir,root_element)
	newdoc.writexml(xmlfile,"","\t","\n")
	
