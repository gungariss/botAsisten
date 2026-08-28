<div align="center">

<h1>Bot Asisten</h1>

<h3>Asisten Virtual Python Berbasis GUI. Otomatisasi Desktop. Integrasi AI.</h3>

<p>Kendalikan PC Anda hanya dengan teks.<br>Pemutar musik, peluncur game, alur kerja, dan percakapan AI dalam satu jendela.</p>

<p>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square" alt="Python"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"></a>
<a href="#prasyarat"><img src="https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square" alt="Platform"></a>
<a href="main.py"><img src="https://img.shields.io/badge/GUI-Tkinter-brightgreen?style=flat-square" alt="Tkinter"></a>
</p>

<table>
<tr>
<td align="center"><b>1 Jendela</b><br><sub>antarmuka utama</sub></td>
<td align="center"><b>10+</b><br><sub>perintah otomatisasi</sub></td>
<td align="center"><b>Groq API</b><br><sub>ditenagai LLM cerdas</sub></td>
<td align="center"><b>0</b><br><sub>klik manual untuk setup</sub></td>
</tr>
</table>

<p><b>Mengubah rutinitas harian yang repetitif menjadi satu ketikan perintah.</b></p>

<hr>

</div>

<br>

**Bot Asisten** adalah asisten virtual interaktif yang dirancang khusus untuk mempermudah kegiatan Anda di depan komputer. Alih-alih mengklik banyak aplikasi untuk memulai kerja atau bermain, Anda cukup mengetikkan satu kata kunci.

---

## 📑 Daftar Isi

- [Bagian I: Memulai (Getting Started)](#bagian-i-memulai)
  - [Prasyarat](#prasyarat)
  - [Instalasi Cepat](#instalasi-cepat)
- [Bagian II: Penggunaan & Perintah](#bagian-ii-penggunaan--perintah)
  - [Otomatisasi & Alur Kerja (Workflows)](#otomatisasi--alur-kerja)
  - [Pemutar & Pengunduh Musik](#pemutar--pengunduh-musik)
  - [Mode AI Penuh](#mode-ai-penuh)
- [Bagian III: Catatan Pengembang](#bagian-iii-catatan-pengembang)

---

## Bagian I: Memulai

### Prasyarat

Bot Asisten dirancang untuk berjalan di sistem operasi **Windows**. Pastikan Anda memiliki lingkungan Python yang siap pakai.

| Modul | Kegunaan |
|---|---|
| `tkinter` | Antarmuka grafis (GUI) bawaan Python. |
| `pyautogui` | Simulasi ketikan dan kontrol keyboard/mouse. |
| `yt-dlp` | Mengunduh lagu dari YouTube dengan kualitas terbaik. |
| `openai` | Berkomunikasi dengan API Groq (DeepSeek/Qwen). |
| `python-dotenv`| Membaca kunci API secara aman dari file `.env`. |

### Instalasi Cepat

Hanya butuh waktu kurang dari dua menit untuk menyiapkan asisten ini.

```console
$ git clone https://github.com/gungariss/botAsisten.git
$ cd botAsisten
$ pip install pyautogui python-dotenv openai yt-dlp
```

Setelah repositori diunduh, Anda wajib membuat sebuah file `.env` di dalam folder utama untuk mengaktifkan fitur AI:

```env
GROQ_API_KEY=masukkan_api_key_groq_anda_disini
```

Jalankan program menggunakan command prompt atau klik ganda pada file `run.bat`:

```console
$ python main.py
```

---

## Bagian II: Penggunaan & Perintah

Semua interaksi dilakukan melalui kotak teks di bagian bawah jendela aplikasi. 

### Otomatisasi & Alur Kerja

Alih-alih membuka aplikasi satu per satu, gunakan perintah mode untuk membuka lingkungan kerja/bermain secara instan.

| Perintah | Apa yang Terjadi |
| :--- | :--- |
| `kerja` | Membuka YouTube, menyetel musik, dan menyiapkan tab Google & Gemini untuk produktivitas penuh. |
| `mc` | Alur kerja kreator: Membuka TLauncher, CapCut, OBS Studio, dan direktori penyimpanan video secara bersamaan. |
| `code` | Lingkungan developer: Membuka Visual Studio Code di folder proyek saat ini dan meluncurkan profil GitHub Anda. |
| `minecraft` | Membuka TLauncher secara instan melalui sistem pencarian Windows. |
| `roblox` | Membersihkan proses Roblox lama yang tersangkut di latar belakang (`taskkill`), lalu meluncurkan sesi Roblox Player baru. |
| `shutdown` | Mematikan PC (membutuhkan input kata sandi 2x sebagai pengaman). |
| `keluar` | Menutup aplikasi Bot Asisten (juga dilindungi kata sandi ganda). |

### Pemutar & Pengunduh Musik

Bot ini memiliki modul `music.py` khusus untuk menangani hiburan Anda.

```console
> Kamu: download lagu
Asisten: Masukkan link YouTube-nya di bawah ini.
> Kamu: https://youtube.com/watch?v=...
✅ Selesai didownload: Nama_Lagu.mp3
```

- **`download lagu`**: Mengunduh audio YouTube dalam format MP3 langsung ke folder lokal `Lagu`. Bisa menerima banyak tautan sekaligus.
- **`play music`**: Membuat *playlist* otomatis (`.m3u`) dari semua lagu di folder `Lagu` dan memutarnya di pemutar media bawaan PC Anda.
- **`music`**: Membuka YouTube Music di peramban web dan secara otomatis mengacak/melompati beberapa lagu agar Anda mendapat putaran yang segar.

### Mode AI Penuh

Bot Asisten terintegrasi dengan arsitektur LLM berkecepatan tinggi melalui Groq.

```console
> Kamu: mode ai
Asisten: Memasuki mode AI
Halo! Aku AI model qwen/qwen3.8-27b. Ada yang bisa dibantu?
> Kamu: model
Asisten: Ketik nama model: (chat/reasoner)
```

Di dalam mode ini, bot menyimpan riwayat percakapan secara dinamis (sebagai memori) sehingga dapat memahami konteks pertanyaan lanjutan Anda. Ketik `keluar` untuk menghapus memori dan kembali ke mode asisten standar.

---

## Bagian III: Catatan Pengembang

Terdapat beberapa mekanisme khusus yang ditanamkan dalam `main.py` untuk menjaga keamanan dan kelancaran eksekusi:

1. **Anti-Close (Tombol X Dimatikan):**
   Fungsi `WM_DELETE_WINDOW` ditimpa agar pengguna tidak bisa menutup jendela dengan menekan tombol silang (X). Ini mencegah aplikasi tertutup tanpa sengaja. Satu-satunya cara keluar adalah mengetik perintah `keluar` dan memasukkan *password*.

2. **Hardcoded Paths:**
   Beberapa fungsi direktori (seperti di perintah `code`, `mc`, dan variabel `FOLDER_LAGU`) merujuk pada *path* absolut seperti `F:/kerjaan/...`. **Pastikan Anda mengubah path ini** di kode sumber agar sesuai dengan tata letak direktori komputer Anda.

3. **Threading untuk AI & Download:**
   Panggilan ke Groq API dan proses unduhan `yt-dlp` diletakkan di dalam *background thread* (`threading.Thread`). Hal ini memastikan UI Tkinter tidak akan *freeze* (membeku) saat menunggu respons dari server atau saat mengunduh file besar.

<br>

<div align="center">
<sub>Dibuat dengan Python 🐍 untuk menyederhanakan hari Anda.</sub>
</div>
