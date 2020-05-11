FROM alpine:3.8
RUN apk add python3 py-pip && python3 -m ensurepip && pip3 install --upgrade pip && pip3 install flask boto3
COPY arp-honeypot.py /app/
WORKDIR /app
EXPOSE 8080
CMD ["python3","arp-honeypot.py"]
