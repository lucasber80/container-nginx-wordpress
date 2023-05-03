from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)
    @task
    def index(self):
        self.client.get("/?p=1") # Realiza um get na url <HOST_DO_WORDPRESS>/?p=1
  
