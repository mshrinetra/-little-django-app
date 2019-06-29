# little-django-app
A small django app, following the instruction official django documentation.

---

### Instructions for deployment

#### Accessing remote Linux server

##### Loging through SSH
    ssh USER_NAME@REMOTE_SERVER_URL -> Enter -> Enter password -> Enter Yes

OR

	ssh USER_NMAE@REMOTE_SERVER_IP -> Enter -> Enter password -> Enter Yes

Avoid using root account, creat a new account and make it member of sudo group

    adduser NEW_USERNAME
    adduser NEW_USERNAME sudo

##### Enabling key based login

###### On remote server

    mkdir -p ~/.ssh

###### On local computer

    ssh-keygen -b 4096

Give in input for all the query, then a private-public key pair will be created in .ssh folder on local computer.

Copy the public key from in local .ssh to remote .ssh

    scp ~/.ssh/id_rsa.pub USER_NAME@REMOTE_SERVER:~/.ssh/authrized_key

###### On remote server

    sudo chmod 700 ~/.ssh
    sudo chmod 600 ~/.ssh/*

#### Deployment
##### REMOTE_SERVER Preperation
###### Run following commands

	sudo apt update
	sudo apt upgrade
	sudo hostnamectl set-hostname DESIRED_HOST_NAME_OF_THE_SERVER

###### Edit hosts file

    sudo nano /etc/hosts

Add IP and SITE_HOST_NAME
Save and Exit

###### Install UncomplicatedFireWall, and configure

    sudo apt install ufw
    sudo ufw default allow outgoing
    sudo ufw default deny incoming
    sudo ufw allow ssh
    sudo ufw allow http
    sudo ufw allow https
    sudo ufw enable

##### Uploading site to the server
###### Using git
On remote server

    git clone https://github.com/mshrinetra/little-django-app.git

###### Using SCP
On local computer

    scp -r PATH_TO_PROJECT USER_NAME@REMOTE_SERVER:~/

##### Prepare the site
On remote server

    sudo apt install python3-pip -y
    sudo apt install python3-venv -y
    python3 -m venv PATH_TO_PROJECT/venv
    cd PATH_TO_PROJECT
    source venv/bin/activate
    pip install -r requirements.txt
    cd src
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic

##### Preparing WebServer
###### Install apache
    sudo apt install apache2 -y
    sudo apt install libapache2-mod-wsgi-py3 -y
    sudo systemctl stop apache2

###### Configure apach
conf file location: /etc/apache2/sites-available/

    sudo cd /etc/apache2/sites-available/
    sudo cp 000-default.conf littledjangoapp.conf
    sudo nano littledjangoapp.conf

In the opened file, under <VirtualHost> section, change the value of DocumentRoot to site's root like 

    DocumentRoot /PATH/TO/ROOT_DIR

And add following within the section at the end
    
    Alias /robots.txt /PATH/TO/ROOT_DIR/static/robots.txt
    Alias /favicon.ico /PATH/TO/ROOT_DIR/static/favicon.ico

    Alias /static/ /PATH/TO/ROOT_DIR/static/
    <Directory /PATH/TO/ROOT_DIR/static>
        Require all granted
    </Directory>

    Alias /media/ /PATH/TO/ROOT_DIR/media/
    <Directory /PATH/TO/ROOT_DIR/media>
        Require all granted
    </Directory>

    WSGIScriptAlias / /PATH/TO/ROOT_DIR/mylittleapp/wsgi.py
    <Directory /PATH/TO/ROOT_DIR/mylittleapp>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess mylittleapp.fun python-home=/PATH/TO/venv python-path=/PATH/TO/ROOT_DIR
    WSGIProcessGroup mylittleapp.fun

Save the chenges to file

Continue with following commands

    cd ~
    sudo a2dissite 000-default.conf
    sudo chown -R :www-data mini-django/
    sudo chmod -R 775 mini-django/
    sudo systemctl start apache2

Now try to access the site