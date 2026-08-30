from monitoring.metrics_service import MetricsService


class AnomalyDetector:

    def __init__(self):

        self.metrics = MetricsService()

        # Thresholds
        self.cpu_threshold = 80          # %
        self.memory_threshold = 1.5      # GB

        # Primary application container to monitor
        self.target_container = "monitoring-app"

    def _get_metric_value(self, metric):

        try:
            results = metric["data"]["result"]

            if not results:
                return None

            return float(results[0]["value"][1])

        except Exception:
            return None

    def detect(self):

        anomalies = []

        # ====================================================
        # CPU USAGE
        # ====================================================

        # Calculate CPU percentage using Prometheus rate()
        cpu_query = f"""
        rate(container_cpu_usage_seconds_total{{name="{self.target_container}"}}[1m]) * 100
        """

        cpu_metric = self.metrics.query(cpu_query)

        cpu_percent = self._get_metric_value(cpu_metric)

        if cpu_percent is not None:

            cpu_percent = round(cpu_percent, 2)

            if cpu_percent > self.cpu_threshold:

                anomalies.append({

                    "metric": "CPU Usage",

                    "value": cpu_percent,

                    "unit": "%",

                    "status": "Critical"

                })

        # ====================================================
        # MEMORY USAGE
        # ====================================================

        memory_query = f"""
        container_memory_usage_bytes{{name="{self.target_container}"}}
        """

        memory_metric = self.metrics.query(memory_query)

        memory_raw = self._get_metric_value(memory_metric)

        if memory_raw is not None:

            memory_gb = memory_raw / (1024 * 1024 * 1024)

            memory_gb = round(memory_gb, 2)

            if memory_gb > self.memory_threshold:

                anomalies.append({

                    "metric": "Memory Usage",

                    "value": memory_gb,

                    "unit": "GB",

                    "status": "Critical"

                })

        return anomalies