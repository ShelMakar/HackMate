FROM python:3.12-slim

WORKDIR /app

COPY requirements/prod.txt ./prod.txt
RUN pip install --no-cache-dir -r prod.txt

COPY hackmate/ ./hackmate/

RUN python hackmate/manage.py collectstatic --noinput

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "--chdir", "/app/hackmate", "hackmate.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-"]