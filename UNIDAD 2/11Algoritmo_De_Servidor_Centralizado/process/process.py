import requests
import time
import random
import sys

class Process:
    def __init__(self, name, coordinator_url):
        self.name = name
        self.coordinator_url = coordinator_url

    def request_token(self):
        response = requests.post(
            f"{self.coordinator_url}/request_token", 
            json={"name": self.name}
        )
        print(response.json()['message'])

    def release_token(self):
        response = requests.post(
            f"{self.coordinator_url}/release_token", 
            json={"name": self.name}
        )
        print(response.json()['message'])

    def access_critical_section(self):
        print(f"{self.name} is accessing the critical section.")
        time.sleep(random.randint(1, 3))  # Simulate work
        print(f"{self.name} has finished using the critical section.")

    def run(self):
        while True:
            self.request_token()
            time.sleep(5)  # Simulate waiting

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process.py <name> <coordinator_url>")
        sys.exit(1)

    name = sys.argv[1]
    coordinator_url = sys.argv[2]
    process = Process(name, coordinator_url)
    process.run()
