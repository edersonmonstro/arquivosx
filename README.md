# arquivosx

## instalar e usar venvs
https://www.javatpoint.com/django-virtual-environment-setup

## banco de dados
usar o postgres no docker-composer


## superuser
admin/admin

## development layers
create new app - make folder by hand first inside apps and run:
django-admin startapp cases apps/cases

layers to develop:
models
views
forms
urls
templates in templates folder
migrations to create/populate db

## links uteis
### na hora de montar o update view
https://www.w3schools.com/django/django_update_record.php

## put imagens with django
 <div class="alert alert-success" role="alert">
            <h2></h2>{% load static %} <img src="{% static "img/fbi_logo.png" %}" alt="home" width="80px" height="80px" /> X-Files Cases List</h2>
            
        </div>
