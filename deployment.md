# Deployment


## Requirement- 
1. apache2 (or higher version) : 
   - sudo apt install apcahe2
   
2. to show app that installed
   - sudo ufw app list
3. sudo ufw allow 'Apache'
4. sudo service status apache2

5. sudo apt install libapache2-mod-wsgi python-dev
6. go to dir /var/www/ and create your directory app
7. copy your app file and virtualenv into it
8. sudo nano /etc/apache2/sites-available/<your directory>.conf
9. .conf file script
```
 <VirtualHost *:80>
		ServerName ip
		ServerAdmin email@mywebsite.com
		WSGIScriptAlias / /var/www/webapp.wsgi
		<Directory /var/www/webApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/webApp/static
		<Directory /var/www/webApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
