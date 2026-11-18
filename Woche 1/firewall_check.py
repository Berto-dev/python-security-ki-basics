# ===============
# Firewall-Check
# ===============

# 1. Blacklist und Whitelist anlegen
blacklist = ["185.220.101.4", "45.33.32.156", "103.21.244.0"]
whitelist = ["192.168.1.1", "10.0.0.1"]

print("--- Firewall-Zugriffskontrolle ---")

# 2. IP-Adresse abfragen
aktuelle_ip = input("Bitte gib deine IP-Adesse ein: ")

# 3. Prüfung mit 'in' und Bonus-Aktion im 'else'-Block
if aktuelle_ip in blacklist:
    print("🚨  ALARM: Zugriff verweigert! Diese IP ist gesperrt.")
elif aktuelle_ip in whitelist:
    print("✅  Zugriff gewährt: Vertrauenswürdige interne IP.")
else:
    print("⚠️  Unbekannte IP-Adresse. Bitte 2-Faktor-Authentifizierung durchführen.")
    # Bonus-Schritt: Unbekannte IP automatisch zur Blacklist hinzufügen
    blacklist.append(aktuelle_ip)
    print(f"ℹ️  Die IP {aktuelle_ip} wurde vorsorglich auf die Blacklist gesetzt.")
    print(f"Aktualisierte Blacklist: {blacklist}")
    