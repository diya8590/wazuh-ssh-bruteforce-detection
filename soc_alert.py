import json
import requests
from datetime import datetime

# ---------------------------

# CONFIGURATION

# ---------------------------

TELEGRAM_TOKEN = "8656525474:AAEANKCcaBUBPRzRqbTCBYVA03rzdkiWc5Y"
CHAT_ID = 1503027556
ALERTS_FILE = "/var/ossec/logs/alerts/alerts.json"

# --------------------------

# FUNCTION TO SEND TELEGRAM ALERT

# --------------------------
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        print(f"[Telegram] Alert sent: {message}")
    except Exception as e:
        print(f"[Telegram] Error: {e}")

# --------------------------

# MAIN SCRIPT

# --------------------------
try:
    with open(ALERTS_FILE) as f:
         for line in f:
             alert = json.loads(line)
             desc = alert.get("rule", {}).get("description", "").lower()
             if "sshd" in desc or "ssh" in desc:
                 src_ip = alert.get("data", {}).get("srcip", "unknown")
                 ts = alert.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                 message = f"  SOC ALERT\nSSH Brute Force Detected!\nIP: {src_ip}\nTime: {ts}\nRule: {desc}"
                 send_telegram(message)

except FileNotFoundError:
    print(f"[Error] Wazuh alerts file not found: {ALERTS_FILE}")
except json.JSONDecodeError:
    print("[Error] JSON decode error in alert file")
except Exception as e:
    print(f"[Error] {e}")

