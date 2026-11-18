# ========================
# Schleifen (Log-Scanner)
# ========================

# 1. Simulierte Log-Daten anlegen

server_logs = [
    "INFO: User admin logged in",
    "ERROR: Failed password for root from 185.220.101.4",
    "INFO: File config.json uploaded",
    "WARNING: High CPU usage (88%)",
    "ERROR: Failed password for user1 from 45.33.32.156",
    "ERROR: Unauthorized API access attempt",
    "INFO: Backup completed successfully"
]

# 2. Zähler und Liste für Treffer vorbereiten
error_count = 0
kritische_logs = []

print("--- Starte Sicherheits-Scan ---")

# 3. Log-Liste Eintrag für Eintrag durchlaufen
for log in server_logs:
    if "ERROR" in log:
        print(f"🚨 KRITISCH:{log}")
        error_count += 1
        kritische_logs.append(log)

# 4. Abschlussbericht (nicht mehr eingerückt!)
print("\n--- Scan-Ergebnis ---")
print(f"Geprüfte Einträge gesamt: {len(server_logs)}")
print(f"Gefundene Fehler (ERROR): {error_count}")
print(f"Gespeicherte kritische Logs: {kritische_logs}")
