# ==================
# KI-Kosten-Rechner
# ==================

# 1. Verfügbare Modelle definieren
modelle = ["gpt-4o-mini", "gpt-4o", "claude-3.5-sonnet"]

print("--- KI-Token- & Kosten-Rechner ---")
print(f"Verfügbare Modelle: {modelle}")

# 2. Modell und Wortanzahl abfragen
modell = input("Welches Modell möchtest du nutzen? ").lower()
woerter = int(input("Wie viele Wörter umfasst dein Text? "))

# 3. Ungefähre Token-Anzahl berechnen
tokens = woerter * 1.3

# 4. Prüfung und Ausgabe mit 'not in'
if modell not in modelle:
    print("❌  Fehler: Dieses Modell wird nicht unterstützt.")
elif modell == "gpt-4o-mini":
    print(f"💚  Günstiges Modell gewählt! Geschätzte Tokens: {tokens} (Kosten: unter 0,01 €)")
else:
    print(f"💎  Premium-Modell gewählt! Geschätzte Tokens: {tokens} (Höhere API-Kosten beachten)")
