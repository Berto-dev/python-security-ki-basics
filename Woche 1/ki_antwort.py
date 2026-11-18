# ===========================
# Dictionaries (KI-Response)
# ===========================

# 1. Simulierte API-Antwort anlegen
api_response = {
    "modell": "gpt-4o",
    "status": "erfolgreich",
    "kategorie": "Phising-Verdacht",
    "risiko_score": 85,
    "empfehlung": "Link nicht anklicken und Absender blockieren."
}

# 2. Sicherheitsbericht ausgeben
print("--- KI-Sicherheitsanalyse ---")
print(f"Analysiert durch Modell: {api_response[ 'modell']}")
print(f"Erkannte Kategorie: {api_response[ 'kategorie']}")
print(f"Risiko-Bewertung: {api_response[ 'risiko_score']} von 100")
print(f"Handlungsempfehlung: {api_response[ 'empfehlung']}")

# 3. Werte aktualisieren und neuen Schlüssel hinzufügen
api_response["risiko_score"] = 95
api_response["manuell_geprueft"] = True

print("\n--- Aktualisiertes Dictionary ---")
print(api_response)
