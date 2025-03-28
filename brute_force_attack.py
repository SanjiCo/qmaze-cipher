from qmaze_cipher import QMazeCipher

# Adım 1: Gerçek anahtar ve mesaj
gercek_anahtar = "correct_horse_battery_staple"
mesaj = "Gizli bilgi: Bunu kimse bilmemeli!"
sifreli = QMazeCipher(gercek_anahtar).encrypt(mesaj)

print("🔐 Şifreli metin:", sifreli)

# Adım 2: Parola listesi oku
def load_password_list(filepath):
    with open(filepath, "r", encoding="latin1") as f:
        return [line.strip() for line in f if line.strip()]

# Adım 3: Brute-force denemesi
def brute_force(ciphertext, wordlist_path):
    passwords = load_password_list(wordlist_path)
    for i, guess in enumerate(passwords):
        try:
            result = QMazeCipher(guess).decrypt(ciphertext)
            if "Gizli" in result:
                print(f"\n✅ Anahtar bulundu! ({i+1}. tahmin): {guess}")
                print("📦 Çözüm:", result)
                return guess
        except Exception:
            continue
    print("\n❌ Anahtar bulunamadı.")
    return None

import time

start = time.time()  # ⏱️ Süreyi başlat
brute_force(sifreli, "rockyou_sample.txt")
end = time.time()    # ⏱️ Süreyi bitir

print(f"\n⏱️ Toplam süre: {end - start:.2f} saniye")
