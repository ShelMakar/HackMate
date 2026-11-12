FROM python:3.12-slim

WORKDIR /app

COPY requirements/prod.txt ./prod.txt
RUN pip install --no-cache-dir -r prod.txt

COPY hackmate/ ./hackmate/

RUN python hackmate/manage.py collectstatic --noinput

COPY entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//' /entrypoint.sh && \
    chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "/app/hackmate/manage.py", "runserver", "0.0.0.0:8000"]