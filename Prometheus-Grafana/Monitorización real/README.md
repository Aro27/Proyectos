# Parte 2: Monitorización de Infraestructura Real

En esta parte, vamos a realizar una monitorización en una infraestructura con dos VM que se encuentran en la misma red, donde:

- Ubuntu Server tiene instalado Prometheus y node_exporter.
- Ubuntu Cliente tiene instalado Grafana para la monitorización y el dashboard de node_exporter.

# Ubuntu Server

A continuación, vamos a ver lo que ser ha realizado por partes, empezando por el Ubuntu Server:

Lo primero que vamos a hacer es instalar el node_exporter en el servidor, este es un componente de monitorización para Prometheus que se encarga de exportar métricas del sistema operativo (host) en el que se ejecuta.

Haciendo uso de ```wget https://github.com/prometheus/node_exporter/releases/download/v1.8.0/node_exporter-1.8.0.linux-amd64.tar.gz```, obtenemos la herramienta de node_exporter comprimida en tar.gz, y tras eso, añadimos el node exporter a los binarios del usuario, además hemos creado un usuario llamado node_exporter para modificar posteriormente los permisos.

Una vez realizado lo anterior, vamos a añadir los siguientes contenidos al siguiente fichero, para que de esta manera podamos habilitar y correr el servicio de node_exporter:

![I10](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/10.png)

Su función general es garantizar que node_exporter se inicie automáticamente al arrancar el sistema, después de que la red esté disponible, y que se ejecute bajo un usuario no privilegiado por seguridad, ejecutando el binario desde su ubicación correspondiente. 

Tras esto, habilitamos y corremos el servicio y si ejecutamos el curl desde localhost o desde un equipo de la red, vemos que funciona a la perfección.

![I11](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/11.png)
![I12](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/12.png)

# Ubuntu Cliente

Para proceder con este punto tenemos que instalar Prometheus, haciendo el mismo procedimiento que con el Ubuntu Server con node_exporter, donde lo primero que haremos será ejecutar lo siguiente el wget para poder instalar el Prometheus --> ```wget https://github.com/prometheus/prometheus/releases/download/v2.52.0/prometheus-2.52.0.linux-amd64.tar.gz```, también hemos creado el usuario prometheus y hemos aplicado los permisos 600 a los directorios /etc/prometheus/ y /var/lib/prometheus/ y con chown hemos cambiado el usuario propietario.

Tras eso, hemos configurado el fichero .yml de la siguiente manera:

![I15](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/15.png)

Donde hemos configurado el target para que apunte a la .101, que es la IP del servidor.

Y también hemos configurado el prometheus.service, donde hemos añadido las siguientes líneas para poder habilitar el servicio de prometheus. Su función general es iniciar Prometheus automáticamente al arrancar el sistema, una vez que la red esté disponible. Ejecuta el binario de Prometheus como el usuario prometheus, especificando la ruta del archivo de configuración, el directorio de almacenamiento de datos de series temporales y las rutas de las plantillas web para la interfaz gráfica. 

![I16](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/16.png)

Tras esto, ya podemos ver que Prometheus funciona a la perfección.

![I17](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/17.png)

Ahora tenemos que instalar Grafana, que para ello, tenemos que ejecutar lo siguiente para poder añadir el repositorio oficial a nuestro equipo:

```
sudo apt install -y software-properties-common
sudo add-apt-repository "deb https://apt.grafana.com stable main"
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt update
```

Tras eso, instalamos el servicio Grafana, haciendo un apt install grafana, y tras instalarlo, podemos acceder al servicio de Grafana de manera gráfica.

![I19](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/19.png)

Una vez dentro de la interfaz, vamos a ir a la parte de la izquierda al apartado de Data Sources, y le daremos a añadir uno nuevo, para poder añadirlo como fuente de datos, donde en el apartado de URL introduciremos nuestra localhost con el puerto 9090, y tras eso lo guardamos.

![I20](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/20.png)

Finalmente, importamos la dashboard, e introducimos la fuente de datos Prometheus, y finalmente podremos ver el panel completo con las métrcias del servidor siendo moniotrizadas.

![I21](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/21.png)
![I22](https://github.com/alvaromespen/pps-10003375/blob/main/template-main/RA5/RA5_3/Assets%20-%20Prometheus%20%26%20Grafana/22.png)

De esta manera, tenemos el servidor siendo monitorizado haciendo uso de Grafana desde nuestro equipo cliente.
