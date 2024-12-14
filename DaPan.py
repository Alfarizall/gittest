# Data panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1. Tampilkan seluruh data
print("Data panen:")
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    for hasil, jumlah in data['hasil_panen'].items():
        print(f"  {hasil.capitalize()}: {jumlah}")
    print()

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
print("\nJumlah hasil panen jagung dari lokasi2:")
print(data_panen['lokasi2']['hasil_panen']['jagung'])

# 3. Tampilkan nama lokasi dari lokasi3
print("\nNama tempat dari lokasi3:")
print(data_panen['lokasi3']['nama_lokasi'])

# 4. Masukkan jumlah hasil panen padi dan kedelai setiap lokasi ke dalam variabel berbeda
jumlah_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
jumlah_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print("\nJumlah hasil panen padi per lokasi:", jumlah_padi)
print("Jumlah hasil panen kedelai per lokasi:", jumlah_kedelai)

# 5. Buat percabangan
print("\nKondisi lokasi berdasarkan hasil panen:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    nama_lokasi = data['nama_lokasi']

    if padi > 1300 or jagung > 800:
        print(f"{nama_lokasi} perlu perhatian khusus. (padi: {padi}, jagung: {jagung})")
    else:
        print(f"{nama_lokasi} dalam kondisi baik. (padi: {padi}, jagung: {jagung})")