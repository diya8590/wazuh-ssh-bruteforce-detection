# Wazuh SSH Brute-Force Detection (SOC Project)

## Overview
This project simulates an SSH brute-force attack and detects it using **Wazuh SIEM**.  
When a brute-force attempt is detected, automated alerts are sent via **Telegram** and **Email**.

> ⚠️ Sensitive credentials are **not included**. Use `.env` file to store your own Telegram bot token and email credentials.

---

## Features
- SSH brute-force simulation using Hydra
- Wazuh rule-based detection
- Python scripts for SOC alerts
  - Telegram notifications
  - Email notifications
- Cron job automation for continuous monitoring
- Logs monitoring via Wazuh JSON alerts

---

## Tools Used
- **Kali Linux** – Generate SSH brute-force attacks
- **Ubuntu Server** – Wazuh manager and alert monitoring
- **Wazuh SIEM** – Detect brute-force attacks
- **Python** – Automation scripts
- **Telegram API** – Alert messages
- **SMTP Email** – Email notifications

---

## Project Structure

```text
wazuh-ssh-bruteforce-detection/
│
├── soc_alert.py        # Python script for Telegram alerts
├── soc_email_alert.py  # Python script for email alerts
├── screenshots/        # Screenshots of attacks and alerts
│   ├── hydra_attack.png
│   ├── wazuh_alert.png
│   ├── telegram_alert.png
│   └── email_alert.png      # Example environment variables file
└── README.md
