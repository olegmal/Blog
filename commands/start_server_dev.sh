#!/bin/bash
 sh -c "python manage.py wait_for_db &&
        python src/manage.py migrate &&
        python src/manage.py runserver 0.0.0.0:8000"