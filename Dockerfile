# escape=`

FROM python:3
COPY . /usr/src/wiki
WORKDIR /usr/src/wiki
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

