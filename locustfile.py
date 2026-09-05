from locust import HttpUser, task, between

class InfrastructureUser(HttpUser):
    wait_time = between(0.05, 0.1)

    @task(5)
    def metrics(self):
        self.client.get("/metrics")

    @task(3)
    def health(self):
        self.client.get("/health")

    @task(2)
    def predictions(self):
        self.client.get("/phase2/predictions")
