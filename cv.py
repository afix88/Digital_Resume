import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Afik Maulana S.Kom.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Seorang Data Analyst yang berdedikasi dengan pengalaman luas dalam analisis data, pemodelan 
statistik, dan visualisasi data. Mampu mengumpulkan, menganalisis, dan menyajikan data secara 
efektif untuk mendukung pengambilan keputusan strategis. Memiliki keahlian dalam penggunaan alat 
analisis data seperti SQL, Python,Looker dan Ms Power BI. Terampil dalam mengkomunikasikan 
hasil analisis secara jelas dan mendalam kepada para pemangku kepentingan.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Afik Maulana</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
      <a class="nav-link" href="#skill">Skill</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#my-project">My Project</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('''
## Education
''')

txt('**S1 – Sistem Informatika**, *STMIK Nusa Mandiri* ',
    '2019 – 2020')
st.markdown('''
- IPK :`3.57`
- Tugas Akhir : Analisis Data Perfect Store di PT. UNILEVER dengan Menggunakan Metode OLAP (Online Analytical Processing)
''')

txt('**DIII - Manajemen informatika**, *Bina Sarana Informatika*',
    '2017 - 2010')
st.markdown('''
- IPK: `3.47`
- Tugas Akhir : *Perancangan Dan Pembuatan Website Informasi Reparasi ponsel dengan Menggunakan PHP , Dreamweaver 8 dan MYSQL*
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Analyst & Reporting Project Customer Development**, *PT. Unilever*',
    '2017-Current')
st.markdown('''
- Mengumpulkan, membersihkan, dan menganalisis data untuk mengidentifikasi tren dan pola yang relevan. 
- Membangun model statistik untuk melakukan prediksi dan segmentasi data.
- enghasilkan laporan dan visualisasi data yang menggambarkan temuan analisis secara komprehensif.
-  Memberikan wawasan data kepada tim manajemen untuk mendukung pengambilan keputusan.
''')

txt('**Admin Support Strategic Partnership & Alliances**, *PT. Permata Bank*',
    '2013-2017')
st.markdown('''
-  Rekap Data Penjualan dari Berbagai Merchant Partner. 
-  Melakukan Proses konversi Cicilan 0'%' sesuai Perjanjian Kerjasama.
-  Melakukan Proses Pembayaran Marketing Communication.
-  Membuat Dan Mengirimkan Report ke User.
''')

txt('**Sistem Informasi Debitur (SID) Checking**, *PT. Permata Bank*',
    '2011-2013')
st.markdown('''
-  Melakukan pencarian dan pengecekan data informasi debitur sesuai dengan data. 
-  Mengumpulkan dan Mendownload Data Historical Debitur (SID) calon nasabah sesuai dengan data yang dicari.
-  Melakukan upload data debitur yang dicari ke system analyst.
-  Mengirimkan laporan hasil data yang sudah kita checking ke pihak terkait.
''')

txt('**Data Support**,  *PT Nusantara Card Semesta*',
    '2010-2011')
st.markdown('''
- Monitor terhadap schedule pick up berjalan sesuai dengan client yang menjadi tanggung jawabnya
- Melakukan proses predelivery pada level synchronize data dengan fisik kiriman , agar product kiriman bisa dilanjutkan pada proses distribusi.
- Upload data ke dalam data base system jika product kiriman sudah valid.
- Mengirimkan data melalui via email ke cabang sesuai komposisi masing masing cabang untuk proses entry level hasil kurir ke cabang.
- Updata report hasil delivery cabang kedalam data base system sebagai materi pelaporan ke client.
- Monitor performance kiriman dan Informasikan ke wilayah terkait.
- Monitor schedule reporting ke client.
- Membuat Daily report dan closing report sebagai update report hasil delivery.
- Membuat report performance Delivery ke klient sebagai akhir report yang nantinya dijadikan acuan invoice.           
''')

#####################
st.markdown('''
## Skill
''')
txt3('Programming', '`Python`, `PHP`, `Javascript`,`VBA`,`Foxpro`')
txt3('Data processing/wrangling',
     '`SQL`, `pandas`, `numpy`,`Ms.Excel`,`Power Query`,`Big Query`')
txt3('Data visualization',
     '`matplotlib`, `seaborn`, `plotly`,`Ms.Power BI`,`Looker`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Mobility development', '`Flutter`, `kivy`')
txt3('Model deployment', '`streamlit`, `render`, `R Shiny`, `Heroku`, `Azure`,`GCP`')

#####################
st.markdown('''
## My Project
''')

txt('**DTC (Document Trafic Center) Sistem**, *PT Bank Permata* ',
    '')
st.markdown('''
 - `Membuat system DTC (Document Trafic Center) dengan menggunakan mysql dan php`
''')
txt('**Perfect Store GT**, *PT Unilever* ',
    '')
st.markdown('''
 - `Membuat system DTC (Document Trafic Center) dengan menggunakan mysql dan php`
''')
txt('**Locus System**, *PT Unilever* ',
    '')
st.markdown('''
 - `Mengumpulkan dan menganalisis data kendaraan , Jarak , waktu dan Volume apakah 
Distributor yang menggunakan aplikasi locus mendapatkan efisiensi dari Jumlah 
kendaraan yang digunakan dan biaya yang dikeluarkan saat pengiriman`
''')
txt('**Otif & Utilize Promotion Budget Tracker**, *PT Unilever* ',
    '')
st.markdown('''
 - `Membuat sebuah dashboard atau tools untuk mentracker apakah Promo sampai sesuai 
waktunya dan memastikan semua promo flown ke Mobility.
Dan Mentracker dan Menganalisa penggunaan Budget per Promo`
''')
txt('**SOD & EOD Sync Tracker**, *PT Unilever* ',
    '')
st.markdown('''
 - `Membuat sebuah dashboard atau tools untuk mentracker apakah Salesman melakukan 
SOD (Start Of Day) dan EOD (End Of Day) sesuai pjp-nya`
''')
txt('**Speed To Shelf NPD MT Tracker**, *PT Unilever* ',
    '')
st.markdown('''
 - `Mengumpulkan dan Menganalisa Distribusi NPD (New Product Development)
apakah terdistribusi ke Store MT (Modern Trade) sesuai time table bisnis dan 
mengukur waktu kapan rata rata product tersebut terdistribusi di account dan Area`
''')
txt('**E-PO 2.0**, *PT Unilever* ',
    '')
st.markdown('''
 - `Membuat Dashboard Analisa Status order yang dilakukan toko apakah sudah di 
proses oleh pihak distributor menjadi invoice dan Menganalisa ketersedian Stock 
Product di Distrubutor`
''')
