from monitoring.metrics_service import MetricsService

metrics = MetricsService()

print("=" * 80)
print("CPU")
print("=" * 80)
print(metrics.get_cpu_usage())

print()

print("=" * 80)
print("MEMORY")
print("=" * 80)
print(metrics.get_memory_usage())

print()

print("=" * 80)
print("WORKING MEMORY")
print("=" * 80)
print(metrics.get_working_memory())

print()

print("=" * 80)
print("DISK")
print("=" * 80)
print(metrics.get_disk_usage())

print()

print("=" * 80)
print("DATABASE CONNECTIONS")
print("=" * 80)
print(metrics.get_database_connections())

print()

print("=" * 80)
print("DATABASE SIZE")
print("=" * 80)
print(metrics.get_database_size())

print()

print("=" * 80)
print("REQUEST COUNT")
print("=" * 80)
print(metrics.get_request_count())