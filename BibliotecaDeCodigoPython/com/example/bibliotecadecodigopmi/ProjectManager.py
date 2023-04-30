#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.example.bibliotecadecodigopmi import Project

class ProjectManager(object):
	def exportToXML(self, aProjects):
		"""@ParamType aProjects java.util.List
		@ReturnType void"""
		pass

	def eliminarProjecto(self, aProject):
		"""@ParamType aProject com.example.bibliotecadecodigopmi.Project
		@ReturnType void"""
		pass

	def convertXmlToMpxj(self, aXmlFilePath, aMpxjFilePath):
		"""@ParamType aXmlFilePath String
		@ParamType aMpxjFilePath String
		@ReturnType void"""
		pass

	def exportToMPXJ(self, aProjects, aFilename):
		"""@ParamType aProjects java.util.List
		@ParamType aFilename String
		@ReturnType void"""
		pass

	def getProjectFile(self):
		""""""@ReturnType net.sf.mpxj.ProjectFile"""
		@ReturnType net.sf.mpxj.ProjectFile"""
		return self.___projectFile

	def __init__(self):
		self.___projectFile = None
		"""@AttributeType net.sf.mpxj.ProjectFile"""
		self.___projects = None
		# @AssociationType com.example.bibliotecadecodigopmi.Project*
		# @AssociationMultiplicity *

