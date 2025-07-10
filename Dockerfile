FROM python:3-alpine
WORKDIR /code

RUN mkdir templates

COPY requirements.txt requirements.txt
COPY templates/* templates/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python /code/app.py

