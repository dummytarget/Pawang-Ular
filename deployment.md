# Deployment


## Requirement- 
1. apache2 (or higher version) : sudo apt install apcahe2
2. sudo ufw app list (to show app that installed)
3. sudo ufw allow 'Apache'
4. sudo service status apache2
5. sudo apt install libapache2-mod-wsgi python-dev
6. go to dir /var/www/ and create your directory app
7. copy your app file and virtualenv into it
8. sudo nano /etc/apache2/sites-available/<your directory>.conf
 
