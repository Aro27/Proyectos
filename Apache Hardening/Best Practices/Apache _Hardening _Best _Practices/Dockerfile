FROM pps10003375/apache-pr4

# Eliminar el banner de versión del servidor (Ya lo hemos hecho, por lo que ponerlo podría generar problemas).
#RUN echo "ServerTokens Prod\nServerSignature Off" >> /etc/apache2/apache2.conf

# Deshabilitar métodos HTTP inseguros
RUN echo '<Directory "/var/www/html">\n    <LimitExcept GET POST>\n        Deny from all\n    </LimitExcept>\n</Directory>' >> /etc/apache2/apache2.conf

#Deshabilitar el listado de directorios
RUN sed -i 's/Options Indexes FollowSymLinks/Options -Indexes +FollowSymLinks/' /etc/apache2/apache2.conf

# Ejecutar Apache con un usuario sin privilegios
RUN groupadd -r apache && useradd -r -g apache apache
RUN chown -R apache:apache /var/www/html
RUN sed -i 's/^User .*/User apache/' /etc/apache2/apache2.conf
RUN sed -i 's/^Group .*/Group apache/' /etc/apache2/apache2.conf

# Proteger la configuración del sistema
RUN sed -i 's/AllowOverride All/AllowOverride None/' /etc/apache2/apache2.conf

# Deshabilitar el rastreo de solicitudes HTTP
RUN echo 'TraceEnable off' >> /etc/apache2/apache.conf

# Inicio del servicio Apache en primer plano
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
