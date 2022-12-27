FROM python:3.10-slim-buster
WORKDIR /app
CMD mkdir app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app/main.py /app/main.py


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]