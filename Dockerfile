FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt --user
RUN apk add --update sqlite && rm -rf /var/cache/apk/*
EXPOSE 5000
#CMD ["sqlite3", "test.db"]
CMD ["python3", "app.py"]
