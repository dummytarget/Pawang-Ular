# Deployment


## Requirement- 
1. apache2 (or higher version) : 
   - sudo apt install apcahe2
   
2. to show app that installed
   - sudo ufw app list
3. sudo ufw allow 'Apache'
4. sudo service status apache2

5. sudo apt install libapache2-mod-wsgi python-dev
6. go to dir /var/www/ and create your directory app (ex. `/var/www/microweb)
7. copy your app file and virtualenv into it
8. sudo nano /etc/apache2/sites-available/<< (your app name) >>.conf
9. .conf file script
```
 <VirtualHost *:80>
		ServerName <ip address>
		ServerAdmin email@mywebsite.com
		WSGIScriptAlias / /var/www/<<your app name>>.wsgi
		<Directory /var/www/<<your app name>>/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/<<your app name>>/static
		<Directory /var/www/<<your app name>>/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
10. activate the site and reload apache
	 - sudo a2ensite << (your app name) >>
	 - service reload apache2

11. config wsgi file
	- /<< (your app name) >># sudo nano << (your app name) >>.wsgi
	- 
	```
	#!/usr/bin/python
	import sys
	import logging
	logging.basicConfig(stream=sys.stderr)
	sys.path.insert(0,"/var/www/<<your app name>>/")
	
	from webApp import <app> as application
	# app is variable name
	application.secret_key = '<<Add your secret key>>'
	  ```
	
12. restart server :
	- sudo service apache2 restart
	
13. run your ip address on your browser!
