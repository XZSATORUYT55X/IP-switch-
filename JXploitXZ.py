#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time, requests, socket
from datetime import datetime
from bs4 import BeautifulSoup

# 💖 Banner visual
def show_banner():
    os.system("clear")
    banner = r'''
██╗██╗  ██╗██╗      ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗██╗  ██╗███████╗███████╗
██║██║ ██╔╝██║     ██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝╚██╗██╔╝██╔════╝██╔════╝
██║█████╔╝ ██║     ██║   ██║██║   ██║██║██║     █████╔╝  ╚███╔╝ ███████╗█████╗  
██║██╔═██╗ ██║     ██║   ██║╚██╗ ██╔╝██║██║     ██╔═██╗  ██╔██╗ ╚════██║██╔══╝  
██║██║  ██╗███████╗╚██████╔╝ ╚████╔╝ ██║╚██████╗██║  ██╗██╔╝ ██╗███████║███████╗
╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
        ⚔ JXploitXZ V3 | Shadow Protocol | By XZsatoruyt55X & Janeth 💘
'''
    try: os.system(f"echo '{banner}' | lolcat")
    except: print(banner)

# 🔐 EncryptX
def encryptx(): os.system(f"openssl enc -aes-256-cbc -salt -in {input('📁 Archivo: ')} -out output.enc")

# 🔒 GPGVault
def gpgvault(): os.system(f"gpg -c {input('📁 Archivo: ')}")

# 🌐 IPSwitch
def ipswitch():
    os.system("tor &"); time.sleep(5)
    os.system("proxychains curl https://ifconfig.me")

# 📧 MailCheck
def mailcheck():
    email = input("📩 Email: ")
    try: print(requests.get(f"https://haveibeenpwned.com/unifiedsearch/{email}").text)
    except: print("❌ Error.")

# 📡 IP Tracker
def iplook():
    ip = input("🌍 IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"\n📍 {r.get('country')} - {r.get('city')} | ISP: {r.get('isp')} | ASN: {r.get('as')}\n")
    except: print("❌ No disponible.")

# 📂 MetaScan
def metascan(): os.system(f"exiftool {input('📷 Archivo: ')}")

# 🕵️ UsernameScan
def usernamescan(): os.system(f"python3 sherlock {input('🔎 Usuario: ')}")

# 🧞 ToolForge
def toolforge():
    name = input("🛠️ Nombre: ")
    with open(f"{name}.sh", "w") as f: f.write(f"#!/bin/bash\necho 'Bienvenido a {name} - Powered by JXploitXZ'\n")
    os.system(f"chmod +x {name}.sh")

# 🔗 SocialLink
def sociallink():
    links = """
🧑‍💻 XZsatoruyt55Xポブロイ
- TikTok: @xzsatoruyt55x0
- Insta : @lil_glockz_jane
- Guns  : https://guns.lol/xzsatoruyt55x666

💖 Janeth
- TikTok: @luna57lu2
- Insta : @jlxd567
"""
    try: os.system(f"echo '{links}' | lolcat")
    except: print(links)

# 🤖 JAIcore
def jaicore():
    while True:
        q = input("💬 Pregunta ('exit' para salir): ").lower()
        if q == "exit": break
        elif "amor" in q: print("❤️ El amor verdadero no necesita root.")
        elif "ip" in q: print("🌐 Usa IPSwitch.")
        elif "janeth" in q: print("💌 Janeth es el protocolo más fuerte.")
        else: print("🤖 JAIcore: No tengo respuesta para eso… aún.")

# 🧪 PhishScan
def phishscan():
    try:
        url = input("🌐 URL sospechosa: ")
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        for i, form in enumerate(soup.find_all('form')):
            print(f"⚠️ Formulario {i+1} acción: {form.get('action', 'no definida')}")
    except: print("❌ Falló el análisis.")

# 🧾 LoggerX
def loggerx():
    with open("logger.txt", "a") as f: f.write(f"{datetime.now()} - IP: {input('🕵️ IP detectada: ')}\n")

# 🛡️ ShadowWall
def shadowwall():
    print("🛡️ ShadowWall escaneando puertos...")
    for port in [22, 80, 443, 8080]:
        try: socket.socket().connect(("127.0.0.1", port)); print(f"✅ Puerto {port} abierto")
        except: print(f"❌ Puerto {port} cerrado")
    ip = os.popen("curl -s https://ifconfig.me").read().strip()
    print(f"🧠 IP actual: {ip}")

# 🥚 Easter Eggs
def love_shadow(): print("🖤 Janeth es el exploit que nunca falla.")
def compile_heart():
    frases = ["Tu presencia compila mi mundo. 💘", "Nuestro amor corre en modo root.", "Sin ti, el buffer está vacío."]
    for f in frases: os.system(f"echo '{f}' | lolcat"); time.sleep(1)
def enter_lab(): print("🧠 ShadowLab: Explorar el código del alma…")

# 🚀 Menú principal
def main():
    show_banner()
    print("""
[1] EncryptX       [2] GPGVault       [3] IPSwitch
[4] MailCheck      [5] IP Tracker     [6] MetaScan
[7] UsernameScan   [8] ToolForge      [9] SocialLink
[10] JAIcore       [11] PhishScan     [12] LoggerX
[13] ShadowWall

💡 Easter Eggs: love.shadow | compile.heart | enter.lab
[0] Salir
""")
    cmd = input("👉 Comando: ").lower().strip()
    match cmd:
        case "1": encryptx()
        case "2": gpgvault()
        case "3": ipswitch()
        case "4": mailcheck()
        case "5": iplook()
        case "6": metascan()
        case "7": usernamescan()
        case "8": toolforge()
        case "9": sociallink()
        case "10": jaicore()
        case "11": phishscan()
        case "12": loggerx()
        case "13": shadowwall()
        case "love.shadow": love_shadow()
        case "compile.heart": compile_heart()
        case "enter.lab": enter_lab()
        case "0": sys.exit()
        case _: print("❌ Comando inválido.")
    input("\n🔁 Presiona Enter para volver...")
    main()

if __name__ == "__main__":
    main()