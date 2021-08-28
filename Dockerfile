FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt --user
EXPOSE 5000
CMD ["python3", "app.py"]
