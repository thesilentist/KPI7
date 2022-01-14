FROM python:3.7
ENV port=5000
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD python3 server.py ${port}