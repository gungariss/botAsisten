import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
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
   
    global hitung_keluar
    global hitung_keluar1
    
    perintah = kotak_input.get().lower().strip()
    kotak_input.delete(0, tk.END) 
    
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
        # hitung_keluar += 1 # Tambah angka penghitung sebanyak 1
        
        # if hitung_keluar == 1:
        #     cetak_teks("Asisten: Bagus! Tapi itu baru satu kali.")
        #     cetak_teks("Ketik kalimat yang sama SATU KALI LAGI untuk konfirmasi!")
        # elif hitung_keluar == 2:
        #     cetak_teks("Asisten: Konfirmasi berhasil! Selamat beristirahat.")
        #     jendela.update()
        #     time.sleep(2)
        #     jendela.destroy() 
            
    # elif perintah == "keluar":
    #     cetak_teks("Asisten: Kamu tidak bisa keluar sembarangan!")
    #     cetak_teks("Ketik passwordnya 2 kali")
        
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