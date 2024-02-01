FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -e . && \
    chmod +x migrate.sh && \
    chmod +x entrypoint.sh

EXPOSE 8080

CMD ["/app/entrypoint.sh]
