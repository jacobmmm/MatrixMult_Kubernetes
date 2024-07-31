from locust import HttpUser, task, between
import numpy as np
class MatrixUser(HttpUser):
    wait_time = between(1, 2)  # Random wait time between requests
    host = "http://118.138.234.138:30007"

    @task
    def send_matrices(self):
        # Sample payload - replace with actual matrix data

        matrix_a = np.random.randint(1, 100, size=(1000, 1000))
        matrix_b = np.random.randint(1, 100, size=(1000, 1000))

        matrix_a_list = matrix_a.tolist()

        matrix_b_list = matrix_b.tolist()

        payload = {"A": matrix_a_list, "B": matrix_b_list}


        self.client.post("/matrixmult", json=payload)