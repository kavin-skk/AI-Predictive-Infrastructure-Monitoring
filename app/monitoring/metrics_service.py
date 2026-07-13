import requests


class MetricsService:

    def __init__(self):

        self.prometheus_url = "http://prometheus:9090"

    def query(self, promql):

        try:

            response = requests.get(
                f"{self.prometheus_url}/api/v1/query",
                params={"query": promql},
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }

    # ----------------------------------------------------
    # CPU Usage
    # ----------------------------------------------------

    def get_cpu_usage(self):

        query = """
        container_cpu_usage_seconds_total
        """

        return self.query(query)

    # ----------------------------------------------------
    # Memory Usage
    # ----------------------------------------------------

    def get_memory_usage(self):

        query = """
        container_memory_usage_bytes
        """

        return self.query(query)

    # ----------------------------------------------------
    # Working Set Memory
    # ----------------------------------------------------

    def get_working_memory(self):

        query = """
        container_memory_working_set_bytes
        """

        return self.query(query)

    # ----------------------------------------------------
    # Disk Usage
    # ----------------------------------------------------

    def get_disk_usage(self):

        query = """
        container_fs_usage_bytes
        """

        return self.query(query)

    # ----------------------------------------------------
    # PostgreSQL Connections
    # ----------------------------------------------------

    def get_database_connections(self):

        query = """
        pg_stat_database_numbackends
        """

        return self.query(query)

    # ----------------------------------------------------
    # PostgreSQL Database Size
    # ----------------------------------------------------

    def get_database_size(self):

        query = """
        pg_database_size_bytes
        """

        return self.query(query)

    # ----------------------------------------------------
    # HTTP Requests
    # ----------------------------------------------------

    def get_request_count(self):

        query = """
        home_page_requests_total
        """

        return self.query(query)

    # ----------------------------------------------------
    # Get Everything
    # ----------------------------------------------------

    def get_all_metrics(self):

        return {

            "cpu": self.get_cpu_usage(),

            "memory": self.get_memory_usage(),

            "working_memory": self.get_working_memory(),

            "disk": self.get_disk_usage(),

            "database_connections": self.get_database_connections(),

            "database_size": self.get_database_size(),

            "request_count": self.get_request_count()
        }