from qmaze_cipher import QMazeCipher

# Şifreleyen kişi
gercek_anahtar = "Test123"
mesaj = "Gizli mesaj"
sifreli = QMazeCipher(gercek_anahtar).encrypt(mesaj)

# Saldırgan tarafı
print("🔐 Şifreli metin:", sifreli)

anahtar_listesi = ["abc", "test", "Test123", "admin", "1234"]
for guess in anahtar_listesi:
    try:
        cozum = QMazeCipher(guess).decrypt(sifreli)
        if "Gizli" in cozum:  # Basit bir doğrulama mantığı
            print(f"✅ Anahtar bulundu: {guess} → {cozum}")
            break
        else:
            print(f"❌ {guess} → anlamsız çıktı: {cozum}")
    except Exception:
        print(f"❌ {guess} → hata oluştu (geçersiz çözüm)")
