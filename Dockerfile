FROM python:3.9-slim
RUN apt update; apt install -y libgl1
# Project Files and Settings
RUN mkdir -p /app && mkdir -p /app/static && mkdir -p /app/media
VOLUME ["/app/static", "/app/media"]
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . ./
COPY dndtools/settings_secret.py.template ./dndtools/settings_secret.py
# Server
EXPOSE 8080
STOPSIGNAL SIGINT
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080"]
CMD ["--workers=4", "dndtools.wsgi"]
