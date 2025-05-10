import subprocess
import re
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def list_wifi_networks():
    """List available WiFi networks using netsh (Windows)."""
    try:
        result = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True, check=True)
        output = result.stdout
        ssids = re.findall(r"SSID \d+ : (.+)", output)
        if not ssids:
            logging.error("No WiFi networks found. Ensure WiFi is enabled.")
            return []
        logging.info("Available WiFi networks:")
        for i, ssid in enumerate(ssids, 1):
            print(f"{i}. {ssid}")
        return ssids
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to list WiFi networks: {e}")
        return []

def select_network(ssids):
    """Prompt user to select a WiFi network."""
    while True:
        try:
            choice = int(input("Enter the number of your mobile hotspot WiFi (e.g., 1): "))
            if 1 <= choice <= len(ssids):
                return ssids[choice - 1]
            print(f"Please enter a number between 1 and {len(ssids)}.")
        except ValueError:
            print("Please enter a valid number.")