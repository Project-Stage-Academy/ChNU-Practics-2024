FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

RUN python3 -m venv /opt/venv && \
  /opt/venv/bin/pip install --upgrade pip && \
  /opt/venv/bin/pip install -e .

EXPOSE 8000

CMD ["/opt/venv/bin/gunicorn", "-c", "python:config.gunicorn", "config.wsgi"]
