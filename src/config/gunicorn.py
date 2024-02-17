import os


bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"
accesslog = "-"
access_log_format = (
    "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"  # noqa: E501
)

workers = 4
worker_connections = 1000
threads = 4

reload = bool(os.getenv("WEB_RELOAD", "false"))
