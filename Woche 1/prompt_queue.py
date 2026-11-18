# =========================
# Python-Listen (KI-Queue)
# =========================

# 1. Leere Liste für die Warteschlange anlegen
warteschlange = []

print("--- KI-Aufgaben-Manager ---")

# 2. Nutzer dreimal nach Aufgaben fragen
aufgabe_1 = input("Erster Prompt für die KI: ")
aufgabe_2 = input("Zweiter Prompt für die KI: ")
aufgabe_3 = input("Dritter Prompt für die KI: ")

# 3. Eingaben der Reihe nach in die Liste einfügen
warteschlange.append(aufgabe_1)
warteschlange.append(aufgabe_2)
warteschlange.append(aufgabe_3)

# 4. Status im Terminal ausgeben
print("\n--- Status der Verarbeitung ---")
print(f"Aktuelle Warteschlange: {warteschlange}")
print(f"Als Nächstes wird bearbeitet: {warteschlange[0]}")
