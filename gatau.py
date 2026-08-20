import tkinter as tk
from tkinter import messagebox
import webbrowser
import pyautogui
import time
import random
import os

# ====================================================
# 1. SETUP JENDELA APLIKASI GUI
# ====================================================
jendela = tk.Tk()
jendela.title("Asisten Python (Anti-Malas)")
jendela.geometry("600x450")
jendela.configure(bg="#0c0c0c") # Warna latar hitam khas hacker

# ====================================================
# 2. SISTEM PERTAHANAN TOMBOL X (MUTLAK)
# ====================================================
def dilarang_tutup():
    messagebox.showwarning("Akses Ditolak!", "Tombol X sudah dimatikan!\n\nUntuk keluar, ketik kalimat rahasianya di dalam program!")

# Mengganti fungsi bawaan tombol 'X' menjadi fungsi peringatan di atas
jendela.protocol("WM_DELETE_WINDOW", dilarang_tutup)

# ====================================================
# 3. VARIABEL & FUNGSI TEKS TAMPILAN
# ====================================================
music = "https://music.youtube.com/watch?list=PLUtCFw418uUX_bPCM0mEjwQelMPx3nZxf&si=Uc8wkGh5s-44Cxer"
youtube = "https://youtube.com"
google = "https://google.com"
gemini = "https://gemini.google.com"
hitung_keluar = 0

# Fungsi ini menggantikan print() agar teks muncul di layar aplikasi
def cetak_teks(teks):
    layar_teks.configure(state=tk.NORMAL)
    layar_teks.insert(tk.END, teks + "\n")
    layar_teks.configure(state=tk.DISABLED)
    layar_teks.see(tk.END)
    jendela.update() # Memperbarui layar agar tidak macet saat ada time.sleep()

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
    # Wajib tambahkan kata kunci global di sini
    global hitung_keluar 
    
    perintah = kotak_input.get().lower().strip()
    kotak_input.delete(0, tk.END) 
    
    cetak_teks(f"\n> Kamu: {perintah}")
    
    # --- FITUR KELUAR DENGAN SYARAT 2X ---
    if perintah == "hari ini aku sudah mengerjakan tugas di komputer":
        hitung_keluar += 1 # Tambah angka penghitung sebanyak 1
        
        if hitung_keluar == 1:
            cetak_teks("Asisten: Bagus! Tapi itu baru satu kali.")
            cetak_teks("Ketik kalimat yang sama SATU KALI LAGI untuk konfirmasi!")
        elif hitung_keluar == 2:
            cetak_teks("Asisten: Konfirmasi berhasil! Selamat beristirahat.")
            jendela.update()
            time.sleep(2)
            jendela.destroy() 
            
    elif perintah == "keluar":
        cetak_teks("Asisten: Kamu tidak bisa keluar sembarangan!")
        cetak_teks("Ketik passwordnya 2 kali")
        
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
        # Mengganti input(y/n) dengan Pop-Up Modern!
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah kamu yakin akan mematikan komputer?")
        if konfirmasi:
            cetak_teks("⚠️ Komputer akan dimatikan dalam 5 detik!")
            jendela.update()
            time.sleep(5)
            for i in range(10):
                pyautogui.hotkey("alt", "tab")
                pyautogui.hotkey("alt", "f4")
                pyautogui.press("enter")
            # os.system("shutdown /s /t 0")
            cetak_teks("hello world")
            done()
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
        
    else:
        cetak_teks("Maaf, saya tidak mengerti")

# ====================================================
# 5. DESAIN TAMPILAN (UI) BAWAH
# ====================================================
# Layar besar tempat teks muncul (Warna font hijau ala hacker)
layar_teks = tk.Text(jendela, bg="#0c0c0c", fg="#00ff00", font=("Consolas", 10), state=tk.DISABLED)
layar_teks.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Kotak panjang tempat kamu ngetik perintah
kotak_input = tk.Entry(jendela, font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")
kotak_input.pack(padx=10, pady=(0, 10), fill=tk.X)

# Menyambungkan tombol ENTER (Return) dengan fungsi logika
kotak_input.bind("<Return>", proses_perintah)

# Persiapan sebelum aplikasi berjalan penuh
opening()
kotak_input.focus() # Otomatis taruh kursor di kotak ngetik
jendela.mainloop() # Menyala abangku! 🔥