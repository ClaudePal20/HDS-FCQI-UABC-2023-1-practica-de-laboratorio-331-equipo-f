#!/usr/bin/python
# -*- coding: UTF-8 -*-
from com.example.bibliotecadecodigopmi import Project
from com.example.bibliotecadecodigopmi import ProjectManager
from com.example.bibliotecadecodigopmi import Tarea

class PMBOKLibraryGUI(object):
	def main(self, *aArgs):
		"""@ParamType aArgs String*
		@ReturnType void"""
		pass

	def start(self, aPrimaryStage):
		"""@ParamType aPrimaryStage javafx.stage.Stage
		@ReturnType void"""
		pass

	def __mostrarDetallesProjectos(self, aPrimaryStage, aProject):
		"""@ParamType aPrimaryStage javafx.stage.Stage
		@ParamType aProject com.example.bibliotecadecodigopmi.Project
		@ReturnType void"""
		pass

	def __agregarProyectoCuadro(self):
		"""@ReturnType void"""
		pass

	def __mostrarCuadroAgregarTarea(self):
		"""@ReturnType com.example.bibliotecadecodigopmi.Tarea"""
		pass

	def __mostrarPanelEditarTarea(self, aTareaSeleccionada, aPrimaryStage):
		"""@ParamType aTareaSeleccionada com.example.bibliotecadecodigopmi.Tarea
		@ParamType aPrimaryStage javafx.stage.Stage
		@ReturnType void"""
		pass

	def __init__(self):
		self.___projectDetailsLayout = None
		"""@AttributeType javafx.scene.layout.VBox"""
		self.___observableProjects = None
		"""@AttributeType javafx.collections.ObservableList"""
		self.___projects = new ArrayList<>()
		# @AssociationType com.example.bibliotecadecodigopmi.Project*
		# @AssociationMultiplicity *
		self.___projectManager = None
		# @AssociationType com.example.bibliotecadecodigopmi.ProjectManager

