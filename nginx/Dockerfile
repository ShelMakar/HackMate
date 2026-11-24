FROM nginx:stable-alpine AS builder

WORKDIR /app

COPY nginx.conf ./nginx.conf

FROM nginx:stable-alpine AS runtime

COPY --from=builder /app/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://127.0.0.1/nginx-health || exit 1

CMD ["nginx", "-g", "daemon off;"]
