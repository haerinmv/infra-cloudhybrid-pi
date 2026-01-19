[Interface]
# Adresse IP du serveur VPN dans le tunnel
Address = 10.8.0.1/30
ListenPort = 51820

# Clé privée du serveur (générer avec: wg genkey)
PrivateKey = <GENERATED_WITH_WG_GENKEY>

# Règles iptables pour NAT et forwarding
# Permet au trafic VPN d'accéder au LAN via wlan0
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o wlan0 -j MASQUERADE

[Peer]
# Clé publique du client (obtenue avec: wg pubkey depuis sa PrivateKey)
PublicKey = <CLIENT_PUBLIC_KEY>

# IPs autorisées pour ce peer:
# - 10.8.0.2/32 : IP du client dans le tunnel
# - 10.9.0.0/24 : Accès au réseau distant du client
AllowedIPs = 10.8.0.2/32, 10.9.0.0/24
