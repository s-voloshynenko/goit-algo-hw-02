import random
import time
from queue import Queue

requests_queue = Queue()

class Request:
    def __init__(self):
        self.id = random.randint(1, 1000)

def generate_request():
    new_request = Request()
    requests_queue.put(new_request)
    print(f"Generated request ID: {new_request.id}.")

def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Processed request ID: {request.id}.")
    else:
        print("The queue is empty.")

def main():
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting.")

if __name__ == "__main__":
    main()
