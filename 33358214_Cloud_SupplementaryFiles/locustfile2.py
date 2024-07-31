from locust import HttpUser, task, between
import numpy as np

class MatrixUser(HttpUser):
    wait_time = between(1, 2)  # Random wait time between requests
    host = "http://118.138.234.138:30007"

    @task
    def send_matrices(self):
        # Generate two 8660x8660 matrices with random 32-bit float numbers
        matrix_a = np.random.rand(8660, 8660).astype(np.float32)
        matrix_b = np.random.rand(8660, 8660).astype(np.float32)

        # Convert matrices to lists
        matrix_a_list = matrix_a.tolist()
        matrix_b_list = matrix_b.tolist()

        # Create payload
        payload = {"A": matrix_a_list, "B": matrix_b_list}

        # Send POST request with the payload
        self.client.post("/matrixmult", json=payload)
