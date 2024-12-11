from prometheus_client import start_http_server, Gauge
import os
import psutil
import time

cpu_usage = Gauge('cpu_usage_percent', 'CPU Usage Percentage')
memory_total = Gauge('memory_total_bytes', 'Total Memory in Bytes')
memory_used = Gauge('memory_used_bytes', 'Used Memory in Bytes')
disk_total = Gauge('disk_total_bytes', 'Total Disk Space in Bytes')
disk_used = Gauge('disk_used_bytes', 'Used Disk Space in Bytes')

def collect_metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_total.set(memory.total)
    memory_used.set(memory.used)
    disk_total.set(disk.total)
    disk_used.set(disk.used)

if __name__ == "__main__":
    host = os.getenv("EXPORTER_HOST", "0.0.0.0")
    port = int(os.getenv("EXPORTER_PORT", 8000))
    start_http_server(port, addr=host)

    while True:
        collect_metrics()
        time.sleep(5)