import webbrowser
import pyautogui
import time
import random
import os

def opening():
    print("===========================")
    print("===== ASISTEN PYTHON! =====")
    print("===========================\n")
    print("Ketik 'bantuan' untuk lihat daftar perintah, atau 'keluar' untuk tutup asisten \n\n")

def bantuan():
    print("[Daftar Perintah]")
    print("- Music")
    print("- Youtube")
    print("- Roblox")
    print("- Google")
    print("- Minecraft")

def done():
    print("\n===========================")
    print("=== PERINTAH DIJALANKAN ===")      
    print("===========================\n")
    
def batal():
    print("\n===========================")
    print("=== PERINTAH DIBATALKAN ===")      
    print("===========================\n")

    
music = "https://music.youtube.com/watch?list=PLUtCFw418uUX_bPCM0mEjwQelMPx3nZxf&si=Uc8wkGh5s-44Cxer"
youtube = "https://youtube.com"
google = "https://google.com"
    
opening() 
    
while True:
    perintah = input("Mau minta tolong apa? ").lower().strip()
    
    if perintah == "keluar":
        done()
        print("Program akan ditutup")
        break
    elif perintah == "bantuan":
        done()
        bantuan()
    elif perintah == "music":
        webbrowser.open(music)
        time.sleep(1.5)
        lagu = random.randint(0, 10)
        for i in range(lagu):
            pyautogui.hotkey("shift", "n")
        pyautogui.press("s")
        done()
    elif perintah == "roblox":
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
        pyautogui.press("win")
        time.sleep(0.1)
        pyautogui.write("Tlauncher", interval=0.06)
        pyautogui.press("enter")
        done()
    elif perintah == "shutdown":
        konfirmasi = input("Apakah kamu yakin akan mematikan komputer? y/n ")
        if konfirmasi == "y":
            print("⚠️ Komputer akan dimatikan dalam 5 detik!")
            time.sleep(5)
            os.system("shutdown /s /t 0")
        elif konfirmasi == "n":
            batal()
        else:
            print("Maaf, saya tidak mengerti")
            
            
    else:
        print("Maaf, saya tidak mengerti")
