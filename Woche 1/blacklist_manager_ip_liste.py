# =========================
# Python-Listen (Security)
# =========================

verdaechtige_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.23", "185.220.101.4"]

print(f"Start-Status: Es befinden sich {len(verdaechtige_ips)} IPs auf der Sperrliste.")

verdaechtige_ips.append("45.33.32.156")
verdaechtige_ips.append("103.21.244.0")

verdaechtige_ips.remove("192.168.1.10")

print("\n--- Aktualisierte Sperrlist ---")
print(f"Komplette Liste: {verdaechtige_ips}")
print(f"Neue Anzahl: {len(verdaechtige_ips)} IPs")
print(f"Erste IP in der Liste: {verdaechtige_ips[0]}")
print(f"Letzte IP in der Liste: {verdaechtige_ips[-1]}")
