package com.example.bibliotecadecodigopmi;

import net.sf.mpxj.ProjectFile;
import net.sf.mpxj.mpx.MPXWriter;
import net.sf.mpxj.reader.ProjectReader;
import net.sf.mpxj.reader.ProjectReaderUtility;
import net.sf.mpxj.writer.ProjectWriter;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;
import java.util.Date;
import java.util.List;

public class ProjectManager {
    private List<Project> projects;
    private ProjectFile projectFile;
    public void exportToXML(List<Project> projects) throws ParserConfigurationException, TransformerException {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document document = builder.newDocument();
        Element rootElement = document.createElement("projects");
        document.appendChild(rootElement);
        for (Project project : projects) {
            Element projectElement = document.createElement("project");
            rootElement.appendChild(projectElement);

            Element nameElement = document.createElement("name");
            nameElement.setTextContent(project.getNombre());
            projectElement.appendChild(nameElement);

            Element startDateElement = document.createElement("startDate");
            startDateElement.setTextContent(project.getFechaDeInicio().toString());
            projectElement.appendChild(startDateElement);

            Element endDateElement = document.createElement("endDate");
            endDateElement.setTextContent(project.getFechaDeTerminado().toString());
            projectElement.appendChild(endDateElement);

            Element budgetElement = document.createElement("budget");
            budgetElement.setTextContent(project.getPresupuesto());
            projectElement.appendChild(budgetElement);

            Element managerElement = document.createElement("manager");
            managerElement.setTextContent(project.getManagerDeProyecto());
            projectElement.appendChild(managerElement);

            Element tasksElement = document.createElement("tasks");
            projectElement.appendChild(tasksElement);

            for (Tarea task : project.getTareas()) {
                Element taskElement = document.createElement("task");
                tasksElement.appendChild(taskElement);

                Element taskNameElement = document.createElement("name");
                taskNameElement.setTextContent(task.getNombre());
                taskElement.appendChild(taskNameElement);

                Element taskStartDateElement = document.createElement("startDate");
                taskStartDateElement.setTextContent(task.getFechaDeInicio().toString());
                taskElement.appendChild(taskStartDateElement);

                Element taskEndDateElement = document.createElement("endDate");
                taskEndDateElement.setTextContent(task.getFechaDeTerminado().toString());
                taskElement.appendChild(taskEndDateElement);
            }
        }

        // Write the DOM document to the file
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        DOMSource domSource = new DOMSource(document);
        StreamResult streamResult = new StreamResult(new File("projects.xml"));

        transformer.transform(domSource, streamResult);
    }
    public void eliminarProjecto(Project project) {
        this.projects.remove(project);
    }
    public static void convertXmlToMpxj(String xmlFilePath, String mpxjFilePath) {
        try {
            // Add file extension if necessary
            if (!xmlFilePath.endsWith(".xml")) {
                xmlFilePath += ".xml";
            }
            // Read the XML file
            File xmlFile = new File(xmlFilePath);
            ProjectReader reader = ProjectReaderUtility.getProjectReader(xmlFile.getName());
            ProjectFile project = reader.read(xmlFile);
            // Write the MPXJ file
            File mpxjFile = new File(mpxjFilePath);
            ProjectWriter writer = new MPXWriter();
            writer.write(project, mpxjFile);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    // Read an MPXJ file and add the projects to the list
    //public void importFromMPXJ(String filename) {
    //        try {
    //            File file = new File(filename);
    //            ProjectReader reader = new UniversalProjectReader();
    //            ProjectFile projectFile = reader.read(file);
    //            if (projectFile != null) {
    //                List<net.sf.mpxj.Task> tasks = projectFile.getChildTasks();
    //                for (net.sf.mpxj.Task task : tasks) {
    //                    String name = task.getName();
    //                    Date startDate = task.getStart();
    //                    Date endDate = task.getFinish();
    //                    List<net.sf.mpxj.Task> childTasks = task.getChildTasks();
    //                    ArrayList<Tarea> tareas = new ArrayList<>();
    //                    for (net.sf.mpxj.Task childTask : childTasks) {
    //                        String tareaName = childTask.getName();
    //                        Date tareaStartDate = childTask.getStart();
    //                        Date tareaEndDate = childTask.getFinish();
    //                        LocalDate fechaInicio = tareaStartDate.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
    //                        LocalDate fechaFinal = tareaEndDate.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
    //                        String descripcion = childTask.getNotes();
    //                        Tarea tarea = new Tarea(tareaName, fechaInicio, fechaFinal, descripcion);
    //                        tareas.add(tarea);
    //                    }
    //                    String presupuesto = task.getCost().toString();
    //                    String manager = task.getResourceNames();
    //                    Project project = new Project(name, startDate, endDate, tareas, presupuesto, manager);
    //                    projects.add(project);
    //                }
    //            } else {
    //                System.out.println("Error: projectFile is null");
    //            }
    //
    //        } catch (Exception ex) {
    //            System.out.println("Error reading MPXJ file: " + ex.getMessage());
    //        }
    //    }
    public ProjectFile getProjectFile() {
        if(projectFile== null) {
            projectFile = new ProjectFile();
        }
        return projectFile;
    }
    public void exportToMPXJ(List<Project> projects, String filename) {
        try {
            ProjectFile projectFile = getProjectFile();

            for (Project project : projects) {
                net.sf.mpxj.Task parentTask = projectFile.addTask();
                parentTask.setName(project.getNombre());
                parentTask.setStart(project.getFechaDeInicio());
                parentTask.setFinish(project.getFechaDeTerminado());
                parentTask.setCost(Double.parseDouble(project.getPresupuesto()));
                parentTask.setResourceNames(project.getManagerDeProyecto());

                for (Tarea task : project.getTareas()) {
                    net.sf.mpxj.Task childTask = parentTask.addTask();
                    childTask.setName(task.getNombre());
                    Date tareaStartDate = childTask.getStart();
                    Date tareaEndDate = childTask.getFinish();
                    childTask.setStart(tareaStartDate);
                    childTask.setFinish(tareaEndDate);
                    childTask.setNotes(task.getDescripcion());
                }
            }

            MPXWriter writer = new MPXWriter();
            writer.write(projectFile, filename);
        } catch (Exception ex) {
            System.out.println("Error exporting MPXJ file: " + ex.getMessage());
        }
    }


}
