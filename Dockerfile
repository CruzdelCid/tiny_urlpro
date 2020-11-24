FROM python:3.8

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /app/

COPY . ./

EXPOSE 5000:5000

CMD ["python", "app.py"]