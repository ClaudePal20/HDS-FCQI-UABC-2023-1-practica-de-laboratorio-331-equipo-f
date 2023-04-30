#ifndef TAREA_H
#define TAREA_H

namespace com {
	namespace example {
		namespace bibliotecadecodigopmi {
			class Tarea {

			private:
				String Nombre;
				java::time::LocalDate FechaDeInicio;
				java::time::LocalDate FechaDeTerminado;
				String Descripcion;
				std::vector<com::example::bibliotecadecodigopmi::Recurso> recursos;

			public:
				Tarea(String Nombre, java::time::LocalDate FechaDeInicio, java::time::LocalDate FechaDeTerminado, String Descripcion);

				void setResources(com::example::bibliotecadecodigopmi::Recurso recurso);

				java::util::List<com::example::bibliotecadecodigopmi::Recurso> getResources();

				String toString();
			};
		}
	}
}

#endif
