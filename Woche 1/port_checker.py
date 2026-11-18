# ===================================
# Benutzereingaben & Logik (if/else)
# ===================================

print("--- Mini Port-Security-Checker ---")

# 1. Benutzereingabe abfragen und direkt in eine Ganzzahl (int) umwandeln
eingabe = input("Bitte gib eine Portnummer zur Prüfung ein: ")
port = int(eingabe)

# 2. Sicherheitsprüfung mit if / elif / else (inkl. Bonus-Prüfung)
if port < 1 or port > 65535:
    print("❌  Ungültige Portnummer! Gültige Ports liegen zwischen 1 und 65535.")
elif port == 80:
    print("⚠️  Port 80 (HTTP): Unverschlüsselter Datenverkehr! Sicherheitsrisiko.")
elif port == 443:
    print("✅  Port 443 (HTTPS): Verschlüsselte Verbindung. Sicher.")
elif port == 22:
    print("🔑  Port 22 (SSH): Fernwartungs-Zugang erkannt. Starkes Passwort erforderlich.!")
elif port == 21:
    print("🚨  Port 21 (FTP): Veraltetes Protokoll! Unverschlüsselte Dateiübertragung.")
else:
    print(f"ℹ️  Port {port}: Kein Standard-Webport. Manuelle Prüfung nötig.")
