unsichere_passwoerter = [
    "123456", "password", "123456789", "12345678", "12345", "111111", "1234567", "sunshine", "qwerty", "iLoveyou", "princess", "admin", "welcome", "666666", "abc123", "football", "123123", "monkey", "654321", "!", "passwort123" 
]

print("--- Passwort-Sicherheitscheck ---")

while True:
    pw = input("Bitte wähle ein neues Passwort: ")

    if pw.lower() in unsichere_passwoerter:
        print("🚨 Abgelehnt: Dieses Passwort steht auf der Liste der häufigsten gehackten Passwörter!")
    elif len(pw) < 10:
        print(f"⚠️ Abgelehnt: Das Passwort muss mindestens 10 Zeichen lang sein (aktuell: {len(pw)} Zeichen).")
    else:
        print("✅ Passwort akzeptiert! Dein Account ist jetzt geschützt.")
        break
    