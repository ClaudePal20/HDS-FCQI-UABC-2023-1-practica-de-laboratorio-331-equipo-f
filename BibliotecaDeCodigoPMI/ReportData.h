#ifndef REPORTDATA_H
#define REPORTDATA_H

namespace com {
	namespace example {
		namespace bibliotecadecodigopmi {
			class ReportData {

			private:
				String projectName;
				java::time::LocalDate startDate;
				java::time::LocalDate endDate;

			public:
				ReportData(String projectName, java::time::LocalDate startDate, java::time::LocalDate endDate);
			};
		}
	}
}

#endif
