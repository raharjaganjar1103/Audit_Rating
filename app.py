import streamlit as st
import pandas as pd

@st.cache_data
def muat_data_dari_github(url):
    data = pd.read_excel(url)
    return data

# Fungsi untuk menghitung rating
def const calculateRating = () => {
  // FRAUD selalu HIGH
  if (fraud) {
    setRating("HIGH");
    return;
  }

  // >2 MAJOR selalu HIGH
  if (major > 2) {
    setRating("HIGH");
    return;
  }

  // 2 MAJOR: MEDIUM kalau moderate s.d 10, HIGH kalau >10
  if (major === 2) {
    setRating(moderate > 10 ? "HIGH" : "MEDIUM");
    return;
  }

  // 1 MAJOR: MEDIUM kalau moderate s.d 12, HIGH kalau >12
  if (major === 1) {
    setRating(moderate > 12 ? "HIGH" : "MEDIUM");
    return;
  }

  // 0 MAJOR:
  // LOW: moderate 0–7
  // MEDIUM: moderate 8–15
  // HIGH: moderate >15
  if (moderate > 15) {
    setRating("HIGH");
  } else if (moderate >= 8) {
    setRating("MEDIUM");
  } else {
    setRating("LOW");
  }
};

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
