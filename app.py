import streamlit as st
import pandas as pd

@st.cache_data
def muat_data_dari_github(url):
    data = pd.read_excel(url)
    return data

# Fungsi untuk menghitung rating
def calculate_rating(minor, moderate, major, fraud):
    # FRAUD selalu HIGH
    if fraud:
        return "HIGH"

   # HIGH
    if (
        ( major == 0 and moderate > 15) or
        ( major == 1 and moderate > 12) or
        ( major == 2 and moderate > 10) or
        (major >= 3)
    ):
        return "HIGH"

    # MEDIUM
    if (
        (major == 0 and 8 <= moderate <= 15) or    # Kriteria 1
        (major == 1 and moderate <= 12) or    # Kriteria 2
        (major == 2 and moderate <= 10)    # Kriteria 3
         ):
        return "MEDIUM"

   # Kriteria LOW:
    if (major == 0 and moderate <= 7):
        return "LOW"

 # Default case:
    # Jaminan: kalau sudah ada temuan major >= 1, minimal MEDIUM,
    # jadi tidak akan pernah LOW.
    if major >= 1:
        return "MEDIUM"

  # Fallback terakhir (kalau benar-benar di luar semua rule di atas)
    return "LOW"
    
# Streamlit untuk antarmuka
st.title("Kalkulator Audit Rating")
st.markdown('''
- Refresh web ini jika rating audit issue nya tidak berjalan
- Disarankan menggunakan web browser seperti Google Chrome atau Microsoft Edge
- Penginputan jumlah temuan bisa ketikkan angka nya langsung
''')

# Input jumlah temuan
minor = st.number_input("Masukkan jumlah temuan Minor:", min_value=0, step=1)
moderate = st.number_input("Masukkan jumlah temuan Moderate:", min_value=0, step=1)
major = st.number_input("Masukkan jumlah temuan Major:", min_value=0, step=1)

# Checkbox untuk "Terdapat Fraud"
fraud = st.checkbox("Terdapat Fraud")

# Hitung rating
rating = calculate_rating(minor, moderate, major, fraud)

# Tampilkan hasil
st.write(f"Rating Audit Issue Anda adalah: **{rating}**")
