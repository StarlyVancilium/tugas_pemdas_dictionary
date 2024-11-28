data_panen = {
    'lokasi': {
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
}

#tampil seluruh data
for i in data_panen['lokasi']:
    print(data_panen['lokasi'][i])
    
print()    

#jagung lokasi 2
jagung_lok2 = data_panen['lokasi']['lokasi2']['hasil_panen']['jagung']
print(f"Jagung lokasi 2: {jagung_lok2}")

#masukkan jumlah hasil panen padi dan kedelai setiap lokasi ke dalam variabel yang berbeda
padi_lok1 = data_panen['lokasi']['lokasi1']['hasil_panen']['padi']
padi_lok2 = data_panen['lokasi']['lokasi2']['hasil_panen']['padi']
padi_lok3 = data_panen['lokasi']['lokasi3']['hasil_panen']['padi']
padi_lok4 = data_panen['lokasi']['lokasi4']['hasil_panen']['padi']
padi_lok5 = data_panen['lokasi']['lokasi5']['hasil_panen']['padi']

kedelai_lok1 = data_panen['lokasi']['lokasi1']['hasil_panen']['kedelai']
kedelai_lok2 = data_panen['lokasi']['lokasi2']['hasil_panen']['kedelai']
kedelai_lok3 = data_panen['lokasi']['lokasi3']['hasil_panen']['kedelai']
kedelai_lok4 = data_panen['lokasi']['lokasi4']['hasil_panen']['kedelai']
kedelai_lok5 = data_panen['lokasi']['lokasi5']['hasil_panen']['kedelai']\

#padi > 1300 atau jagung > 800, maka butuh perhatian khusus
lokasi_perhatian = []
for i in data_panen['lokasi']:
    if data_panen['lokasi'][i]['hasil_panen']['padi'] > 1300 or data_panen['lokasi'][i]['hasil_panen']['jagung'] > 800:
        lokasi_perhatian.append(data_panen['lokasi'][i]['nama_lokasi'])
        
for i in lokasi_perhatian:
    print(f"Lokasi {i} memerlukan perhatian khusus.")                                