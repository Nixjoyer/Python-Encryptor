# Python Encryption Script (MD5 + Fernet)

This project contains a simple Python script that:

* Computes the **MD5 hash** of an input message
* Generates a **Fernet symmetric key**
* Encrypts and decrypts the input message using the key

---

# Usage

You'll be prompted to enter a message. The script will display:

* The MD5 hash of your message
* A newly generated symmetric key
* The encrypted version of your message
* The decrypted (original) message
<img width="893" height="102" alt="Screenshot_20250712_125931" src="https://github.com/user-attachments/assets/ce5e4a99-7150-4613-9241-02f43670cbd9" />

---

# Requirements

* Python 3.7 or higher
* `cryptography` package

Install it manually (if needed):

`pip install cryptography`

---

---

# Running the Script

🔹Option 1: On **NixOS (with flakes)**

Clone the repo and run:

`git clone https://github.com/your-username/encryption-script.git
cd encryption-script`

# Run directly using flakes
`nix run`

# Or enter a dev shell with Python + cryptography
`nix develop
python3 encryptor.py`

---

# Make sure `flakes` are enabled in your `/etc/nixos/configuration.nix`:

`nix.settings.experimental-features = [ "nix-command" "flakes" ];`

---

🔹 Option 2: On **Other Linux Distros/ macOS**

1. Make sure Python 3 is installed.
`sudo apt install python3.13.5  and sudo apt install python3-pip(For Debian)`
`sudo dnf install python3.13.5 and sudo dnf install python3-pip (For Fedora)`
`sudo pacman -S python3.13.5 and sudo pacman -S python-pip (For Arch)`
 
3. Install cryptography:

`pip install cryptography`

---

3. Run the script:
   
`python3 encryptor.py`

---

---

🔹 Option 3: On **Windows**

You can either:

🅰️ Use **WSL**

1. Install WSL and Ubuntu or any other distro from the Microsoft Store
2. Follow the "Other Linux" instructions above

🅱️ Or use the **Python Installer**

1. Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Open Command Prompt
3. Install cryptography:

`pip install cryptography`

4. Run:

`python encryptor.py`

---

## 📁 File Structure **For NixOS**
`
├── encryptor.py     # The encryption script
├── flake.nix        # Nix flake for reproducible builds
├── flake.lock        # Nix flake file to lock version lists for reproducible builds
└── README.md        # This file
`

---
