# Introducción

A lo largo de la siguiente parte de la práctica veremos cómo desplegar una aplicación en K3s a partir de un archivo docker-compose, adaptando los servicios definidos en él al entorno de Kubernetes. Este enfoque permite reutilizar configuraciones existentes, facilitando el paso de entornos de desarrollo locales a infraestructuras orquestadas. Validaremos el despliegue utilizando K9s, lo que nos proporcionará una visión clara y dinámica del estado de los recursos, facilitando la detección de posibles errores y la comprobación de que los servicios se han desplegado correctamente.

# Despliegue de docker-compose en K3s con validación en K9s

En este caso, lo que hemos tenido que realizar es crear un docker-compose.yml básico que cree dos réplicas del servicio nginx.

![I12](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/12.PNG)

Una vez con el docker-compose creado, podemos hacer uso de kompose convert para convertir el archivo docker-compose.yml en archivos de manifiesto de Kubernetes, y genera los archivos YAML equivalentes para Kubernetes. De esta manera conseguimos migrar fácilmente aplicaciones definidas con Docker Compose a Kubernetes, facilitando así la transición entre entornos de contenedores.

![I13](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/13.PNG)

Tras esto, con estos dos ficheros, lo que tenemos que hacer es aplicarlos de la siguiente manera, y así podemos verificar que se haya creado a la perfección:

![I14](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/14.PNG)

![I14-15](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/14-15.PNG)

Como podemos ver se ha creado a la perfección, y si accedemos a K9s, vemos que se han creado a la perfección también y podemos visualizarlo.

![I15](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/15.PNG)
