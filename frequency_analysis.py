from qmaze_cipher import QMazeCipher
from collections import Counter
import base64
import matplotlib.pyplot as plt

# Şifreleme
key = "StrongKey123"
plaintext = "Gizli mesaj gizlidir gizli gizli gizli gizli"
cipher = QMazeCipher(key)
encrypted = cipher.encrypt(plaintext)

print("🔐 Şifreli metin (Base64):", encrypted)

# Frekans Analizi Fonksiyonu
def frequency_plot(data, title):
    counter = Counter(data)
    total = sum(counter.values())
    freqs = {char: count / total for char, count in counter.items()}
    sorted_freqs = dict(sorted(freqs.items(), key=lambda x: -x[1]))

    plt.figure(figsize=(10, 4))
    plt.bar(sorted_freqs.keys(), sorted_freqs.values())
    plt.title(title)
    plt.xlabel("Karakter")
    plt.ylabel("Frekans")
    plt.grid(True)
    plt.show()

# 🔍 Orijinal metin frekansı
frequency_plot(plaintext, "Orijinal Metin Harf Frekansı")

# 🔍 Şifreli metnin (Base64 hali) frekansı
decoded = base64.urlsafe_b64decode(encrypted).decode('latin1', errors='ignore')
frequency_plot(decoded, "Şifreli Metin (Base64) Frekansı")
