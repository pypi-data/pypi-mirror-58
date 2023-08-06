FROM python:3.8

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir uwsgi
COPY . .
RUN pip install .
EXPOSE 8180
ENTRYPOINT ["/bin/bash", "/usr/src/app/entrypoint.sh"]
