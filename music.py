import yt_dlp
import os
import tempfile

# Tambahkan parameter 'cetak_teks' di dalam kurung
def downloadlagu(urls_string, cetak_teks):
    daftar_url = urls_string.split()
    folder_tujuan = 'F:/kerjaan/code/python/BotAsisten/Lagu' 

    # Ini adalah fungsi untuk mengirim LOG ke Tkinter
    def laporan_status(d):
        if d['status'] == 'finished':
            # Mengambil nama lagunya saja dari lokasi file yang panjang
            nama_file = d['filename'].split('\\')[-1].split('/')[-1]
            # Mengubah nama .webm/.m4a menjadi .mp3 di log
            nama_file = nama_file.rsplit('.', 1)[0] + '.mp3'
            
            # Mencetak log langsung ke layar CLI asistenmu
            cetak_teks(f"✅ Selesai didownload: {nama_file}")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3', 
            'preferredquality': '192',
        }],
        'outtmpl': f'{folder_tujuan}/%(title)s.%(ext)s',
        'ignoreerrors': True,
        'quiet': True,
        'noprogress': True,
        'progress_hooks': [laporan_status],
        # 'cookiesfrombrowser': ('edge', ), 
    }

    cetak_teks("\nAsisten: Mulai mendownload di latar belakang...")
    cetak_teks("(Kamu bisa lanjut mengetik perintah lain sambil menunggu!)")
    
    for url in daftar_url:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            cetak_teks(f"Gagal mendownload link tertentu: {e}")
            
    cetak_teks("\nAsisten: Semua proses download lagu telah selesai!")
    
    
# Lokasi folder lagu kamu
FOLDER_LAGU = r'F:\kerjaan\code\python\botAsisten\Lagu'

def putar_musik():
    if not os.path.exists(FOLDER_LAGU):
        print("Folder lagu tidak ditemukan!")
        return

    # Ambil semua file audio
    daftar_lagu = [os.path.join(FOLDER_LAGU, f) for f in os.listdir(FOLDER_LAGU) if f.endswith(('.mp3', '.m4a', '.wav'))]

    if not daftar_lagu:
        print("Belum ada lagu di dalam folder abc.")
        return

    # Simpan playlist di folder Temp agar tidak kena blokir akses/permission
    path_playlist = os.path.join(tempfile.gettempdir(), "playlist_asisten.m3u")
    
    # Tulis path lengkap setiap lagu ke file m3u
    with open(path_playlist, 'w', encoding='utf-8') as f:
        for lagu in daftar_lagu:
            f.write(lagu + '\n')

    print(f"Memutar {len(daftar_lagu)} lagu...")
    os.startfile(path_playlist)
