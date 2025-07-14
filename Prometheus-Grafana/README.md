# Introducción

A lo largo del siguiente proyecto veremos cómo implementar un sistema de monitorización completo utilizando las herramientas Prometheus, Node Exporter y Grafana. Nos centraremos en supervisar el estado y el rendimiento de un servidor Ubuntu de manera remota y visual, permitiendo obtener métricas clave del sistema como el uso de CPU, memoria, disco y red. Con ello, buscamos sentar las bases de un entorno básico de observabilidad dentro de una infraestructura de red.

En esta documentación veremos 2 partes:

**Parte 1: Validación del Stack de Monitorización**

En esta primera fase, procedemos a implementar el stack básico siguiendo un repositorio de referencia, y haciendo uso de dockers. 

Validaremos la correcta instalación y configuración de Prometheus y Grafana, incluyendo las métricas iniciales locales y el funcionamiento general del entorno.

[Parte 1: Validación del Stack de Monitorización](https://github.com/Aro27/Proyectos/tree/main/Prometheus-Grafana/Stack%20de%20Validaci%C3%B3n)

**Parte 2: Monitorización de Infraestructura Real**

Aquí llevaremos a cabo la creación de un entorno de monitorización adaptado a una infraestructura compuesta por dos máquinas: un servidor Ubuntu que expone métricas mediante Node Exporter y un cliente Ubuntu que actúa como plataforma de visualización mediante Grafana. Este escenario simula una monitorización real en red.

[Parte 2: Monitorización de Infraestructura Real](https://github.com/Aro27/Proyectos/tree/main/Prometheus-Grafana/Monitorizaci%C3%B3n%20real)
