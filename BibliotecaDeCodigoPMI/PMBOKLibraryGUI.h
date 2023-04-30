#ifndef PMBOKLIBRARYGUI_H
#define PMBOKLIBRARYGUI_H

namespace com {
	namespace example {
		namespace bibliotecadecodigopmi {
			class PMBOKLibraryGUI : javafx::application::Application {

			private:
				javafx::scene::layout::VBox projectDetailsLayout;
				javafx::collections::ObservableList<com::example::bibliotecadecodigopmi::Project> observableProjects;
				std::vector<com::example::bibliotecadecodigopmi::Project> projects;
				com::example::bibliotecadecodigopmi::ProjectManager projectManager;

			public:
				static void main(String args[]);

				void start(javafx::stage::Stage primaryStage);

			private:
				void mostrarDetallesProjectos(javafx::stage::Stage primaryStage, com::example::bibliotecadecodigopmi::Project project);

				void agregarProyectoCuadro();

				com::example::bibliotecadecodigopmi::Tarea mostrarCuadroAgregarTarea();

				void mostrarPanelEditarTarea(com::example::bibliotecadecodigopmi::Tarea tareaSeleccionada, javafx::stage::Stage primaryStage);
			};
		}
	}
}

#endif
