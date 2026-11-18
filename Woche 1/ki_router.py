# =====================
# Der KI-Prompt-Router
# =====================

print("--- Intelligenter KI-Modell-Router ---")

# 1. Nutzereingabe abfragen und direkt in Kleinbuchstaben umwandeln
anfrage = input("Was soll die KI für dich tun? ").lower()

# 2. Bonus-Prüfung (Länge der Eingabe checken) & Routing-Logik
if len(anfrage) < 4:
    print("⚠️  Anfrage zu kurz! Bitte beschreibe dein Anliegen etwas genauer.")
elif "übersetz" in anfrage:
    print("🌍  Route zu Deepl API: Optimales Modell für präzise Übersetzungen gewählt.")
elif "code" in anfrage or "python" in anfrage:
    print("💻  Route zu Claude 3.5 Sonnet / GPT-4o: Spezialisiert auf Programmierung.")
elif "bild" in anfrage or "foto" in anfrage:
    print("🎨  Route zu Midjourney / DALL-E 3: Bildgenerierung wird gestartet.")
else:
    print("🤖 Route zu Standard-LLM: Allgemeine Textverarbeitung aktiv.")
