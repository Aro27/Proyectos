# Introducción

A lo largo de la siguiente parte de la práctica veremos cómo realizar la instalación, configuración y validación de un clúster K3s en modo HA (High Availability). Este tipo de arquitectura permite garantizar la disponibilidad del plano de control mediante la distribución del mismo entre varios nodos. 

Implementaremos un servicio nginx con 2 réplicas con HA, lo que nos permitirá comprobar tanto la correcta distribución de la carga como la tolerancia a fallos dentro del clúster. Además, utilizaremos K9s para supervisar el estado de los recursos y facilitar la gestión visual en tiempo real del entorno Kubernetes.

# Parte 2: Instalación y despliegue en modo High Availability (HA)

En este caso, lo primero que vamos a realizar es crear el nodo principal del clúster en modo HA con K3s, y esto lo hacemos gracias a través del siguiente comando:

![I6](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/6.PNG)

Este comando lo que hace es configurar el nodo actual como primer nodo servidor, como control plane en un cluster en modo HA, además inicia el clúster sin la necesidad de hacer uso de una base de datos externa.

A continuación, para configurar los siguientes nodos en las otras dos VM para conseguir la HA, necesitamos el token, que lo vemos de la siguiente manera:

![I7](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/7.PNG)

Una vez con el token, accedemos a las otras VMs, y ejecutamos lo siguiente, para instalar K3s, y especificamos el servidor a través de la IP, como además, a través del tokén.

![I8](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/8.PNG)

![I9](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/9.PNG)

A continuación, para verificar su buen funcionamiento podemos hacer uso del comando ```k3s kubectl get nodes```, de esta manera, obtenemos el resultado de todos los nodos del clúster registrados, y vemos en NAME, el nombre de cada VM en las que se encuentran los nodos Readys.

![I10](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/10.PNG)

Lo siguiente que tenemos que hacer, es visualizarlo a través de K9s, no obstante, nos generaba un error de permisos, y tras investigar, la solución a este problema era crearun directorio oculto en nuestro directorio personal, y añadir el k3s.yaml, modificar los permisos y exportar la KUBECONFIG a ese directorio también, y tras realizar eso, ya podemos ver los nodos a través de K9s.

![I10-11](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/10-11.PNG)

![I11](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_4/Assets/11.PNG)
