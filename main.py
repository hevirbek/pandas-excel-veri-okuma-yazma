import pandas as pd
import matplotlib.pyplot as plt

# Dosya adı tanımlama
filename = 'ornek.xlsx'

# Veriyi çekme
df = pd.read_excel(filename, index_col=False)

# Alış sütunu
alis = df["Alış"]

# Satış sütunu
satis = df["Satış"]


# Kar sütünu ekleme
def kar(row):
    return row["Satış"] - row["Alış"]


df['Kar'] = df.apply(lambda x: kar(x), axis=1)

# Kar grafiğini çıkarma
kar = df['Kar']
plt.plot(kar)
plt.title("Kar grafiği")
plt.savefig("kargrafigi.png")

# Sonuçta oluşan veriyi excel dosyası olarak çıkarma
df.to_excel('sonuc.xlsx', index=False, sheet_name='Güncel')
