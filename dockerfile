from python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
copy . /usr/src/app
workdir /usr/src/app
run pip install -r requirements.txt
cmd ["python","manage.py","runserver","0.0.0.0:8000"]