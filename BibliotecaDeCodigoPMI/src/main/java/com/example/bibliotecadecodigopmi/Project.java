package com.example.bibliotecadecodigopmi;

import java.time.LocalDate;
import java.util.Date;
import java.util.List;
public class Project {
    private String nombre;
    private Date FechaDeInicio;
    private Date FechaDeTerminado;
    private String presupuesto;
    private String ManagerDeProyecto;
    private List<Tarea> tareas;
    public Project(String nombre, Date FechaDeInicio, Date FechaDeTerminado, List<Tarea> tareas, String presupuesto, String ManagerDeProyecto) {
        this.nombre = nombre;
        this.FechaDeInicio = FechaDeInicio;
        this.FechaDeTerminado = FechaDeTerminado;
        this.tareas = tareas;
        this.presupuesto = presupuesto;
        this.ManagerDeProyecto = ManagerDeProyecto;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }
    public void setFechaDeInicio(Date FechaDeInicio) {
        this.FechaDeInicio = FechaDeInicio;
    }
    public void setFechaDeTerminado(Date FechaDeTerminado) {
        this.FechaDeTerminado = FechaDeTerminado;
    }
    public Date getFechaDeInicio() {
        return FechaDeInicio;
    }
    
    public Date getFechaDeTerminado() {
        return FechaDeTerminado;
    }
    public void createTarea(String nombre, LocalDate FechaDeInicio, LocalDate FechaDeTerminado, String Descripcion) {
        Tarea tarea = new Tarea(nombre, FechaDeInicio, FechaDeTerminado, Descripcion);
        this.tareas.add(tarea);
    }

    public List<Tarea> getTareas() {
        return tareas;
    }

    public void setTareas(List<Tarea> tareas) {
        this.tareas = tareas;
    }

    public void addTarea(Tarea tarea) {
        this.tareas.add(tarea);
    }

    public void removeTarea(Tarea tarea) {
        this.tareas.remove(tarea);
    }

    public String getPresupuesto() {
        return presupuesto;
    }
    public String getManagerDeProyecto() {
        return ManagerDeProyecto;
    }
    @Override
    public String toString() {
        return nombre;
    }

    public void agregarTarea(Tarea task) {
        this.tareas.add(task);
    }
}
