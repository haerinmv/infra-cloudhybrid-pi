#!/usr/bin/env python

import sys
import json
import requests
import os

# Obtenir via @BotFather sur Telegram
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID_HERE')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

alert_file = open(sys.argv[1])
alert_json = json.loads(alert_file.read())
alert_file.close()

alert_level = alert_json.get('rule', {}).get('level', "N/A")
description = alert_json.get('rule', {}).get('description', "N/A")
agent_name = alert_json.get('agent', {}).get('name', "N/A")
agent_id = alert_json.get('agent', {}).get('id', "N/A")
agent_ip = alert_json.get('agent', {}).get('ip', "N/A")
manager_name = alert_json.get('manager', {}).get('name', "N/A")
rule_id = alert_json.get('rule', {}).get('id', "N/A")
timestamp = alert_json.get('timestamp', "N/A")

msg_text = f"""
🔔 *Wazuh Alert*
------------------------
*Agent Name:* {agent_name}
*Agent ID:* {agent_id}
*Agent IP:* {agent_ip}
*Manager:* {manager_name}
*Alert Level:* {alert_level}
*Rule ID:* {rule_id}
*Description:* {description}
*Timestamp:* {timestamp}
"""

msg_data = {
    'chat_id': CHAT_ID,
    'text': msg_text,
    'parse_mode': 'Markdown'
}

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

try:
    response = requests.post(TELEGRAM_API_URL, headers=headers, data=json.dumps(msg_data))
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de l'envoi Telegram: {e}")
    sys.exit(1)

sys.exit(0)
