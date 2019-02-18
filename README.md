## Virtustream test

This is a minimal Flask app with Fibonacci numbers API functionality.
For demo purposes please see [here](http://46.101.202.234:8000)

## Setup on a mac or some other unix based machine

Clone this repo

`git clone https://github.com/daugela/virtustream-test.git`

Go inside

`cd virtustream-test`

Download prerequisites and prepare Python environment

`wget https://bootstrap.pypa.io/get-pip.py`  
`sudo python3 get-pip.py`  
`sudo pip3 install virtualenv`  

Create virtual environment directory (djenv)
`virtualenv -p python3 djenv`

Activate environment
`source djenv/bin/activate`

Install dependencies
`pip install -r requirements.txt`

Test installation with Flasks built in development server.

`FLASK_APP=pythoncode.py flask run --host=0.0.0.0`

This will start accepting requests under http://yourhostname-or-ip:5000 (5000 port)

## Deploy to production under apache

Install apache and other dependencies    
Be sure to deploy wsgi module to run python apps (I was running Python3)  

`sudo apt-get install apache2`  
`sudo apt-get install python-setuptools`  
`sudo apt-get install libapache2-mod-wsgi-py3`  

Use below apache configuration

```
#Listen for specific port if necessary
Listen 8000
<VirtualHost *:8000>
	
	#Change your email
	ServerAdmin andrius.daugela@gmail.com

	# Configure your hostname
	ServerName 46.101.202.234

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
	WSGIDaemonProcess virtusapp user=www-data group=www-data threads=5
	WSGIProcessGroup virtusapp

	#
	# Adjust directories below according to your environment
	#

	WSGIScriptAlias / /home/andrius/www-virtustream/wrapper.wsgi

	<Directory /home/andrius/www-virtustream>
		Require all granted
	</Directory>

	<Directory /home/andrius/www-virtustream/>
		Order allow,deny
		Allow from all
	</Directory>

	<Files wrapper.wsgi>     
		Order allow,deny
		Allow from all
	</Files>

</VirtualHost>
```