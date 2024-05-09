# reservas

Pasos para ejecutar el proyecto Reservas

1) XAMPP phpmyadmin crear una base de datos llamada reservas
2) instalar Python 
3) abrir el proyecto e instalar las siguientes librerías
	pip install django 
	pip install mysqlclient
	pip install openpyxl 
4) ya teniendo esto creamos las migraciones para que se creen la tabla reservar y la tabla login con este comando
	python manage.py migrate
5) Ejecutar el proyecto 
	python manage.py runserver