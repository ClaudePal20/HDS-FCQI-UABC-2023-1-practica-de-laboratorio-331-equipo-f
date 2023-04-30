#!/usr/bin/python
# -*- coding: UTF-8 -*-
class ReportData(object):
	def ReportData(self, aProjectName, aStartDate, aEndDate):
		"""@ParamType aProjectName String
		@ParamType aStartDate java.time.LocalDate
		@ParamType aEndDate java.time.LocalDate"""
		pass

	def setProjectName(self, aProjectName):
		""""""@ParamType aProjectName String"""
		@ParamType aProjectName String"""
		self.___projectName = aProjectName

	def getProjectName(self):
		""""""@ReturnType String"""
		@ReturnType String"""
		return self.___projectName

	def setStartDate(self, aStartDate):
		""""""@ParamType aStartDate java.time.LocalDate"""
		@ParamType aStartDate java.time.LocalDate"""
		self.___startDate = aStartDate

	def getStartDate(self):
		""""""@ReturnType java.time.LocalDate"""
		@ReturnType java.time.LocalDate"""
		return self.___startDate

	def setEndDate(self, aEndDate):
		""""""@ParamType aEndDate java.time.LocalDate"""
		@ParamType aEndDate java.time.LocalDate"""
		self.___endDate = aEndDate

	def getEndDate(self):
		""""""@ReturnType java.time.LocalDate"""
		@ReturnType java.time.LocalDate"""
		return self.___endDate

	def __init__(self):
		self.___projectName = None
		"""@AttributeType String"""
		self.___startDate = None
		"""@AttributeType java.time.LocalDate"""
		self.___endDate = None
		"""@AttributeType java.time.LocalDate"""

	projectName = property(getProjectName, setProjectName)

	startDate = property(getStartDate, setStartDate)

	endDate = property(getEndDate, setEndDate)

