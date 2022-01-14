FROM python:3.7
WORKDIR /usr/src/app
ENV ip=server
ENV port=5000
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD python client.py ${ip} ${port}