# Introducción

A lo largo de la siguiente parte veremos cómo instalar y configurar un clúster K3s en modo single-node, una modalidad ideal para entornos de desarrollo local o sistemas con recursos limitados. Este enfoque nos permitirá familiarizarnos con los componentes básicos de Kubernetes de forma simplificada, sentando las bases para entornos más complejos.

Como parte del ejercicio, desplegaremos un servicio nginx con 2 réplicas, lo cual nos servirá para aplicar los conceptos de Deployments, Pods y Services en un entorno real. Además, aprenderemos a verificar el estado del clúster y de los recursos desplegados utilizando comandos de kubectl.

Ademas, añadiremos a este trabajo  la instalación de K9s, una herramienta basada en terminal que facilita la supervisión y gestión de los recursos del clúster. Esta nos proporcionará una interfaz más visual e interactiva para observar en tiempo real la ejecución de los servicios desplegados.

# RA5_4_1: Instalación y despliegue en modo Single-Node

Lo primero que debemos realizar es instalar K3s, para ello, hacemos uso del comando de instalación rápida, una vez instalado, podemos verificar su funcionamiento con ```k3s kubectl get nodes```, y tras comprobar su funcionamiento, exportamos el kubeconfig para poder hacer uso de kubectl directamente, a continuación, veremos los pasos detallados de como realizarlo todo:

![I1](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/1.png)

Una vez hecho eso, procederemos a configurar el .yaml poder desplegar una aplicación NGINX haciendo uso de 2 réplicas.

![I2](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/2.png)

Una vez creado este fichero, lo aplicaremos, y verificaremos su funcionamiendo, viendo los pods creados por ejemplo, o realizando un curl al puerto establecido.

![I3](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/3.png)

(A partir de esta parte, realizamos la configuración de K9s a través de SSH, a eso se debe el cambio de terminal.)****

Ahora que ya están desplegadas las dos réplicas de NGINX, vamos a descargar e instalar K9s, haciendo uso de curl, una vez en nuestro equipo instaldo, tendremos que volver a exportar el KUBECONFIG.

![I4](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/4.PNG)

![I4-5](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/4-5.PNG)

Finalmente, podremos observar que si ejecutamos K9s, interfaz de usuario basada en terminal (TUI) para Kubernetes que te permite interactuar con tu clúster de forma rápida y visual, sin tener que escribir constantemente comandos kubectl.

![I5](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/5.PNG)
