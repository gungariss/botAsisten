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
jendela.minsize(400, 300) 
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
password = "aku sudah mengerjakan tugas di komputer"
hitung_keluar = 0
hitung_keluar1 = 0
status_input = "normal"
github = "https://github.com/gungariss"
modelai = ""
riwayat_chat = []

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
    cetak_teks("- Music\n- Youtube\n- Roblox\n- Google\n- Minecraft\n- Kerja\n- Shutdown\n- Download Lagu\n- mc\n- Mode AI")

def opening():
    cetak_teks("===========================")
    cetak_teks("===== ASISTEN PYTHON! =====")
    cetak_teks("===========================\n")
    cetak_teks("Ketik 'bantuan' untuk lihat daftar perintah, atau 'keluar' untuk tutup asisten \n")

# ====================================================
# 4. LOGIKA UTAMA ASISTEN
# ====================================================

def panggil_ai(teks, model):
    global riwayat_chat # Gunakan variabel global memori
    
    try:
        from openai import OpenAI
        import os
        from dotenv import load_dotenv
        
        # Load variabel dari file .env
        load_dotenv()
        
        # Ambil API Key dari .env, BUKAN dari teks langsung
        api = os.getenv("GROQ_API_KEY")
        
        if not api:
            cetak_teks("AI Error: API Key tidak ditemukan! Pastikan file .env sudah dibuat.")
            return

        client = OpenAI(
            api_key=api,
            base_url="https://api.groq.com/openai/v1"
        )
        
        # Karena DeepSeek kadang menggunakan ID khusus di Groq, sesuaikan dengan nama modelmu
        # Di kode aslimu tertulis "qwen/qwen3.8-27b"
        model_digunakan = "qwen/qwen3.8-27b"
        
        instruksi = """Kamu adalah asistenku, jawab pertanyaan dengan singkat namun dengan tingkat kebenaran 100%, cek jawaban sebelum mengirim
        PENTING: Gunakan teks biasa (plain text) saja. Dilarang keras menggunakan format LaTeX (seperti \\frac atau tanda $), dan kurangi penggunaan Markdown tebal/miring. Gunakan tanda garis miring (/) untuk pecahan dan huruf 'x' atau bintang (*) untuk perkalian."""
        
        # 1. Jika riwayat kosong, masukkan instruksi sistem pertama kali
        if len(riwayat_chat) == 0:
            riwayat_chat.append({"role": "system", "content": instruksi})
            
        # 2. Masukkan pesan user yang baru ke dalam memori
        riwayat_chat.append({"role": "user", "content": teks})
        
        # 3. Kirim SELURUH memori ke AI (bukan cuma pesan terakhir)
        response = client.chat.completions.create(
            model=model_digunakan,
            messages=riwayat_chat
        )
        
        jawaban = response.choices[0].message.content
        
        # 4. Masukkan jawaban AI ke dalam memori agar diingat untuk pertanyaan selanjutnya
        riwayat_chat.append({"role": "assistant", "content": jawaban})
        
        # Opsional: Batasi memori agar tidak melebihi batas token (menyimpan 10 pesan terakhir + 1 instruksi)
        if len(riwayat_chat) > 11:
            riwayat_chat = [riwayat_chat[0]] + riwayat_chat[-10:]
            
        cetak_teks(f"AI: {jawaban} ({modelai})")
        
    except Exception as e:
        # Jika terjadi error (misal jaringan putus), hapus pertanyaan terakhir agar tidak nyangkut
        if len(riwayat_chat) > 0 and riwayat_chat[-1]["role"] == "user":
            riwayat_chat.pop()
        cetak_teks(f"AI Error: {e}")
        
def proses_perintah(event=None):
    global hitung_keluar, hitung_keluar1, status_input, modelai
    
    teks_input = kotak_input.get().strip()
    kotak_input.delete(0, tk.END) 
    
# 0. JIKA DALAM MODE AI
    if status_input == "mode_ai":
        cetak_teks(f"\n> Kamu: {teks_input}")
        
        if teks_input.lower() in ["keluar", "mode asisten"]:
            cetak_teks("AI: Sampai jumpa! Memori percakapan telah dihapus. Kembali ke mode asisten.")
            status_input = "normal"
            
            # Hapus memori percakapan saat keluar mode AI
            global riwayat_chat
            riwayat_chat.clear() 
            return
            
        elif teks_input.lower() == "model":
            pilihmodel = simpledialog.askstring("AI", "Ketik nama model:\n- chat (DeepSeek V3)\n- reasoner (DeepSeek R1)")
            if pilihmodel:
                if pilihmodel.lower() == "chat":
                    modelai = 'deepseek-chat'
                elif pilihmodel.lower() == "reasoner":
                    modelai = "deepseek-reasoner"
                else:
                    modelai = 'deepseek-chat'
                    cetak_teks(f"Asisten: Model tidak dikenal, kembali ke {modelai}")
                cetak_teks(f"Asisten: Model AI berhasil diubah menjadi {modelai}")
            return
            
        cetak_teks("AI: Sedang berpikir...")
        jendela.update()
        
        # --- MENGGUNAKAN THREADING AGAR GUI TIDAK FREEZE ---
        thread_ai = threading.Thread(target=panggil_ai, args=(teks_input, modelai))
        thread_ai.daemon = True
        thread_ai.start()
        return

    # 1. JIKA PROGRAM SEDANG MENUNGGU LINK DOWNLOAD
    if status_input == "tunggu_link":
        cetak_teks(f"\n> Kamu: {teks_input}")
        
        if teks_input:
            thread_download = threading.Thread(target=downloadlagu, args=(teks_input, cetak_teks))
            thread_download.daemon = True 
            thread_download.start() 
        else:
            cetak_teks("Asisten: Dibatalkan karena tidak ada link.")
        
        status_input = "normal"  
        return

    # 2. JIKA DALAM KONDISI NORMAL (MENGKETIK PERINTAH BIASA)
    perintah = teks_input.lower()
    cetak_teks(f"\n> Kamu: {perintah}")

    # --- FITUR KELUAR DENGAN SYARAT 2X ---
    if perintah == "keluar":
        konfirmasi = simpledialog.askstring("Konfirmasi", "Ketik passwordnya 2x sebelum keluar:")

        if konfirmasi == password:
            hitung_keluar += 1 
                
            if hitung_keluar == 1:
                cetak_teks("Asisten: Bagus! Tapi itu baru satu kali.")
                time.sleep(0.07)
                konfirmasi = simpledialog.askstring("Konfirmasi", "Ketik passwordnya 2x sebelum keluar:")
                if konfirmasi == password:
                    hitung_keluar +=1
                    if hitung_keluar == 2:
                        cetak_teks("Asisten: Konfirmasi berhasil! Selamat beristirahat.")
                        jendela.update()
                        time.sleep(2)
                        jendela.destroy()
                else:
                    cetak_teks("Asisten: Password kedua salah. Batal keluar.")
                    hitung_keluar = 0
            else:
                cetak_teks("Asisten: Maaf saya tidak mengerti")
        else:
             cetak_teks("Asisten: Password salah!")
             hitung_keluar = 0
             
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
        konfirmasi = simpledialog.askstring("Konfirmasi", "Ketik passwordnya sebelum shutdown:")
        
        if konfirmasi == password:
            hitung_keluar1 += 1 
            
            if hitung_keluar1 == 1:
                cetak_teks("Asisten: Bagus! Tapi itu baru satu kali.")
                hitung_keluar1 +=1
                konfirmasi = simpledialog.askstring("Konfirmasi", "Ketik passwordnya sebelum shutdown:")
                if konfirmasi == password:
                    if hitung_keluar1 == 2:
                        cetak_teks("Asisten: Konfirmasi berhasil! Selamat beristirahat.")
                        jendela.update()
                        time.sleep(2)
                        jendela.destroy()
                        os.system("shutdown /s /t 0")
                else:
                    cetak_teks("Asisten: Password kedua salah!")
                    hitung_keluar1 = 0
        else:
            batal()
            
    elif perintah == "kerja":
        cetak_teks("Menjalankan rutinitas kerja...")
        webbrowser.open(youtube)
        time.sleep(0.2)
        webbrowser.open(music)
        time.sleep(4.3)
        lagu = random.randint(0, 15)
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
        time.sleep(0.2)
        pyautogui.hotkey("win", "s")
        pyautogui.write("Capcut", interval=0.05)
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.hotkey("win", "s")
        pyautogui.write("obs studio", interval=0.05)
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.hotkey("win", "r")
        pyautogui.write("file:///F:/kerjaan/youtube")
        pyautogui.hotkey("enter")
        time.sleep(3.3)
        pyautogui.hotkey("alt", "tab", "tab")
        done()
        
    elif perintah == "code":
        pyautogui.hotkey("win","s")
        pyautogui.write("vscode", interval=0.05)
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.hotkey("win", "r")
        pyautogui.write("file:///F:/kerjaan/code")
        time.sleep(0.2)
        webbrowser.open(github)
        done()
        
    elif perintah == "download lagu":
        status_input = "tunggu_link" 
        cetak_teks("Asisten: Masukkan link YouTube-nya di bawah ini.")
        cetak_teks("(Tips: Bisa ketik banyak link sekaligus, pisahkan dengan spasi!)")
        return 
    
    elif perintah in ["play music", "putar music", "play musik", "putar musik"]:
        cetak_teks("Musik akan diputar...")
        time.sleep(0.1)
        putar_musik()
        done()
        
    elif perintah == "mode ai":
        status_input = "mode_ai"
        cetak_teks("Asisten: Memasuki mode AI")
        cetak_teks(f"Halo! Aku AI model {modelai}. Ada yang bisa dibantu? (ketik 'keluar' atau 'mode asisten' untuk stop)")
        
    else:
        cetak_teks("Asisten: Maaf saya tidak mengerti perintah itu")

# ====================================================
# 5. DESAIN TAMPILAN (UI) BAWAH
# ====================================================

kotak_input = tk.Entry(jendela, font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")
kotak_input.pack(side=tk.BOTTOM, padx=10, pady=(0, 10), fill=tk.X)

layar_teks = tk.Text(jendela, bg="#0c0c0c", fg="#00ff00", font=("Consolas", 10), state=tk.DISABLED)
layar_teks.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

kotak_input.bind("<Return>", proses_perintah)

opening()
kotak_input.focus() 
jendela.mainloop()