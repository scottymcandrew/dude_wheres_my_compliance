FROM python:3.9.6

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 443

CMD [ "python3", "./app.py"]