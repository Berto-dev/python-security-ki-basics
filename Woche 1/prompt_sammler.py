# ========================
# while-Schleifen & break
# ========================

# 1. Lerre Liste anlegen

aufgaben = []

print("--- KI-Aufgaben-Sammler ---")

# 2. Endlosschleife für beliebig viele Eingaben
while True:
    eingabe = input("Gib eine Aufgabe für die KI ein (oder 'start' zum Ausführen): ")

    # 3. Abbruchbedingung prüfen
    if eingabe.lower() == "start":
        break
    else:
        aufgaben.append(eingabe)
        print(f"➕ Aufgabe hinzugefügt. (Aktuell {len(aufgaben)}) in der Warteschlange.")

# 4. Gesammelte Aufgaben nach dem Abbruch der Reihe nach ausgeben
print("\n🚀 Starte KI-Verarbeitung für folgende Aufgaben: ")
for aufgabe in aufgaben:
    print(f"- {aufgabe}")
    