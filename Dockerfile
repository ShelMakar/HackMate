FROM python:3.12-slim AS builder

WORKDIR /app

ARG REQUIREMENTS_FILE=requirements/prod.txt

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements/ ./requirements/

RUN pip install --no-cache-dir -r ${REQUIREMENTS_FILE}

COPY hackmate/ ./hackmate/

RUN mkdir -p /app/hackmate/media /app/hackmate/staticfiles

RUN python hackmate/manage.py collectstatic --noinput


FROM python:3.12-slim AS runtime

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=builder /app/hackmate ./hackmate

COPY entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r$//' /entrypoint.sh && \
    chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

HEALTHCHECK --interval=30s --timeout=3s --start-period=30s --retries=3 \
    CMD python -c "import socket; socket.create_connection(('localhost', 8000), timeout=2).close()" || exit 1


CMD ["gunicorn", "--chdir", "/app/hackmate", "hackmate.wsgi:application", "--bind", "0.0.0.0:8000"]