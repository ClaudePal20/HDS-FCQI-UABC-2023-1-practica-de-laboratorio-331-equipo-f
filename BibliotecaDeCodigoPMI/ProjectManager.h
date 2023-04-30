#ifndef PROJECTMANAGER_H
#define PROJECTMANAGER_H

namespace com {
	namespace example {
		namespace bibliotecadecodigopmi {
			class ProjectManager {

			private:
				net::sf::mpxj::ProjectFile projectFile;
				std::vector<com::example::bibliotecadecodigopmi::Project> projects;

			public:
				void exportToXML(java::util::List<com::example::bibliotecadecodigopmi::Project> projects);

				void eliminarProjecto(com::example::bibliotecadecodigopmi::Project project);

				static void convertXmlToMpxj(String xmlFilePath, String mpxjFilePath);

				void exportToMPXJ(java::util::List<com::example::bibliotecadecodigopmi::Project> projects, String filename);
			};
		}
	}
}

#endif
