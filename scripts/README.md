# Wazuh Telegram Alert Integration

## Prérequis

- Bot Telegram créé via [@BotFather](https://t.me/botfather)
- Chat ID du canal/groupe de destination
- Code récuperer sur github avec tuto : https://github.com/Esther7171/Wazuh-Complete-Guide/blob/main/Docs/Integrations/Alerts/Telegram-bot.md#integrating-telegram-bot-with-wazuh-alerts



## Créer un bot Telegram
```
1. Ouvrir Telegram et chercher @BotFather
2. Envoyer /newbot
3. Suivre les instructions
4. Récupérer le token
```

##Obtenir le Chat ID

# Ajouter le bot à votre groupe/canal
# Envoyer un message test
# Récupérer le chat_id :
```bash
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```

## Installer sur Wazuh Manager
# Copier le script
```bash
sudo cp wazuh-telegram-alert.py /var/ossec/integrations/custom-telegram.py
sudo chmod 750 /var/ossec/integrations/custom-telegram.py
sudo chown root:wazuh /var/ossec/integrations/custom-telegram.py
```

# Installer requests si nécessaire
sudo pip3 install requests

## Format des alertes

Les alertes contiennent :
-  Nom et ID de l'agent
-  IP de l'agent
-  Niveau de criticité
-  ID de la règle déclenchée
-  Description de l'alerte
-  Timestamp

