#!/bin/bash

# DuckDNS Dynamic DNS Update Script
# Cron: */5 * * * * ~/duckdns/duckdns-update.sh

# Configuration
DUCKDNS_DOMAIN="your-subdomain"
DUCKDNS_TOKEN="your-duckdns-token-here"
LOG_FILE="$HOME/duckdns/duck.log"

# Mise à jour de l'IP publique
echo url="https://www.duckdns.org/update?domains=${DUCKDNS_DOMAIN}&token=${DUCKDNS_TOKEN}&ip=" | curl -k -o ${LOG_FILE} -K -
