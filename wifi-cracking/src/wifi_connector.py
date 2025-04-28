import subprocess
import time
import os
import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_wifi_profile(ssid, password):
    """Generate a WiFi profile XML file for connection."""
    profile = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    profile_path = f"wifi_profile_{ssid}.xml"
    with open(profile_path, "w") as f:
        f.write(profile)
    return profile_path

def try_connect_wifi(ssid, password):
    """Attempt to connect to the WiFi network with the given password."""
    try:
        profile_path = generate_wifi_profile(ssid, password)
        subprocess.run(["netsh", "wlan", "add", "profile", f"filename={profile_path}"], capture_output=True, check=True)
        result = subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"], capture_output=True, text=True, check=True)
        time.sleep(2)
        status = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True, check=True)
        if f"SSID                   : {ssid}" in status.stdout and "State                  : connected" in status.stdout:
            logging.info(f"Successfully connected to {ssid} with password: {password}")
            os.remove(profile_path)
            return True
        subprocess.run(["netsh", "wlan", "disconnect"], capture_output=True)
        subprocess.run(["netsh", "wlan", "delete", "profile", f"name={ssid}"], capture_output=True)
        os.remove(profile_path)
        return False
    except subprocess.CalledProcessError as e:
        logging.debug(f"Failed to connect with password {password}: {e}")
        if os.path.exists(profile_path):
            os.remove(profile_path)
        return False