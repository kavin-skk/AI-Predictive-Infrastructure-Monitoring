from monitoring.metrics_service import MetricsService


class AnomalyDetector:

    def __init__(self):

        self.metrics = MetricsService()

        # Thresholds
        self.cpu_threshold = 80          # %
        self.memory_threshold = 1.5      # GB

    def _get_metric_value(self, metric):

        try:
            return float(metric["data"]["result"][0]["value"][1])
        except Exception:
            return None

    def detect(self):

        anomalies = []

        # -----------------------
        # CPU
        # -----------------------

        cpu_metric = self.metrics.get_cpu_usage()

        cpu_raw = self._get_metric_value(cpu_metric)

        if cpu_raw is not None:

            # Convert raw cumulative counter into an approximate percentage
            cpu_percent = min(cpu_raw, 100)

            if cpu_percent > self.cpu_threshold:

                anomalies.append({

                    "metric": "CPU Usage",

                    "value": round(cpu_percent, 2),

                    "unit": "%",

                    "status": "Critical"

                })

        # -----------------------
        # MEMORY
        # -----------------------

        memory_metric = self.metrics.get_memory_usage()

        memory_raw = self._get_metric_value(memory_metric)

        if memory_raw is not None:

            memory_gb = memory_raw / (1024 * 1024 * 1024)

            if memory_gb > self.memory_threshold:

                anomalies.append({

                    "metric": "Memory Usage",

                    "value": round(memory_gb, 2),

                    "unit": "GB",

                    "status": "Critical"

                })

        return anomalies