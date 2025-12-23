import streamlit as st
import pandas as pd

@st.cache_data
def muat_data_dari_github(url):
    data = pd.read_excel(url)
    return data

# Fungsi untuk menghitung rating
def calculate_rating(major, moderate, fraud):
    # FRAUD selalu HIGH
    if fraud:
        return "HIGH"

    # >2 MAJOR selalu HIGH
    if major > 2:
        return "HIGH"

    # 2 MAJOR: MEDIUM kalau moderate <=10, HIGH kalau >10
    if major == 2:
        return "HIGH" if moderate > 10 else "MEDIUM"

    # 1 MAJOR: MEDIUM kalau moderate <=12, HIGH kalau >12
    if major == 1:
        return "HIGH" if moderate > 12 else "MEDIUM"

    # 0 MAJOR:
    # LOW: 0–7, MEDIUM: 8–15, HIGH: >15
    if moderate > 15:
        return "HIGH"
    if moderate >= 8:
        return "MEDIUM"
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
