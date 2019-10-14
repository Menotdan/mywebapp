sudo service apache2 stop
screen -S webserver sudo python3 manage.py runserver 0.0.0.0:80
