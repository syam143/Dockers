FROM python:3.7
COPY ./ app1
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","3.7"]
