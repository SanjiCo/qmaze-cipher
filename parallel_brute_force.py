from qmaze_cipher import QMazeCipher
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 🔐 Şifreli metni oluştur (örnek)
gercek_anahtar = "correct_horse_battery_staple"
mesaj = "Gizli bilgi: Bunu kimse bilmemeli!"
sifreli = QMazeCipher(gercek_anahtar).encrypt(mesaj)

print("🔐 Şifreli metin:", sifreli)

# 🔄 Parola listesini yükle
def load_password_list(filepath):
    with open(filepath, "r", encoding="latin1") as f:
        return [line.strip() for line in f if line.strip()]

# 🔧 Her bir iş parçacığının çalıştıracağı fonksiyon
def try_password(password, ciphertext):
    try:
        result = QMazeCipher(password).decrypt(ciphertext)
        if "Gizli" in result:
            return password, result
    except:
        return None

# 🚀 Paralel brute-force
def parallel_brute_force(ciphertext, wordlist_path, max_workers=8):
    passwords = load_password_list(wordlist_path)
    print(f"🔍 Toplam parola sayısı: {len(passwords)}\n")
    found = None

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(try_password, pw, ciphertext): pw for pw in passwords}

        for i, future in enumerate(as_completed(futures)):
            result = future.result()
            if result:
                found, decrypted = result
                print(f"\n✅ Anahtar bulundu! ({i+1}. tahmin): {found}")
                print("📦 Çözüm:", decrypted)
                return found
    print("\n❌ Anahtar bulunamadı.")
    return None

# ⏱️ Süre ölçerek çalıştır
start = time.time()
parallel_brute_force(sifreli, "rockyou_sample.txt", max_workers=8)
end = time.time()
print(f"\n⏱️ Toplam süre: {end - start:.2f} saniye")
