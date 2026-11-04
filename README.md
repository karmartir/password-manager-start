# 🔒 Secure Password Manager (v2)

Developed by **Garen (Karen Martirosyan)**

A feature-rich, secure desktop password manager built with Python and Tkinter. While initially inspired by foundational concepts from Angela Yu's Python curriculum, this application has been independently architected, redesigned, and substantially extended with professional-grade UI/UX state management and robust security protections.

---

## ✨ Custom Engineering & Advanced Features

* **🔄 State-Machine UI & Dynamic Button Morphing:** Features a true state-driven interface where the "Search" button dynamically transforms into a "Reset" button upon a successful record lookup, returning to normal once cleared.
* **🌑 High-Contrast "Negative" Security Mode:** When viewing retrieved credentials, input fields automatically invert to a secure terminal style (`white text on a deep black background`) to visually flag locked historical data.
* **🛡️ Preventative State Locks:** The "Generate Password" button is automatically locked during searches to eliminate the risk of accidentally overwriting existing records.
* **📋 30-Second Clipboard Auto-Wipe:** Credentials generated or retrieved are automatically copied to the clipboard and scrubbed clean after exactly 30 seconds to prevent sensitive data from lingering in system memory.
* **🏗️ DRY Architecture & Strict Validation:** Implements clean, reusable file I/O helper functions (`load_data()`, `json_dump()`) and strict input validation guards against empty fields and overflow errors.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **GUI Framework:** Tkinter (Standard library)
* **Third-Party Libraries:** 
  * `pyperclip` (Cross-platform clipboard management)
* **Packaging Tool:** PyInstaller (For standalone `.exe` compilation)

---

## 🚀 Getting Started (For Testers & Developers)

If you want to run the project from source, fork it, or test it locally, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/password-manager-v2.git](https://github.com/YOUR_USERNAME/password-manager-v2.git)
cd password-manager-v2