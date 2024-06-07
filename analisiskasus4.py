import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pastikan path file benar
file_path_persediaan = "D:/Semester 4/latihan analisis data/persediaan.csv"

# Membaca data persediaan dari file CSV
df_persediaan = pd.read_csv(file_path_persediaan)

# Hitung saldo akhir setiap barang
df_persediaan['Saldo Akhir'] = df_persediaan['Jumlah Dibeli'] - df_persediaan['Jumlah Keluar']

# Filter barang dengan saldo akhir di bawah 15
df_saldo_akhir_bawah_15 = df_persediaan[df_persediaan['Saldo Akhir'] < 15]

# Plotting
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

# Menggunakan seaborn untuk membuat barplot
ax = sns.barplot(
    x='Nama Barang',
    y='Saldo Akhir',
    data=df_saldo_akhir_bawah_15,
    palette='coolwarm'
)

# Menambahkan judul dan label
ax.set_title('Barang dengan Saldo Akhir di Bawah 15 pada Akhir Mei 2024', fontsize=16)
ax.set_xlabel('Nama Barang', fontsize=14)
ax.set_ylabel('Saldo Akhir', fontsize=14)

# Menampilkan nilai saldo akhir di atas batang
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9),
                textcoords='offset points')

# Rotasi nama barang agar terlihat jelas
plt.xticks(rotation=45, ha='right')

# Menyempurnakan tata letak
plt.tight_layout()

# Menampilkan plot
plt.show()
