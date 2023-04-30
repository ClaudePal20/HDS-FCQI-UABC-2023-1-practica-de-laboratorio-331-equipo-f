#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.example.bibliotecadecodigopmi import Tarea

class Project(object):
	def Project(self, aNombre, aFechaDeInicio, aFechaDeTerminado, aTareas, aPresupuesto, aManagerDeProyecto):
		"""@ParamType aNombre String
		@ParamType aFechaDeInicio java.util.Date
		@ParamType aFechaDeTerminado java.util.Date
		@ParamType aTareas java.util.List
		@ParamType aPresupuesto String
		@ParamType aManagerDeProyecto String"""
		pass

	def createTarea(self, aNombre, aFechaDeInicio, aFechaDeTerminado, aDescripcion):
		"""@ParamType aNombre String
		@ParamType aFechaDeInicio java.time.LocalDate
		@ParamType aFechaDeTerminado java.time.LocalDate
		@ParamType aDescripcion String
		@ReturnType void"""
		pass

	def addTarea(self, aTarea):
		"""@ParamType aTarea com.example.bibliotecadecodigopmi.Tarea
		@ReturnType void"""
		pass

	def removeTarea(self, aTarea):
		"""@ParamType aTarea com.example.bibliotecadecodigopmi.Tarea
		@ReturnType void"""
		pass

	def toString(self):
		"""@ReturnType String"""
		pass

	def agregarTarea(self, aTask):
		"""@ParamType aTask com.example.bibliotecadecodigopmi.Tarea
		@ReturnType void"""
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
		""""""@ParamType aFechaDeInicio java.util.Date"""
		@ParamType aFechaDeInicio java.util.Date"""
		self.___fechaDeInicio = aFechaDeInicio

	def getFechaDeInicio(self):
		""""""@ReturnType java.util.Date"""
		@ReturnType java.util.Date"""
		return self.___fechaDeInicio

	def setFechaDeTerminado(self, aFechaDeTerminado):
		""""""@ParamType aFechaDeTerminado java.util.Date"""
		@ParamType aFechaDeTerminado java.util.Date"""
		self.___fechaDeTerminado = aFechaDeTerminado

	def getFechaDeTerminado(self):
		""""""@ReturnType java.util.Date"""
		@ReturnType java.util.Date"""
		return self.___fechaDeTerminado

	def getPresupuesto(self):
		""""""@ReturnType String"""
		@ReturnType String"""
		return self.___presupuesto

	def getManagerDeProyecto(self):
		""""""@ReturnType String"""
		@ReturnType String"""
		return self.___managerDeProyecto

	def setTareas(self, *aTareas):
		""""""@ParamType aTareas com.example.bibliotecadecodigopmi.Tarea*"""
		@ParamType aTareas com.example.bibliotecadecodigopmi.Tarea*"""
		self.___tareas = aTareas

	def getTareas(self):
		""""""@ReturnType com.example.bibliotecadecodigopmi.Tarea*"""
		@ReturnType com.example.bibliotecadecodigopmi.Tarea*"""
		return self.___tareas

	def __init__(self):
		self.___nombre = None
		"""@AttributeType String"""
		self.___fechaDeInicio = None
		"""@AttributeType java.util.Date"""
		self.___fechaDeTerminado = None
		"""@AttributeType java.util.Date"""
		self.___presupuesto = None
		"""@AttributeType String"""
		self.___managerDeProyecto = None
		"""@AttributeType String"""
		self.___tareas = None
		# @AssociationType com.example.bibliotecadecodigopmi.Tarea*
		# @AssociationMultiplicity *

	nombre = property(getNombre, setNombre)

	FechaDeInicio = property(getFechaDeInicio, setFechaDeInicio)

	FechaDeTerminado = property(getFechaDeTerminado, setFechaDeTerminado)

	tareas = property(getTareas, setTareas)

