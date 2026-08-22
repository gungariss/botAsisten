import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from music import downloadlagu
from music import putar_musik
import threading
import webbrowser
import pyautogui
import time
import random
import os

# ====================================================
# 1. SETUP JENDELA APLIKASI GUI
# ====================================================
jendela = tk.Tk()
jendela.title("Asisten Python")
jendela.geometry("600x450")
jendela.minsize(400, 300) # Tambahkan ini agar jendela tidak bisa ditarik terlalu kecil
jendela.configure(bg="#0c0c0c")

# ====================================================
# 2. SISTEM PERTAHANAN TOMBOL X (MUTLAK)
# ====================================================
def dilarang_tutup():
    messagebox.showwarning("Akses Ditolak!", "Tombol X sudah dimatikan!\n\nUntuk keluar, ketik kalimat rahasianya di dalam program!")


jendela.protocol("WM_DELETE_WINDOW", dilarang_tutup)

# ====================================================
# 3. VARIABEL & FUNGSI TEKS TAMPILAN
# ====================================================
music = "https://music.youtube.com/watch?list=PLUtCFw418uUX_bPCM0mEjwQelMPx3nZxf&si=Uc8wkGh5s-44Cxer"
youtube = "https://youtube.com"
google = "https://google.com"
gemini = "https://gemini.google.com"
hitung_keluar = 0
hitung_keluar1 = 0
status_input = "normal"


def cetak_teks(teks):
    layar_teks.configure(state=tk.NORMAL)
    layar_teks.insert(tk.END, teks + "\n")
    layar_teks.configure(state=tk.DISABLED)
    layar_teks.see(tk.END)
    jendela.update()

def done():
    cetak_teks("\n===========================")
    cetak_teks("=== PERINTAH DIJALANKAN ===")
    cetak_teks("===========================\n")

def batal():
    cetak_teks("\n===========================")
    cetak_teks("=== PERINTAH DIBATALKAN ===")
    cetak_teks("===========================\n")

def bantuan():
    cetak_teks("[Daftar Perintah]")
    cetak_teks("- Music\n- Youtube\n- Roblox\n- Google\n- Minecraft\n- abc\n- Shutdown")

def opening():
    cetak_teks("===========================")
    cetak_teks("===== ASISTEN PYTHON! =====")
    cetak_teks("===========================\n")
    cetak_teks("Ketik 'bantuan' untuk lihat daftar perintah, atau 'keluar' untuk tutup asisten \n")
# ====================================================
# 4. LOGIKA UTAMA ASISTEN
# ====================================================

def proses_perintah(event=None):
    global hitung_keluar, hitung_keluar1, status_input
    
    teks_input = kotak_input.get().strip()
    kotak_input.delete(0, tk.END) 
    
# 1. JIKA PROGRAM SEDANG MENUNGGU LINK DOWNLOAD
    if status_input == "tunggu_link":
        cetak_teks(f"\n> Kamu: {teks_input}")
        
        if teks_input:
            # --- MENGGUNAKAN THREADING ---
            # Kita menyuruh "pegawai baru" (thread) untuk menjalankan downloadlagu
            # Args berisi link dan fungsi cetak_teks agar file sebelah bisa nge-print ke layar
            thread_download = threading.Thread(target=downloadlagu, args=(teks_input, cetak_teks))
            
            # Daemon = True artinya jika aplikasinya di-X (tutup), downloadnya otomatis ikut berhenti
            thread_download.daemon = True 
            
            # Mulai kerjakan di latar belakang!
            thread_download.start() 
            
        else:
            cetak_teks("Asisten: Dibatalkan karena tidak ada link.")
        
        status_input = "normal"  # Kembalikan status ke normal
        # Hapus fungsi done() di sini, karena sudah di-handle oleh file ytdownloader
        return

    # 2. JIKA DALAM KONDISI NORMAL (MENGKETIK PERINTAH BIASA)
    perintah = teks_input.lower()
    cetak_teks(f"\n> Kamu: {perintah}")

    # --- FITUR KELUAR DENGAN SYARAT 2X ---
    if perintah == "keluar":
        konfirmasi = simpledialog.askstring("Konfirmasi", "Ketik passwordnya 2x sebelum keluar:")

        if konfirmasi == "aku sudah mengerjakan tugas di komputer":
                # Pastikan ada 'global hitung_keluar' di awal fungsi jika kode ini di dalam fungsi
            hitung_keluar += 1 
                
            if hitung_keluar == 1:
                cetak_teks("Asisten: Bagus! Tapi itu baru satu kali.")
                pyautogui.write("keluar")
                time.sleep(0.5)
                pyautogui.press("enter")
            elif hitung_keluar == 2:
                cetak_teks("Asisten: Konfirmasi berhasil! Selamat beristirahat.")
                jendela.update()
                time.sleep(2)
                jendela.destroy()
        
    elif perintah == "bantuan":
        bantuan()
        done()
        
    elif perintah == "music":
        cetak_teks("Memproses musik...")
        webbrowser.open(music)
        time.sleep(4)
        lagu = random.randint(4, 14)
        for i in range(lagu):
            pyautogui.hotkey("shift", "n")
        pyautogui.press("s")
        done()
        
    elif perintah == "roblox":
        cetak_teks("Membuka Roblox...")
        os.system("taskkill /f /im RobloxPlayerBeta.exe >nul 2>&1")
        os.system("taskkill /f /im Roblox.exe >nul 2>&1")
        pyautogui.press("win")
        time.sleep(0.1)
        pyautogui.write("Roblox Player", interval=0.06)
        pyautogui.press("esc")
        os.system("start roblox-player:")
        done()
        
    elif perintah == "youtube":
        webbrowser.open(youtube)
        done()
        
    elif perintah == "google":
        webbrowser.open(google)
        done()
        
    elif perintah == "minecraft":
        cetak_teks("Membuka Minecraft...")
        pyautogui.press("win")
        time.sleep(0.1)
        pyautogui.write("Tlauncher", interval=0.06)
        pyautogui.press("enter")
        done()
        
    elif perintah == "shutdown":
        # Mengganti input dengan Pop-Up dialog Tkinter
        konfirmasi = simpledialog.askstring("Konfirmasi", "Ketik passwordnya sebelum shutdown:")
        
        if konfirmasi == "aku sudah mengerjakan tugas di komputer":
            # Pastikan ada 'global hitung_keluar' di awal fungsi jika kode ini di dalam fungsi
            hitung_keluar1 += 1 
            
            if hitung_keluar1 == 1:
                cetak_teks("Asisten: Bagus! Tapi itu baru satu kali.")
                cetak_teks("Ketik perintah shutdown dan password SATU KALI LAGI untuk konfirmasi!")
            elif hitung_keluar1 == 2:
                cetak_teks("Asisten: Konfirmasi berhasil! Selamat beristirahat.")
                jendela.update()
                time.sleep(2)
                jendela.destroy()
            # cetak_teks("⚠️ Komputer akan dimatikan dalam 5 detik!")
            # jendela.update()
            # time.sleep(5)
            # for i in range(10):
            #     pyautogui.hotkey("alt", "tab")
            #     pyautogui.hotkey("alt", "f4")
            #     pyautogui.press("enter")
            # # os.system("shutdown /s /t 0")
            # cetak_teks("hello world")
            # done()
        else:
            batal()
            
    elif perintah == "abc":
        cetak_teks("Menjalankan rutinitas abc...")
        pyautogui.hotkey("win", "r")
        pyautogui.write("file:///F:/kerjaan")
        pyautogui.hotkey("enter")
        time.sleep(0.05)
        webbrowser.open(youtube)
        time.sleep(0.05)
        webbrowser.open(music)
        time.sleep(4)
        lagu = random.randint(0, 10)
        for i in range(lagu):
            pyautogui.hotkey("shift", "n")
        pyautogui.press("s")
        time.sleep(0.5)
        webbrowser.open(gemini)
        time.sleep(0.05)
        webbrowser.open(google)
        done()
    
    elif perintah == "mc":
        pyautogui.hotkey("win", "s")
        pyautogui.write("Tlauncher", interval=0.05)
        pyautogui.press("enter")
        pyautogui.hotkey("win", "s")
        pyautogui.write("Capcut")
        pyautogui.press("enter")
        pyautogui.hotkey("win", "s")
        pyautogui.write("obs studio")
        pyautogui.press("enter")
        time.sleep(3.3)
        pyautogui.hotkey("alt", "tab", "tab")
        done()
        
    elif perintah == "download lagu":
        status_input = "tunggu_link"  # Ubah status jadi menunggu link
        cetak_teks("Asisten: Masukkan link YouTube-nya di bawah ini.")
        cetak_teks("(Tips: Bisa ketik banyak link sekaligus, pisahkan dengan spasi!)")
        return # Berhenti sebentar menunggu user mengetik link
    
    elif perintah in ["play music", "putar music", "play musik", "putar musik"]:
        cetak_teks("Musik akan diputar...")
        time.sleep(0.1)
        putar_musik()
        done()
        
    else:
        cetak_teks("halo")
# ====================================================
# 5. DESAIN TAMPILAN (UI) BAWAH
# ====================================================

# 1. KOTAK INPUT DI-PACK DULUAN
# Menggunakan side=tk.BOTTOM agar posisi kotak input dikunci di bawah terlebih dahulu
kotak_input = tk.Entry(jendela, font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")
kotak_input.pack(side=tk.BOTTOM, padx=10, pady=(0, 10), fill=tk.X)

# 2. LAYAR TEKS DI-PACK SETELAHNYA
# Menggunakan side=tk.TOP dan expand=True untuk mengisi sisa ruang kosong di atas kotak input
layar_teks = tk.Text(jendela, bg="#0c0c0c", fg="#00ff00", font=("Consolas", 10), state=tk.DISABLED)
layar_teks.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Menyambungkan tombol ENTER (Return) dengan fungsi logika
kotak_input.bind("<Return>", proses_perintah)

# Persiapan sebelum aplikasi berjalan penuh
opening()
kotak_input.focus() # Otomatis taruh kursor di kotak ngetik
jendela.mainloop() # Menyala abangku! 🔥