[Interface]
# Adresse du Pi dans le tunnel site-to-site avec AWS
Address = 10.9.0.1/30

# Clé privée du Pi pour ce tunnel
PrivateKey = <PI_PRIVATE_KEY_FOR_AWS_TUNNEL>

# Activer le forwarding IP pour router entre réseaux
PostUp = sysctl -w net.ipv4.ip_forward=1

# Peer AWS EC2
[Peer]
# Clé publique de l'instance EC2
PublicKey = <EC2_PUBLIC_KEY>

# IP publique élastique de l'EC2
Endpoint = <EC2_ELASTIC_IP>:51820

# Routes autorisées via ce tunnel:
# - 10.9.0.2/32 : IP de l'EC2 dans le tunnel
# - 172.31.0.0/16 : VPC AWS (accès au réseau privé EC2)
AllowedIPs = 10.9.0.2/32, 172.31.0.0/16

# Maintien la connexion active (critique pour site-to-site)
PersistentKeepalive = 25
