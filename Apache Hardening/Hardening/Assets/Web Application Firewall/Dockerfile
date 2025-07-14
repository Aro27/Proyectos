#Imagen de Ubuntu
FROM pps10003375/apache-pra1

#Actualizaciones y instalaciones necesarias
RUN apt-get install libapache2-mod-security2 curl -y

#Copia de los ficheros necesarios
COPY modsecurity.conf /etc/modsecurity/modsecurity.conf

#Habilitar ModSecurity
RUN a2enmod security2

#EXPOSE del puerto 80 y 443
EXPOSE 80
EXPOSE 443

#Inicio del servivio Apache en primer plano
CMD ["apachectl", "-D", "FOREGROUND"]
