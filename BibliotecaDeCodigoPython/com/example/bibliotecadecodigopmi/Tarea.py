#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.example.bibliotecadecodigopmi import Recurso

class Tarea(object):
	def Tarea(self, aNombre, aFechaDeInicio, aFechaDeTerminado, aDescripcion):
		"""@ParamType aNombre String
		@ParamType aFechaDeInicio java.time.LocalDate
		@ParamType aFechaDeTerminado java.time.LocalDate
		@ParamType aDescripcion String"""
		pass

	def setResources(self, aRecurso):
		"""@ParamType aRecurso com.example.bibliotecadecodigopmi.Recurso
		@ReturnType void"""
		pass

	def getResources(self):
		"""@ReturnType java.util.List"""
		pass

	def toString(self):
		"""@ReturnType String"""
		pass

	def setNombre(self, aNombre):
		""""""@ParamType aNombre String"""
		@ParamType aNombre String"""
		self.___nombre = aNombre

	def getNombre(self):
		""""""@ReturnType String"""
		@ReturnType String"""
		return self.___nombre

	def setFechaDeInicio(self, aFechaDeInicio):
		""""""@ParamType aFechaDeInicio java.time.LocalDate"""
		@ParamType aFechaDeInicio java.time.LocalDate"""
		self.___fechaDeInicio = aFechaDeInicio

	def getFechaDeInicio(self):
		""""""@ReturnType java.time.LocalDate"""
		@ReturnType java.time.LocalDate"""
		return self.___fechaDeInicio

	def setFechaDeTerminado(self, aFechaDeTerminado):
		""""""@ParamType aFechaDeTerminado java.time.LocalDate"""
		@ParamType aFechaDeTerminado java.time.LocalDate"""
		self.___fechaDeTerminado = aFechaDeTerminado

	def getFechaDeTerminado(self):
		""""""@ReturnType java.time.LocalDate"""
		@ReturnType java.time.LocalDate"""
		return self.___fechaDeTerminado

	def setDescripcion(self, aDescripcion):
		""""""@ParamType aDescripcion String"""
		@ParamType aDescripcion String"""
		self.___descripcion = aDescripcion

	def getDescripcion(self):
		""""""@ReturnType String"""
		@ReturnType String"""
		return self.___descripcion

	def __init__(self):
		self.___nombre = None
		"""@AttributeType String"""
		self.___fechaDeInicio = None
		"""@AttributeType java.time.LocalDate"""
		self.___fechaDeTerminado = None
		"""@AttributeType java.time.LocalDate"""
		self.___descripcion = None
		"""@AttributeType String"""
		self.___recursos = None
		# @AssociationType com.example.bibliotecadecodigopmi.Recurso*
		# @AssociationMultiplicity *

	Nombre = property(getNombre, setNombre)

	FechaDeInicio = property(getFechaDeInicio, setFechaDeInicio)

	FechaDeTerminado = property(getFechaDeTerminado, setFechaDeTerminado)

	Descripcion = property(getDescripcion, setDescripcion)

