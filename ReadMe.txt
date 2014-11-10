 Install DJango and pip
   sudo apt-get install python-pip python-dev python-virtualenv build-essential (virtualenv just could be helpfull)
   sudo pip install Django==1.6.5

Installing mysql
   sudo apt-get install mysql-server-5.6

make django and mysql friends
   sudo apt-get install libmysqlclient-dev
   sudo pip install MySQL-python

Init DB:
	sh scripts/init.sh