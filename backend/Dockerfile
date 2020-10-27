FROM python:3.7.6

RUN apt-get -y update
RUN apt-get -y upgrade

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]