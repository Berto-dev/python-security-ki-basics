# ======================
# Dictionaries & Lookup
# ======================

# 1. Sicherheits-Datenbank als Dictionary anlegen
threat_db = {
    "185.220.101.4": "Kritisch - Bekannter Tor-Exit-Node (Brute-Force)",
    "45.33.32.156": "Mittel - Automatisierter Port-Scanner",
    "103.21.244.0": "Hoch - Verdächtige API-Anfragen (DDoS-Versuch)"
}

print("--- Threat-Intelligence-Abfrage ---")

# 2. IP-Adresse vom Nutzer abfragen
gesuchte_ip = input("Bitte gib die zu prüfende IP-Adresse ein: ")

# 3. Prüfung mit 'in' und direktem Zugriff über die Variable
if gesuchte_ip in threat_db:
    print(f"🚨 TREFFER IN DATENBANK: {threat_db[gesuchte_ip]}")
else:
    print("✅ IP-Adresse ist aktuell nicht in der Threat-Datenbank gelistet.")
     