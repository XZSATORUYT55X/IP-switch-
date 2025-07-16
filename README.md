
# 🔁 IPSwitcher.py – Cambia tu IP dinámicamente en Termux

**Herramienta de evasión y anonimato** creada por [XZsatoruyt55Xポブロイ], diseñada para Termux sin necesidad de root. Usa la red TOR y ProxyChains para simular rotación de IPs, estilo VPN, ideal para tareas donde necesitas privacidad o protección.

---

## 🧠 Características

- 🔒 Protección estilo VPN sin requerir acceso root
- 🌀 Rotación automática de IP cada 60 segundos
- 🔐 Conexiones cifradas a través de TOR
- 📡 Compatible con scripts Python vía ProxyChains
- 💻 Interfaz estilo hacker con banner personalizado

---

## ⚙️ Requisitos

Instala los paquetes necesarios en Termux:
```bash
pkg update
pkg install tor proxychains python curl
