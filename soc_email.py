import json
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "YOUR_EMAIL"
EMAIL_PASS = "YOUR_EMAIL_PASSWORD"
EMAIL_TO = "EMAIL_ALERT_TO_GET"

ALERT_FILE = "/var/ossec/logs/alerts/alerts.json"

def send_email(message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = "🚨 SOC ALERT - SSH Brute Force"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
        server.quit()

        print("Email Alert Sent")

    except Exception as e:
        print(f"Email Error: {e}")

with open(ALERT_FILE) as f:
    for line in f:
        alert = json.loads(line)
        desc = alert.get("rule", {}).get("description", "").lower()

        if "ssh" in desc:
            ip = alert.get("data", {}).get("srcip", "Unknown")
            time = datetime.now()

            message = f"""
SOC ALERT

SSH Brute Force Detected
Attacker IP: {ip}
Time: {time}
"""

            send_email(message)
