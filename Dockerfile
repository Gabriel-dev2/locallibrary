FROM python:3.10.6

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/app/src/

COPY Pipfile ./
COPY /catalog ./catalog
COPY /locallibrary ./locallibrary
COPY db.sqlite3 ./
COPY manage.py ./
COPY install.sh ./

RUN chmod +x ./install.sh

RUN ./install.sh

EXPOSE 8000

CMD ["pipenv", "run", "python", "./manage.py", "runserver", "0.0.0.0:8000"]