import streamlit as st
from streamlit_option_menu import option_menu # Library untuk navigasi horizontal

# Konfigurasi Halaman
st.set_page_config(page_title="Niko Apriliandi.SH. & Partners", layout="wide", page_icon="⚖️")

# Custom CSS untuk tampilan premium (Warna Navy & Emas)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stHeader { background-color: #1a2a44; }
    h1, h2, h3 { color: #1a2a44; font-family: 'Playfair Display', serif; }
    .stButton>button { background-color: #c5a059; color: white; border-radius: 5px; border: none; }
    .stButton>button:hover { background-color: #b38f48; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGASI HORIZONTAL ---
selected = option_menu(
    menu_title=None,
    options=["Beranda", "Layanan Hukum", "Tim Kami", "Konsultasi"],
    icons=["house", "gavel", "people", "chat-dots"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#1a2a44"},
        "icon": {"color": "#c5a059", "font-size": "18px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "color": "white"},
        "nav-link-selected": {"background-color": "#c5a059"},
    }
)

# --- LOGIKA HALAMAN ---
if selected == "Beranda":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("⚖️ Kantor Hukum Niko Apriliandi, S.H. & Partners")
        st.subheader("Integritas, Profesionalisme, dan Solusi Hukum Terpercaya")
        st.write("""
            Kami hadir untuk memberikan pendampingan hukum terbaik bagi individu maupun badan hukum. 
            Dengan dedikasi tinggi, kami memastikan setiap hak klien terlindungi sesuai hukum yang berlaku di Indonesia.
        """)
        st.button("Pelajari Lebih Lanjut")
    with col2:
        st.image("https://images.unsplash.com", caption="Keadilan Untuk Semua")

elif selected == "Layanan Hukum":
    st.header("Spesialisasi Layanan")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("### Pidana & Perdata")
        st.write("Pendampingan sengketa lahan, perceraian, hingga kasus pidana umum.")
    with c2:
        st.info("### Korporasi")
        st.write("Legal audit, pembuatan kontrak bisnis, dan pendampingan Izin Usaha.")
    with c3:
        st.info("### Ketenagakerjaan")
        st.write("Penyelesaian perselisihan PHK dan hubungan industrial.")

elif selected == "Tim Kami":
    st.header("Partner & Rekan")
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://cdn-icons-png.flaticon.com", width=150)
        st.subheader("Niko Apriliandi, S.H.")
        st.write("Managing Partner")
    with col_b:
        st.write("### Tentang Founder")
        st.write("Niko Apriliandi memiliki pengalaman luas dalam menangani berbagai sengketa strategis di berbagai pengadilan negeri.")

elif selected == "Konsultasi":
    st.header("📩 Hubungi Kami")
    with st.form("form_kontak", clear_on_submit=True):
        nama = st.text_input("Nama Lengkap")
        email = st.text_input("Email / WhatsApp")
        perihal = st.selectbox("Perihal", ["Konsultasi Umum", "Kasus Bisnis", "Somasi/Gugatan"])
        pesan = st.text_area("Jelaskan secara singkat masalah Anda")
        submit = st.form_submit_button("Kirim Jadwal Konsultasi")
        
        if submit:
            st.success(f"Terima kasih Bpk/Ibu {nama}. Pesan Anda telah diterima, kami akan segera menghubungi.")

