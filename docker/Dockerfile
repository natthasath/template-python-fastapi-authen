FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./.env /code/.env
COPY ./main.py /code/main.py
COPY ./app /code/app

COPY ./certs/certificate.crt /etc/ssl/certs/
COPY ./certs/private.key /etc/ssl/private/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "main.py"]
