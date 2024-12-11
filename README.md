# Prometheus
Ensure that you adjusted EXPORTER_HOST and EXPORTER_PORT env variables in `docker-compose.yml`.
```bash
$ docker compose up --build -d
or
$ docker compose build
$ docker compose up -d
```

1. **Загрузка процессора (В среднем за последние 5 минут):**
```promql
avg(rate(cpu_usage_percent[5m]))
```
2. **Общий объем памяти и используемая :**
```promql
memory_total_bytes
memory_used_bytes
```
3. **Емкость диска (total and used):**
```promql
disk_total_bytes
disk_used_bytes
```