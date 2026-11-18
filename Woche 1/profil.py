# ==================================
# Variablen, Datentypen & f-Strings
# ==================================

# 1. Variablen anlegen
mein_name = "Roberto Arduengo"
ziel_position = "Fachinformatiker Anwendungsentwicklung"
fokus = "KI & Cybersecurity"
ziel_datum = "11.01.2027"

# 2. Vorstellungstext mit f-Strings im Terminal ausgeben
print("--- Bewerber-Profil ---")
print(f"Hallo! Ich bin {mein_name}.")
print(f"Aktuell befinde ich mich in der Umschulung zum {ziel_position}.")
print(f"Mein technischer Schwerpunkt liegt auf den Bereichen {fokus}.")
print(f"Ab dem {ziel_datum} starte ich meine Bewerbungsphase für mein Praxisprojekt.")

# 3. Bonus: Datentypen überprüfen
print("\n--- Datentyp-Check ---")
print(f"Datentyp von 'mein_name': {type(mein_name)}")
print(f"Datentyp von 'ziel_datum': {type(ziel_datum)}")
