[Interface]
# Adresse IP du client dans le tunnel
Address = 10.8.0.2/30

# Clé privée du client (générer avec: wg genkey)
PrivateKey = <CLIENT_PRIVATE_KEY>

# DNS pour résolution via le tunnel
DNS = 1.1.1.1

[Peer]
# Clé publique du serveur VPN (Raspberry Pi)
PublicKey = <SERVER_PUBLIC_KEY>

# Point d'entrée du serveur VPN
# Peut être une IP publique ou un domaine DuckDNS
Endpoint = <YOUR_PUBLIC_IP>:51820

# Routes autorisées via le tunnel:
# - 10.8.0.0/30 : Réseau du tunnel VPN
# - 192.168.1.0/24 : Réseau LAN local accessible via VPN
AllowedIPs = 10.8.0.0/30, 192.168.1.0/24

# Maintien la connexion active (utile derrière NAT)
PersistentKeepalive = 25
