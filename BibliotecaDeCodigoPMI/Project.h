#ifndef PROJECT_H
#define PROJECT_H

namespace com {
	namespace example {
		namespace bibliotecadecodigopmi {
			class Project {

			private:
				String nombre;
				java::util::Date FechaDeInicio;
				java::util::Date FechaDeTerminado;
				String presupuesto;
				String ManagerDeProyecto;
				std::vector<com::example::bibliotecadecodigopmi::Tarea> tareas;

			public:
				Project(String nombre, java::util::Date FechaDeInicio, java::util::Date FechaDeTerminado, java::util::List<com::example::bibliotecadecodigopmi::Tarea> tareas, String presupuesto, String ManagerDeProyecto);

				void createTarea(String nombre, java::time::LocalDate FechaDeInicio, java::time::LocalDate FechaDeTerminado, String Descripcion);

				void addTarea(com::example::bibliotecadecodigopmi::Tarea tarea);

				void removeTarea(com::example::bibliotecadecodigopmi::Tarea tarea);

				String toString();

				void agregarTarea(com::example::bibliotecadecodigopmi::Tarea task);
			};
		}
	}
}

#endif
