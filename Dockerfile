FROM python:lastest

WORKDIR /app

COPY requirements.txt ./

RUN apt update
RUN apt upgrade -y

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "./server.py"]
