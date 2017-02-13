FROM python:2.7
ADD . /app
WORKDIR /app
ENV http_proxy=http://10.144.1.10:8080
ENV https_proxy=https://10.144.1.10:8080
ENV ftp_proxy=ftp://10.144.1.10:8080
RUN pip install -r requirements.txt
#COPY app.py /code
ENTRYPOINT ["python"]
CMD ["app.py"]
