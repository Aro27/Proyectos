# Introducción

A lo largo del siguiente proyecto, veremos el uso de K3s, una distribución ligera y certificada de Kubernetes diseñada para simplificar la instalación, operación y mantenimiento de clústeres Kubernetes, especialmente en entornos con recursos limitados como dispositivos IoT.

Nuestro objetivo es comprender como funcionan tanto en modo single-node como en HA. Además veremos también herramientas complementarias, como por ejemplo K9s para la observación y gestión en tiempo real de los recursos del clúster. 

Hemos dividido la actividad en 3 partes.

**Parte 1: Instalación y despliegue en modo Single-Node**

En esta parte, nuestro propósito es lograr la instalación funcional de un clúster K3s en modo single-node, comprendiendo los pasos básicos de despliegue, configuración y validación de servicios en un entorno sencillo. 

[Instalación y despliegue en modo Single-Node](https://github.com/alvaromespen/pps-10003375/tree/main/template-main/RA5/RA5_4/RA5_4_1)

**Parte 2: Instalación y despliegue en modo High Availability (HA)**

En este ejercicio, nos propusimos configurar un entorno K3s en alta disponibilidad, utilizando múltiples nodos server y el backend de almacenamiento embebido etcd. El objetivo principal es comprender cómo lograr la tolerancia a fallos, el mantenimiento del estado del clúster ante caídas parciales y el comportamiento de los pods en escenarios distribuidos. Además, reforzamos el uso de K9s como herramienta de validación visual y diagnóstico de los componentes del clúster.

[Instalación y despliegue en modo High Availability (HA)](https://github.com/alvaromespen/pps-10003375/tree/main/template-main/RA5/RA5_4/RA5_4_2)

**Parte 3: Despliegue de docker-compose en K3s con validación en K9s**

Nos planteamos como meta traducir un archivo docker-compose.yml tradicional a formatos compatibles con Kubernetes, con el fin de desplegar dichos servicios sobre un clúster K3s. El objetivo es identificar las diferencias entre ambas formas de orquestación y comprobar su interoperabilidad. Posteriormente, validar la correcta ejecución de los recursos mediante K9s, con el fin de verificar que el comportamiento esperado se mantenía en el entorno Kubernetes.

[Despliegue de docker-compose en K3s con validación en K9s](https://github.com/alvaromespen/pps-10003375/tree/main/template-main/RA5/RA5_4/RA5_4_3)
