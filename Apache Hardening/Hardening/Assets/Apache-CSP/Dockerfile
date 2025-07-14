#Imagen de Ubuntu
FROM ubuntu:latest

#Actualizaciones y instalaciones necesarias
RUN apt-get update && apt-get -y install apache2 nano ssl-cert
RUN a2enmod ssl && a2enmod headers

#Copia de los ficheros necesarios
COPY apachesec.html /var/www/html
COPY www.apache.sec.conf /etc/apache2/sites-available/

#Copia de certificados
COPY apache.crt /etc/apache2/ssl/apache.crt
COPY apache.key /etc/apache2/ssl/apache.key

#Configuracion del sitio
COPY www.sslapache.sec.conf /etc/apache2/sites-available/
RUN a2ensite www.sslapache.sec.conf

#Deshabilitar el modulo autoindex
RUN a2dismod -f autoindex

#Habilitar CSP
RUN echo 'Header set Content-Security-Policy "default-src 'self'; img-src *; media-src media1.com media2.com; script-src userscripts.example.com"' >> /etc/apache2/conf-available/security.conf
RUN a2enconf security

#EXPOSE del puerto 80 y 443
EXPOSE 80
EXPOSE 443

#Inicio del servivio Apache en primer plano
CMD ["apachectl", "-D", "FOREGROUND"]
