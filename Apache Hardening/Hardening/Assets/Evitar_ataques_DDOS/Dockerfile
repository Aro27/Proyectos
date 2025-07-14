FROM pps10003375/apach-pr3

# Evita la configuración interactiva de paquetes
ARG DEBIAN_FRONTEND=noninteractive

# Preconfigurar Postfix para que no solicite entrada del usuario
RUN echo "postfix postfix/main_mailer_type select No configuration" | debconf-set-selections

# Instalar paquetes sin interacción
RUN apt update && apt install -y postfix

#Instalar mod-evasive
RUN apt install libapache2-mod-evasive -y && a2enmod evasive

# Configuración de mod_evasive
COPY evasive.conf /etc/apache2/mods-available/evasive.conf

# Crear directorio de logs para mod_evasive
RUN mkdir -p /var/log/mod_evasive && chmod 755 /var/log/mod_evasive

# Prohibir uso de .htaccess
RUN sed -i 's/AllowOverride All/AllowOverride None/' /etc/apache2/apache2.conf

# Inicio del servicio Apache en primer plano
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
